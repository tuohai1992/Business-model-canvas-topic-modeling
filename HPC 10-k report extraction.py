import re

# Import requests to retrive Web Urls example HTML. TXT 
import requests
import datetime

# Import BeautifulSoup
from bs4 import BeautifulSoup

# import pandas
import pandas as pd
import string
from sec_api import ExtractorApi
import string
import re


extractorApi = ExtractorApi("xxx")


hpc_keywords = [
    "high performance computing",
    "high-performance computing",
    "high performance computer",
    "supercomputer*",
    "supercomputing",
    "cloud computing",
    "Cloud computing",
    "HPC cloud",
    "cloud services",
    "cloud platform",
    
]




df = pd.read_csv('/Users/lijieyi/Desktop/Business_model/10K_report_all.csv')
df = df[100000:]

# create an empty list to hold the Business column values
# business_values = []
# indexes=0
# exception =0

def keyword_in_text(keywords, text):
    text_lower = text.lower()
    for keyword in keywords:
        if keyword.endswith('*'):
            # Remove '*' for partial matching and make lowercase
            keyword = keyword[:-1].lower()
            if any(word.startswith(keyword) for word in text_lower.split()):
                return True
        else:
            # Exact match for keywords without '*', considering whole words
            if f" {keyword.lower()} " in f" {text_lower} ":
                return True
    return False


# iterate over the rows of the DataFrame
for link in df['linkToHtml']:
    if indexes % 500 == 0:  
        print(indexes)
        print(datetime.datetime.now())
    try:
        section_text = extractorApi.get_section(link, "1", "html")
    except Exception as e:
        print(f"Error with link {link}: {e}")
        business_values.append('N')
        exception+=1
        indexes += 1
        continue  

    # BeautifulSoup HTML
    section_text = BeautifulSoup(section_text, 'html.parser')


    section_text = section_text.get_text(separator='', strip=True)
    


    # Check if any hpc or healthcare keywords are in the text
    if keyword_in_text(hpc_keywords, section_text): 
        business_values.append('Y')
    else:
        business_values.append('N')
    indexes += 1
    
    
