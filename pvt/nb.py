import sqlite3 

conn = sqlite3.connect('shop.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         name          TEXT    NOT NULL,
         category        TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         productID        TEXT    NOT NULL,
         sub        TEXT    NOT NULL,
         description        TEXT    NOT NULL,
         file         TEXT    NOT NULL
);''')
print ("Table created successfully")#name,category,price,file,productid
