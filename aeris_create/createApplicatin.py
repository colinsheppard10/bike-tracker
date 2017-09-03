#the urllib package must be downloaded before the package can be imported
import json, urllib.request

#fill in all fields of data
data = {
'applicationName':'colinApplication3',
'applicationShortName':'colinApp3',
'applicationTag':'colin3',
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
#    "applicationName":"colinApplication3",
#    "applicationShortName":"colinApp3",
#    "applicationTag":"colin3",
#    "description":"A sample AerFrame application",
#    "apiKey":"5a265b6b-90db-11e7-a18b-7fa77add7671",
#    "resourceURL":"https://api.aerframe.aeris.com/registration/v2/17380/applications/002c9cec-2af8-8ed4-6713-682feab828d4",
#    "useSmppInterface":false
# }
