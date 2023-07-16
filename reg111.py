import re
total=0
f1=input("Enter file name")
fn=open(f1)
for line in fn:
  num=re.findall("[0-9]+",line)
  if not num:continue
  else:
    for i in num:
       total=total+int(i)
print(total) 