# for i in $(seq 84 100); do echo $i; done

# make post request
import requests
import json
import sys

# get the url from the command line
url = 'https://api.blockcypher.com/v1/eth/main/addrs?token=aff63d97d132468489b0918a2fa6742f'

# get the data from the command line
data = ''

# make the post request
response = requests.post(url, data)

# print the response
# print(response.text)

# get the response in json format
json_response = json.loads(response.text)

# print the json parameters sepparated by comma
print(json_response['address'] + "," + json_response['private'] + "," + json_response['public'])

