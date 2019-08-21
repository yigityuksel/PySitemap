import argparse
from crawler import Crawler

# initializing parameters
parser = argparse.ArgumentParser(description="Sitemap generator")
parser.add_argument('--url', action="store", default="", help="For example https://www.finstead.com")
parser.add_argument('--exclude', action="store", default="", help="regex pattern to exclude. For example 'symbol/info' will exclude https://www.finstead.com/symbol/info/ORCL")
parser.add_argument('--no-verbose', action="store_true", default="", help="print verbose output")
parser.add_argument('--output', action="store", default="sitemap.xml", help="File path for output, if file exists it will be overwritten")

# parsing parameters
args = parser.parse_args()
url = args.url.rstrip("/")

found_links = []

# initializeing crawler
crawler = Crawler(url, exclude=args.exclude, no_verbose=args.no_verbose);

# fetch links
links = crawler.start()


#write into file
with open(args.output, "w") as file: 

	for link in links:
		file.write("{0}{1}\n".format(url,link))



