import json, urllib.request


data = {
  "callbackReference": {
    "callbackData": "testApp1-mt-delivery",
    "notifyURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c6123-f3d6-910b-35da-f7156565fb29/callback"
  },
  "filterCriteria": "SP:*"
}

#enter the application API key returned in the create application step below
applicationApiKey = '32037d18-9042-11e7-b819-8f25024ce5a4'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/testApp1/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())