import urllib.request
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse
from tqdm import tqdm
import re
import pandas as pd
from pandas.io.json import json_normalize

crawledLinks = []

f = open('foundedLinks.txt') # Open file on read mode
urlList = f.read().split("\n") # Create a list containing all lines
f.close() # Close file

#print(len(urlList))

urlList = list(set(urlList))

#print(len(urlList))

with tqdm(total=len(urlList)) as pbar:
    for url_ in urlList:

        pbar.update(1)
        pbar.set_description("Processing")

        try:
            
            response = urllib.request.urlopen(url_)
            pageStatus = response.getcode()
            page = str(response.read())

            crawledLinks.append({
                "link" : url_,
                "status" : pageStatus
            })

        except:
            crawledLinks.append({
                "link" : url_,
                "status" : "404"
            })
			
df = pd.DataFrame.from_dict(json_normalize(crawledLinks), orient='columns')

writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})

df.to_excel(writer, sheet_name='Sheet_1', index=False)

writer.save()