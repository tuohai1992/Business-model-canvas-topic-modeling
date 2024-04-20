import pandas as pd
from sec_api import QueryApi

api_key = 'xxxxxxx'
queryApi = QueryApi(api_key=api_key)
results = []
# Query string
query_string = "filedAt:{2000-01-01 TO 2023-01-01} AND formType:\"10-K\""

# The maximum size for each API call
size = 200

# Calculate total calls needed
total = 30000  # Set your total number of results required here

# Pagination
for i in range(0, total//size + 1):  # Adjust the range accordingly
    query = {
        "query": {"query_string": {"query": query_string}},
        "from": str(i*size),
        "size": str(size),
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    filings = queryApi.get_filings(query)
    for filing in filings['filings']:
        if filing['formType'] == "10-K":
            results.append(filing)
