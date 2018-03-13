import json, urllib.request

data = {
"address":[
"204043396465018" #replace this number with the imsi of the destination SIM
],
"senderAddress":"colinApp4", #sender address is the application short name 
"outboundSMSTextMessage":{
"message":"threeoheight" #enter the message to be sent
},
"clientCorrelator":"654321",
"senderName":"AFTestClient"
}

#enter the application API key returned in the create application step below
applicationApiKey = '7c8fa0d8-07b6-11e8-b466-059dc9dfa5e8'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/colinApp4/requests?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())
# {  
#    "address":[  
#       "204043396465018"
#    ],
#    "senderAddress":"colinApp4",
#    "senderName":"AFTestClient",
#    "outboundSMSTextMessage":{  
#       "message":"threeoheight"
#    },
#    "clientCorrelator":"654321",
#    "resourceURL":"https://api.aerframe.aeris.com/smsmessaging/v2/17380/outbound/colinApp4/requests/00043f3c-3ed3-607a-4388-3a55ca2040ec"
# }