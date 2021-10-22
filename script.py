import requests
import json
import time

# url = "https://bsc-blockbook.nownodes.io/api/v2/xpub/<xpub>[?page=<page>&pageSize=<size>&from=<block height>&to=<block height>&details=<basic|tokens|tokenBalances|txids|txs>&tokens=<nonzero|used|derived>]"
url = "https://eth-blockbook.nownodes.io/api/"

payload={}
headers = {
  'api-key': '0Y3Es9FydORuZAh7pkXITVSqceiGKWtb',
  'Content-Type': 'application/json'
}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

def getdata(url, headers):
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        print (response.text)
        time.sleep(3)
        getdata(url, headers)
    except:
        print ("an error as occured")
        
print(getdata(url, headers))