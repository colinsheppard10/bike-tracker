import json, urllib.request

data = {
"address":[
"204043396465018" #replace this number with the imsi of the destination SIM
],
"senderAddress":"colinApp3", #sender address is the application short name 
"outboundSMSTextMessage":{
"message":"threeoheight" #enter the message to be sent
},
"clientCorrelator":"654321",
"senderName":"AFTestClient"
}

#enter the application API key returned in the create application step below
applicationApiKey = '5a265b6b-90db-11e7-a18b-7fa77add7671'
#enter the account ID below
accountId = '17380'

url = 'https://api.aerframe.aeris.com/smsmessaging/v2/' + accountId + '/outbound/colinApp3/requests?apiKey=' + applicationApiKey
header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), header)
response = urllib.request.urlopen(req)

print(response.read())