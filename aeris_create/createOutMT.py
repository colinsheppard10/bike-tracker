import json, urllib.request


data = {
  "callbackReference": {
    "callbackData": "testApp1-mt-delivery",
    "notifyURL": #use the callbackURL from Step 2 (Creating the Notification Channel) as your notifyURL
    "https://api.aerframe.aeris.com/notificationchannel/v2/1234/channels/00169bb3-e0d5-e906-331e-9f50dda27cfb/callback"
  },
  "filterCriteria": "SP:*"
}

#enter the application API key returned in the create application step below
applicationApiKey = '22222222-2222-2222-2222-222222222222'
#enter the account ID below
accountId = '1234'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/testApp1/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())
