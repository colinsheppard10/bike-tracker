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
applicationApiKey = 'bcaf94ef-3888-11e6-9693-6d01238098ac'
#enter the account ID below
accountId = '17380'

url = "https://api.aerframe.aeris.com/notificationchannel/v2/" + accountId + "/channels?apiKey=" + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

#use the callbackURL from this step as the notifyURL for Step 3
print(response.read())