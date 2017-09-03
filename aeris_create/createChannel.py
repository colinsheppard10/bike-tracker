import json, urllib.request

data = {
"applicationTag":"colin1", #enter in the applicationTag field
"channelData":{
"maxNotifications":"15",
"type":"nc:LongPollingData"
},
"channelLifetime":"7200",
"channelType":"LongPolling",
"clientCorrelator":"1234"
}

#enter the application API key returned in the create application step below
applicationApiKey = '403d8413-9031-11e7-9b85-7ba95fc8fca5'
#enter the account ID below
accountId = '17380'

url = "https://api.aerframe.aeris.com/notificationchannel/v2/" + accountId + "/channels?apiKey=" + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

#use the callbackURL from this step as the notifyURL for Step 3
print(response.read())
# b'{"clientCorrelator":"1234","applicationTag":"colin1","channelType":"LongPolling","channelData":{"channelURL":"https://longpoll2.aerframe.aeris.com/notificationchannel/v2/17380/longpoll/002c5ab8-0233-1778-3135-a301d7ed000f","maxNotifications":15},"channelLifetime":7200,"callbackURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c5ab8-0233-1778-3135-a301d7ed000f/callback","resourceURL":"https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c5ab8-0233-1778-3135-a301d7ed000f"}'
