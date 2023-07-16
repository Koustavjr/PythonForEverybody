import urllib.error,urllib.request,urllib.parse
import ssl
import xml.etree.ElementTree as ET

ctx= ssl.create_default_context
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

api = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url='https://py4e-data.dr-chuck.net/comments_1848104.xml'

u = urllib.request.urlopen(url)

ud = u.read().decode()

tree = ET.fromstring(ud)

counts=tree.findall(".//count")
s=0
for c in counts:
    s=s+int(c.text)
print(s)    
