Program 19
#database 
 import sqlite3 
 conn = sqlite3.connect('emaildb.sqlite') 
 cur = conn.cursor() 
 cur.execute( 'DROP TABLE IF EXISTS Counts) 
 cur.execute(*) 
 CREATE TABLE Counts (email TEXT, count INTEGER)) 
 fname = input('Enter file name: ') 
 if (len(fnam#Databases 
 import sqlite3 
  
 conn = sqlite3.connect('emaildb2.sqlite') 
 cur = conn.cursor() 
  
 cur.execute(''' 
 DROP TABLE IF EXISTS Counts''') 
  
 cur.execute(''' 
 CREATE TABLE Counts (org TEXT, count INTEGER)''') 
  
 fname = input('Enter file name: ') 
 if (len(fname) < 1): fname = 'mbox.txt' 
 fh = open(fname) 
 list_1 =[] 
 for line in fh: 
     if not line.startswith('From: '): continue 
     pieces = line.split() 
     email = pieces[1] 
     dom = email.find('@') 
     org = email[dom+1:len(email)] 
  
     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) 
     row = cur.fetchone() 
     if row is None: 
         cur.execute('''INSERT INTO Counts (org, count) 
                 VALUES (?, 1)''', (org,)) 
     else: 
         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', 
                     (org,)) 
 conn.commit() 
 # https://www.sqlite.org/lang_select.html 
 sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' 
  
 for row in cur.execute(sqlstr): 
     print(str(row[0]), row[1]) 
  
 cur.close() 
  
     e) < 1): fname = 'mbox-short.txt' 
      fh = open(fname) 
 for line in fh: 
       if not line.startswith('From: '): continue 
       pieces line.split() 
       email = pieces [1] 
       cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) row = cur.fetchone() I 
 if row is None: 
     cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1), (email,)) 
 else: 
      cur.execute('UPDATE Counts SET count = count 1 WHERE email = ?', (email,)) 
 conn.commit() 
 # https://www.sqlite.org/lang_select.html sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10^ prime 
 for row in cur.execute(sqlstr): 
 print(str(row[0]), row[1]) "emaildb.py" 34L, 942C written