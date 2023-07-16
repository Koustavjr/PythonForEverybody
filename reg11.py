import re
fn=open("file1.txt")
total=0
for line in fn:
    num=re.findall("[0-9]+",line)
    if not num:
        continue
    else:
        for i in num:
            total=total+int(i)
print(total)