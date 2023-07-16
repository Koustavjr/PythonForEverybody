from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter:")
pos=int(input("Enter pos:"))
cou=int(input("Enter count:"))
ans=list()
while cou>0:
    print("Retriving:{}".format(url))
    html=urlopen(url,context=ctx).read()
    soap=BeautifulSoup(html,"html.parser")
    anch=soap('a')
    name=anch[pos-1].string
    ans.append(name)
    url=anch[pos-1]["href"]
    cou=cou-1
print(ans[-1])    