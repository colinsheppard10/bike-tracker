#the urllib package must be downloaded before the package can be imported
import json, urllib.request

#fill in all fields of data
data = {
'applicationName':'Colin Application',
'applicationShortName':'colinApp',
'applicationTag':'colin1',
'description':'colin application 1'
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
# b'{"applicationName":"Colin Application","applicationShortName":"colinApp","applicationTag":"colin1","description":"colin application 1","apiKey":"403d8413-9031-11e7-9b85-7ba95fc8fca5","resourceURL":"https://api.aerframe.aeris.com/registration/v2/17380/applications/002c5a7a-0be2-5db6-6d67-c46435d53b1a","useSmppInterface":false}'