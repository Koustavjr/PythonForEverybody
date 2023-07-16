import xml.etree.ElementTree as ET
import sqlite3
con = sqlite3.connect("trackdb.sqlite")
cur=con.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')
fname=input("enter")
if (len(fname)<1): fname="Library.xml"
def lookup(d,key):
    f=False
    for it in d:
        if f: return it.text
        if it.tag=='key' and it.text==key:
            f=True
    return None

stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict')
print(len(all))
for d in all:
    if(lookup(d,'Track ID')is None): continue
    name=lookup(d,'Name')
    artist=lookup(d,'Artist')
    album=lookup(d,'Album')
    count=lookup(d,'Play Count')
    rating=lookup(d,'Rating')
    genre=lookup(d,'Genre')
    length=lookup(d,'Total Time')
    if name is None or artist is None or genre is None or album is None :
        continue
    print(name, artist, album, genre, count, rating, length)
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
    VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    con.commit()