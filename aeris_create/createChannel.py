import json, urllib.request

data = {
"applicationTag":"colin3", #enter in the applicationTag field
"channelData":{
"maxNotifications":"15",
"type":"nc:LongPollingData"
},
"channelLifetime":"7200",
"channelType":"LongPolling",
"clientCorrelator":"1234"
}

#enter the application API key returned in the create application step below
applicationApiKey = '5a265b6b-90db-11e7-a18b-7fa77add7671'
#enter the account ID below
accountId = '17380'

url = "https://api.aerframe.aeris.com/notificationchannel/v2/" + accountId + "/channels?apiKey=" + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

#use the callbackURL from this step as the notifyURL for Step 3
print(response.read())
# {
#     "clientCorrelator": "1234",
#     "applicationTag": "colin3",
#     "channelType": "LongPolling",
#     "channelData": {
#         "channelURL": "https://longpoll2.aerframe.aeris.com/notificationchannel/v2/17380/longpoll/002c9cc4-b535-6358-365d-927e990de8fb",
#         "maxNotifications": 15
#     },
#     "channelLifetime": 7200,
#     "callbackURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c9cc4-b535-6358-365d-927e990de8fb/callback",
#     "resourceURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c9cc4-b535-6358-365d-927e990de8fb"
# }