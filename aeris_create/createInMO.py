import json, urllib.request

data = {
  "callbackReference": {
    "callbackData": "colinApp4", #use appShortName in the callbackData field {appShortName}
    "notifyURL": #use the callbackURL from Step 2 (Creating the Notification Channel) as your notifyURL
    "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab/callback"
  },
  "criteria": "SP:*",
  "destinationAddress": ["colinApp4"] #use appShortName as the destinationAddress
}

#enter the application API key returned in the create application step below
applicationApiKey = '7c8fa0d8-07b6-11e8-b466-059dc9dfa5e8'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/inbound/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())

# {  
#    "callbackReference":{  
#       "notifyURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab/callback",
#       "callbackData":"colinApp4",
#       "notificationFormat":"JSON"
#    },
#    "destinationAddress":[  
#       "colinApp4"
#    ],
#    "criteria":"SP:*",
#    "resourceURL":"https://api.aerframe.aeris.com/smsmessaging/v2/17380/inbound/subscriptions/00044151-1782-940c-1a19-e11acf222416",
#    "link":[  

#    ]
# }