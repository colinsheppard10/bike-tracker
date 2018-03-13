import json, urllib.request

data = {
"applicationTag":"colin4", #enter in the applicationTag field
"channelData":{
"maxNotifications":"15",
"type":"nc:LongPollingData"
},
"channelLifetime":"7200",
"channelType":"LongPolling",
"clientCorrelator":"1234"
}

#enter the application API key returned in the create application step below
applicationApiKey = '7c8fa0d8-07b6-11e8-b466-059dc9dfa5e8'
#enter the account ID below
accountId = '17380'

url = "https://api.aerframe.aeris.com/notificationchannel/v2/" + accountId + "/channels?apiKey=" + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

#use the callbackURL from this step as the notifyURL for Step 3
print(response.read())
# {  
#    "clientCorrelator":"1234",
#    "applicationTag":"colin4",
#    "channelType":"LongPolling",
#    "channelData":{  
#       "channelURL":"https://longpoll2.aerframe.aeris.com/notificationchannel/v2/17380/longpoll/00043ea6-65b9-e6d7-3c23-19b0126fc2ab",
#       "maxNotifications":15
#    },
#    "channelLifetime":7200,
#    "callbackURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab/callback",
#    "resourceURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/00043ea6-65b9-e6d7-3c23-19b0126fc2ab"
# }