import sqlite3

conn = sqlite3.connect('orders.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         oid     TEXT    NOT NULL,
         name     TEXT    NOT NULL,
         date     TEXT    NOT NULL,
         username     TEXT    NOT NULL,
         productID   TEXT    NOT NULL
        
);''')
print ("Table created successfully")
conn.close()#ID,price,oid,name,username,date,productID