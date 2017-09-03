#the urllib package must be downloaded before the package can be imported
import json, urllib.request

#fill in all fields of data
data = {
'applicationName':'colinApplication2',
'applicationShortName':'colinApp2',
'applicationTag':'colin2',
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
# b'{"applicationName":"colinApplication2","applicationShortName":"colinApp2","applicationTag":"colin2","description":"A sample AerFrame application","apiKey":"32037d18-9042-11e7-b819-8f25024ce5a4","resourceURL":"https://api.aerframe.aeris.com/registration/v2/17380/applications/002c60c6-2ff3-0f66-6b53-aa6fa74e62c5","useSmppInterface":false}'