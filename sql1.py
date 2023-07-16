import sqlite3

con=sqlite3.connect('emaildb.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('''CREATE TABLE counts(org TEXT, count INTEGER)''')
fname=input("Enter file name")
if (len(fname) < 1): fname = 'mbox-short.txt'
fh=open(fname)

for line in fh:
    if not line.startswith('From: '):continue
    arr=line.split()
    email=arr[1]
    (ename,organisation)=email.split('@')
    cur.execute('SELECT count FROM counts where org=?',(organisation,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts(org,count) VALUES (?,1)',(organisation,))
    else:
        cur.execute('UPDATE counts SET count=count+1 WHERE org=?',(organisation,))
    con.commit()
sqlstr='SELECT org,count FROM counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()

