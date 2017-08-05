import pandas as pd
from os import listdir
import json
logfiles = listdir() 

fileDict = {}
for num, file in enumerate(logfiles):
	print(str(num) +". "+ file)
	fileDict[str(num)] = file 

fileNum = input("please imput file number: ")
# filestr = pd.read_json(fileDict[fileNum], )
file = open(fileDict[fileNum], 'r',encoding='utf8')
filestr = file.read()
file.close()
filestr = json.loads(filestr)
for line in filestr:
	type(line)
	try:
		print(line)
	except:
		continue
