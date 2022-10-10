import pandas as pd
import requests 
import json
from google.cloud import bigquery 
import db_dtypes

### Section 1 ###
tab1 = pd.read_excel('C:/Users/emman/Documents/GitHub/hha-data-ingestion/Data/Nigerian_Car_Prices.xlsx', 'Nigerian_Car_Prices')
tab2 = pd.read_excel('C:/Users/emman/Documents/GitHub/hha-data-ingestion/Data/Nigerian_Car_Prices.xlsx', 'Nigerian_Car_Prices_Price')

### Section 2 ###
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data') 
apiDataset = apiDataset.json() 

### Section 3 ###
client = bigquery.Client.from_service_account_json('C:/Users/emman/Documents/GitHub/hha-data-ingestion/Data/hha-507-365120-b659f92c0663.json')
query_job = client.query("SELECT * FROM `bigquery-public-data.crypto_bitcoin_cash.transactions` LIMIT 100")
results = query_job.result()
bigquery1 = pd.DataFrame(results.to_dataframe())

client = bigquery.Client.from_service_account_json('C:/Users/emman/Documents/GitHub/hha-data-ingestion/Data/hha-507-365120-b659f92c0663.json')
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results = query_job.result()
bigquery2 = pd.DataFrame(results.to_dataframe())

print(bigquery1)
print(bigquery2)