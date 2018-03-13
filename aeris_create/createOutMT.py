import json, urllib.request

data = {
  "callbackReference": {
    "callbackData": "testApp1-mt-delivery",
    "notifyURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab/callback"
  },
  "filterCriteria": "SP:*"
}

#enter the application API key returned in the create application step below
applicationApiKey = '7c8fa0d8-07b6-11e8-b466-059dc9dfa5e8'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/colinApp4/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())
# {  
#    "callbackReference":{  
#       "notifyURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab/callback",
#       "callbackData":"testApp1-mt-delivery",
#       "notificationFormat":"JSON"
#    },
#    "filterCriteria":"SP:*",
#    "resourceURL":"https://api.aerframe.aeris.com/smsmessaging/v2/17380/outbound/colinApp4/subscriptions/0008eace-5f86-af40-28d1-248d43fb9235",
#    "link":[  

#    ]
# }