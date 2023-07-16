import json
import urllib.request,urllib.parse,urllib.error
url = 'https://py4e-data.dr-chuck.net/comments_1848105.json'
uh=urllib.request.urlopen(url)
data=uh.read()
info=json.loads(data)
#info=info["comments"]
s=0
for i in info["comments"]:
    s=s+int(i["count"])
print(s)