import sqlite3 

conn = sqlite3.connect('wallet.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         balance         TEXT    NOT NULL,
         code          TEXT    NOT NULL,
         pid          TEXT    NOT NULL,
         ppr         TEXT    NOT NULL,
         ct         TEXT    NOT NULL,
         payment         TEXT    NOT NULL,
         quantity         TEXT    NOT NULL,
         amount         TEXT    NOT NULL,
         username         TEXT    NOT NULL,
         link           TEXT    NOT NULL

);''')
print ("Table created successfully")

conn.close()