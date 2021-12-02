import requests
import json
import time
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# url = "https://bsc-blockbook.nownodes.io/api/v2/xpub/<xpub>[?page=<page>&pageSize=<size>&from=<block height>&to=<block height>&details=<basic|tokens|tokenBalances|txids|txs>&tokens=<nonzero|used|derived>]"
url = "https://eth-blockbook.nownodes.io/api/"
api= os.environ.get("API")

payload={}
headers = {
  'api-key': f'{api}',
  'Content-Type': 'application/json'
}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

def getdata(url, headers):
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        #print (response.text)
        
        response_json = json.loads(response.text)
        #print(response_json)
        #print (type(response_json))
        
        #time.sleep(5)
        #getdata(url, headers)
        return response.json()
    except:
        print ("an error as occured")
        
#print(getdata(url, headers))