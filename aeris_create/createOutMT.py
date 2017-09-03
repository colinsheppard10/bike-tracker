import json, urllib.request


data = {
  "callbackReference": {
    "callbackData": "testApp1-mt-delivery",
    "notifyURL": #use the callbackURL from Step 2 (Creating the Notification Channel) as your notifyURL
    "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c6063-028a-bfbd-3481-61e284be83d6/callback"
  },
  "filterCriteria": "SP:*"
}

#enter the application API key returned in the create application step below
applicationApiKey = '403d8413-9031-11e7-9b85-7ba95fc8fca5'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/testApp1/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())
