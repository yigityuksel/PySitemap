import urllib.request
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse
from tqdm import tqdm
import re

def normalize(url):
	scheme, netloc, path, qs, anchor = urlsplit(url)
	return urlunsplit((scheme, netloc, path, qs, anchor))

def is_url(url):
	
	if "http" in url or "https" in url:
		return True 
	else:
		return False

def is_document(url):
	
	if "/docs/" in url or "/static-files/" in url:
		return True 
	else:
		return False


foundedLinkList = []

f = open('sitemap2.xml') # Open file on read mode
urlList = f.read().split("\n") # Create a list containing all lines
f.close() # Close file

with tqdm(total=len(urlList)) as pbar:
	for url_ in urlList:

		pbar.update(1)
		pbar.set_description("Processing sitemap")

		if("/api/" in url_):
			#print("Skipped API url")
			continue

		#print(url_)
		url = normalize(url_)
		host_ = urlparse(url).netloc

		try:
			response = urllib.request.urlopen(url)
			page = str(response.read())
			pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'
			found_links = re.findall(pattern, page)

			for link in found_links:
				if(is_url(link) and is_document(link)):
					#print("\t" + link)
					foundedLinkList.append(link)
		except:
			continue
			
with open("foundedLinks.txt", "w") as file: 

	for link in foundedLinkList:
		file.write("{0}\n".format(link))