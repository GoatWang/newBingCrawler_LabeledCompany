from bs4 import BeautifulSoup


def QueueTramsfering(Queue):
	Qlist = []
	while True:
		try:
			Qlist.append(Queue.get(timeout=1))
		except:
			break
	return Qlist


def BingLinkParser(driver, query):
    url = "https://www.bing.com/"
    driver.get(url)
    elem = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
    elem.send_keys(query)
    elem = driver.find_element_by_xpath('//*[@id="sb_form_go"]')
    elem.submit()
    html = driver.page_source
    driver.close()

    soup = BeautifulSoup(html, 'lxml')
    Links = soup.find_all('a')

    Goodlinks = []
    for link in Links:
        linkstr = str(link)
        if (('http' in linkstr) and ('href' in linkstr) and (not 'href="#"' in linkstr) and (not 'href="http://go.microsoft' in linkstr)and (not 'microsofttranslator' in linkstr)):
            Goodlinks.append(link)

    urls = [link['href'] for link in Goodlinks]

    return urls