import pandas as pd
from os import listdir
import string

files = listdir("../labelData")
files = [file for file in files if "csv" in file]

input_companies = []
for file in files:
    df_comps = pd.read_csv("../labelData/" + file, index_col=None, header=None)

    companyTupleList = []
    def buildTupleList(row):
        companyTuple = (row[0], row[1])
        companyTupleList.append(companyTuple)

    df_comps.apply(buildTupleList, axis=1)

    for company, related in companyTupleList:
        companyDict = {}
        companyDict['name'] = company
        companyDict['query'] = "{} product".format(company)
        companyDict['related'] = related

        exclude = set(string.punctuation)
        companyName = ''.join(p for p in company if p not in exclude)
        companyName = companyName.replace(" ", "_").lower()  ##Build self.companyName
        companyDict['filename'] = companyName

        companyDict['targetCompany'] = file.replace(".csv", "")
        input_companies.append(companyDict)

pd.DataFrame(input_companies).to_csv("CompanyStats.csv")