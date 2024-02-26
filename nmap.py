import requests
import re
from urllib.parse import urljoin

target_url = "https://hackerone.com"
target_links = []





def extract_links_from(link):
	response = requests.get(link)

	return re.findall('(?:href=")(.*?)"',str(response.content))



def crawl(url):
	href_links = extract_links_from(url)


	for link in href_links:
		link = urljoin(url,link)

		if "#" in link:	
			link = link.split("#")[0]
		if target_url in link and link not in target_links: 
			target_links.append(link)
			print ("\n",link)
			crawl(link) 

crawl(target_url)





