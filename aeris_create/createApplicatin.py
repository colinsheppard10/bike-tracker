#the urllib package must be downloaded before the package can be imported
import json, urllib.request

#fill in all fields of data
data = {
'applicationName':'colinApplication4',
'applicationShortName':'colinApp4',
'applicationTag':'colin4',
'description':'A sample AerFrame application'
}

#enter the account API key below
accountApiKey = "bcaf94ef-3888-11e6-9693-6d01238098ac"
#enter the account ID below
accountId = "17380"

url = "https://api.aerframe.aeris.com/registration/v2/" + accountId + "/applications?apiKey=" + accountApiKey

header = {'Content-Type':'application/json'}

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'),header)
response = urllib.request.urlopen(req)

#response will return the unique application apiKey
print(response.read())
# {  
#    "applicationName":"colinApplication4",
#    "applicationShortName":"colinApp4",
#    "applicationTag":"colin4",
#    "description":"A sample AerFrame application",
#    "apiKey":"7c8fa0d8-07b6-11e8-b466-059dc9dfa5e8",
#    "resourceURL":"https://api.aerframe.aeris.com/registration/v2/17380/applications/00043e09-e15e-4a76-6eb5-9b85baf1bf28",
#    "useSmppInterface":false
# }
