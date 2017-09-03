import json, urllib.request


data = {
  "callbackReference": {
    "callbackData": "testApp1-mt-delivery",
    "notifyURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c9cc4-b535-6358-365d-927e990de8fb/callback"
  },
  "filterCriteria": "SP:*"
}

#enter the application API key returned in the create application step below
applicationApiKey = '5a265b6b-90db-11e7-a18b-7fa77add7671'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/colinApp3/subscriptions?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())
# {
#     "callbackReference": {
#         "notifyURL": "https://api.aerframe.aeris.com/notificationchannel/v2/17380/channels/002c9cc4-b535-6358-365d-927e990de8fb/callback",
#         "callbackData": "testApp1-mt-delivery",
#         "notificationFormat": "JSON"
#     },
#     "filterCriteria": "SP:*",
#     "resourceURL": "https://api.aerframe.aeris.com/smsmessaging/v2/17380/outbound/colinApp3/subscriptions/002c9de7-ada9-6c96-2efa-b7de74b0ddb3",
#     "link": []
# }