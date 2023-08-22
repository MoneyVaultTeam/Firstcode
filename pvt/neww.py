import telegram.ext
import telegram.ext 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import datetime
import sqlite3
import random
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
from datetime import datetime as er
import xlwt
from openpyxl import load_workbook
import sqlite3 as sql
import os
from sqlite3 import Error
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
from coinbase_commerce.client import Client
API_KEY = "4fbc31d3-1836-4508-8541-c60fd751c010"
client = Client(api_key=API_KEY)
BUTTON,AB,PID,CATE,FIL,PDB,WALL,JE,DELC,GBS,ULAW,UOL=range(12)
man=[]
weop='Welcome to Prvt Store Market!\n\nTap Market to purchase cards.\nTap Wallet to add funds & view your balance.\nTap Rules to view a list of obligatory rules.\nTap FAQs for a list of Frequently Asked Questions.Replacement Policy:\n\nIF YOU FAIL TO FOLLOW CLEAR INSTRUCTED RULES YOU WILL NOT BE REPLACED\n1. Check card on LYFT\n2. If the card is dead, message @verifiedLC with following details below\n3. Send a Screenshot/Photo that proves the card is dead.\n4. When checking card, you have an automatic 3 minute timer.\n5. Failing to check card / provide proof of card being dead past the 3 minute timer can result in no replacement.\n6. If zip code or email / number is missing this does not qualify for a replacement.\nKeep in Mind:\n\nAccounts \nReplacements for wrong password only\n\nCards\n($5, $10 & $15 Bases are NOT Eligible for replacement)\n($20 & $35 Bases are Eligible for replacement)\n\n⛔️ NOTE ⛔️ \n\n🔹1 Transaction per wallet. The wallet always changes after each completed deposit\n\n🔹If you are using CASHAPP to send BTC, always make sure to send using PRIORITY method\n\n🔹Payment BTC ONLY\n\n🔹BY PURCHASING YOU AGREE TO THESE RULES. FAILURE TO READ THEM IS NOT MY FAULT. I SHALL GIVE NO WARNINGS'
def start(update, context):
    bnm=update.message.from_user
    global ms
    try:
       ms=bnm.username
    except:
        ms=bnm.first_name
    user=update.effective_user.id
    connection = sqlite3.connect("users.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT id FROM COMPANY where id= {}".format(int(user))) 
    jobs = cursor.fetchall()
    if len(jobs) ==0:
        cursor.execute("INSERT INTO COMPANY (ID) \
            VALUES ({})".format(int(user)))
        connection.commit()
        connection.close()
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.cursor() 
        cursor.execute("INSERT INTO COMPANY (ID,balance ,link,code,pid,ppr,ct,amount,payment,quantity,username) \
            VALUES ({}, '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(user),"0","0","0","0","0","0","0","0","0",ms))
        connection.commit()
        connection.close()
        conn = sqlite3.connect('oo.db')
        conn.execute("INSERT INTO COMPANY (ID,pid,pname,number,type,amount) \
                VALUES ('{}', '{}','{}', '{}','{}','{}')".format(str(update.effective_user.id),"0","0","0","0","0")) 
        conn.commit()
    print(update.effective_user.id)
    user = update.message.from_user
    usa=str(update.effective_user.id)
    if usa == "80751603v0" or usa == "837843929" or usa== "1394902938" or usa in man:
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("🔊 Announcement", callback_data="916")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
    else:
        loc_keyboard1 = KeyboardButton(text="💳 Market")
        loc_keyboard2 = KeyboardButton(text="💰 Wallet")
        loc_keyboard3 = KeyboardButton(text="🔮 Rules")
        loc_keyboard4 = KeyboardButton(text="📃 FAQ")
        loc_keyboard5 = KeyboardButton(text="📜 Channel Updates")
        keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard3,loc_keyboard4,loc_keyboard5]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Welcome to Prvt Store Market!\nUsername: {}\nID: {}\n'.format(ms,str(update.effective_user.id))+weop,reply_markup=reply_markup)
        return BUTTON
def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    if a== '1':
        keyboard =[[InlineKeyboardButton("Accounts", callback_data="Accounts"),InlineKeyboardButton("Cards", callback_data="Cards")],[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Select Product Type you want to add',reply_markup=reply_markup)
        return UOL
    elif a== '916':
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send announcement message',reply_markup=reply_markup)
            return JE
    elif a=='100':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("🔊 Announcement", callback_data="916")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON


    elif a=='2':
        keyboard =[[InlineKeyboardButton("Accounts", callback_data="2b"),InlineKeyboardButton("Cards", callback_data="2a")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Which product you want to delete" ,reply_markup=reply_markup)
        return BUTTON

    elif a=='2a':
        keyf=[]
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT file,productID from COMPANY where category='Cards'")
        conn.commit()
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            cursor = conn.execute("SELECT file,productID from COMPANY where category='Cards'")
            conn.commit()
            keyf=[]
            for row in cursor:
                df=row[0].split("Card Number : ")
                df=df[1]
                df=df.split("Expiration Date :")
                df=df[0]
                df= str(df)[:6]
                dd=row[0].split("DOB : ")
                dd=dd[1]           
                print(dd)
                c=[InlineKeyboardButton(df, callback_data=row[1])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 

            context.bot.send_message(chat_id=update.effective_user.id,text="Select the number to delete",reply_markup=reply_markup)  
            return DELC
        else:
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='No Product to delete',reply_markup=reply_markup)
            return BUTTON
    elif a=='2b':
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT file,productID from COMPANY where category='Accounts'")
        conn.commit()
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            cursor = conn.execute("SELECT file,productID from COMPANY where category='Accounts'")
            conn.commit()
            keyf=[]
            for row in cursor:
                df=row[0].split("PP login : ")
                df=df[1]
                df=df.split("PP password : ")
                df=df[0]
                df= df.split("@")[1]
                c=[InlineKeyboardButton(df, callback_data=row[1])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 

            context.bot.send_message(chat_id=update.effective_user.id,text="Select the number to delete",reply_markup=reply_markup)  
            return DELC
        else:
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='No Product to delete',reply_markup=reply_markup)
            return BUTTON
    elif a=='99':
        style = xlwt.easyxf('font: bold 1, color black;')
        conn = sqlite3.connect('orders.db') 
        cursor = conn.execute("SELECT ID,price,oid,name,username,date,productID from COMPANY ")
        conn.commit() 
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            f = open("orders.txt", "w",encoding="utf-8")
            conn = sqlite3.connect('orders.db') 
            cursor = conn.execute("SELECT ID,price,oid,name,username,date,productID from COMPANY ")
            conn.commit()
            xa="Orders\n"
            i=0
            j=0
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Order History")
            sheet.write(i, 1, "order_id", style)
            sheet.write(i, 2, "user_id", style)
            sheet.write(i, 3, "product_id",  style)
            sheet.write(i, 4,"Price",  style)
            sheet.write(i, 5, "user_name",  style)
            sheet.write(i, 6, "Product_name",  style)
            sheet.write(i, 7, "order_date+time",  style)
            for row in cursor:
                    i=i+1
                    j=j+1
                    inv=row[0]
                    vgy=row[1]
                    xdrt=row[2]
                    sheet.write(i, 1, row[2], style)
                    sheet.write(i, 2, row[0], style)
                    sheet.write(i, 3, row[6],  style)
                    sheet.write(i, 4, row[1],  style)
                    sheet.write(i, 5, row[4],  style)
                    sheet.write(i, 6, row[3],  style)
                    sheet.write(i, 7, row[5],  style)
            workbook.save("orders.xls")
            keyboard =[[InlineKeyboardButton("Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_document(chat_id=update.effective_user.id,document=open('orders.xls', 'rb'),reply_markup=reply_markup)
        else:
                keyboard =[[InlineKeyboardButton("❌", callback_data="100")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="You have no orders",reply_markup=reply_markup)
                return BUTTON
    elif a=='200':
        keyboard =[[InlineKeyboardButton("Accounts", callback_data="acc"),InlineKeyboardButton("Cards", callback_data="car")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='What you want to buy?',reply_markup=reply_markup)
        return BUTTON
    elif a=='acc1':
        conn = sqlite3.connect('wallet.db')
        cursor=conn.execute("UPDATE COMPANY set ct = 'Accounts' where ID = {}".format(int(update.effective_user.id)))
        conn.commit() 
        keyboard =[[InlineKeyboardButton("0.75 USD PayPal-B1", callback_data="0.75 USD PayPal-B1")],[InlineKeyboardButton("2 USD PP-A1 Checked", callback_data="2 USD PP-A1 Checked")],
                [InlineKeyboardButton("2 USD YAHOO-A1", callback_data="2 USD YAHOO-A1")],[InlineKeyboardButton("60 USD SMTP - HQ", callback_data="60 USD SMTP - HQ")],
                [InlineKeyboardButton("18 USD RDP - HQ", callback_data="18 USD RDP - HQ")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='This section contains variety of different accounts',reply_markup=reply_markup)
        return GBS
    elif a=='car1':
        conn = sqlite3.connect('wallet.db')
        cursor=conn.execute("UPDATE COMPANY set ct = 'Cards' where ID = {}".format(int(update.effective_user.id)))
        conn.commit() 
        keyboard =[[InlineKeyboardButton("5 USD BASE-A1", callback_data="5 USD BASE-A1")],[InlineKeyboardButton("10 USD BASE-A1", callback_data="10 USD BASE-A1")],
                [InlineKeyboardButton("15 USD BASE-A1", callback_data="15 USD BASE-A1")],[InlineKeyboardButton("60 USD D+P-BASE-HQ", callback_data="60 USD D+P-BASE-HQ")],
                [InlineKeyboardButton("35 USD BASE-HQ", callback_data="35 USD BASE-HQ")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='This section contains variety of different cards',reply_markup=reply_markup)
        return GBS
    elif a=='acc':
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name,productID from COMPANY where category= '{}' ".format('Accounts'))  
        conn.commit()                             
        keyf=[]
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name,productID from COMPANY where category= '{}' ".format('Accounts'))
            conn.commit()
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[1])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True )
            context.bot.send_message(chat_id=update.effective_user.id,text="𝐂𝐚𝐫𝐝𝐬\nThis section contains a variety of different USA Credit / Debit cards",reply_markup=reply_markup)            
            return PDB 
    elif a=='car':
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name,productID from COMPANY where category= '{}' ".format('Cards'))  
        conn.commit()                             
        keyf=[]
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name,productID from COMPANY where category= '{}' ".format('Cards'))
            conn.commit()
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[1])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True )
            context.bot.send_message(chat_id=update.effective_user.id,text="𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬\nThis section contains a variety of different USA Credit / Debit cards",reply_markup=reply_markup)            
            return PDB   
    elif a== 'bal':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Amount you want to add. Send in digits without currency symbols. It will be counted as dollars',reply_markup=reply_markup)
        return WALL        
    elif a== '16':
        cc=update.callback_query.message.text
        fg=cc
        cf=update.callback_query.message.message_id
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT pid,balance,username from COMPANY where ID= {} ".format(update.effective_user.id))
        conn.commit()
        for row in cursor:
            bala=float(row[1])
            tep=row[2]
            rrp=row[0]
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT price,name,productID,category,file from COMPANY where productID= '{}' ".format(row[0]))
            conn.commit()
            for row in cursor:
                ggg=float(row[0])
                pari=row[1]
                ppid=row[2]
                print(ppid)
                disa=row[4]
                if ggg>=bala:
                    keyboard =[[InlineKeyboardButton("Add Balance", callback_data="bal")],[InlineKeyboardButton("🔙 Back", callback_data="100")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
                    context.bot.send_message(chat_id=update.effective_user.id,text="Purchsed Failed!\n\nSorry! You do not have enough funds to make this purchase.",reply_markup=reply_markup)
                    return BUTTON
                else:
                    bala=bala-ggg     
                    yu= random.randint (0,999999)
                    xg=er.today().strftime("%m/%d/%Y, %H:%M:%S")
                    conn = sqlite3.connect('orders.db')
                    conn.execute("INSERT INTO COMPANY (ID,price,oid,name,username,date,productID) \
                                        VALUES ('{}', '{}','{}', '{}','{}','{}','{}')".format(str(update.effective_user.id),ggg,yu,pari,tep,xg,rrp))
                    conn.commit()              
                    conn = sqlite3.connect('wallet.db')
                    cursor=conn.execute("UPDATE COMPANY set balance = '{}' where ID = {}".format(bala,int(update.effective_user.id)))
                    conn.commit() 
                    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
                    context.bot.send_message(chat_id=update.effective_user.id,text='Here is your delivery\n'+disa,reply_markup=reply_markup)
                    return BUTTON  
def je(update,context):
        msg=update.message.text
        conn = sqlite3.connect('users.db')
        cursor = conn.execute("SELECT ID from COMPANY")
        conn.commit()
        for row in cursor:
            aa=row[0]
            try:
                context.bot.send_message(chat_id=aa,text=msg)
            except:
                pass
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Message Sent",reply_markup=reply_markup)
        return BUTTON 
def delc(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    if msg=='🌎Main Menu':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("🔊 Announcement", callback_data="916")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
    else:
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("DELETE from COMPANY where productID='{}'".format(msg))
        conn.commit()
        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Product Deleted",reply_markup=reply_markup)
        return BUTTON
def gbs(update,context):
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('wallet.db')
    cursor = conn.execute("SELECT ct from COMPANY where ID= {} ".format(update.effective_user.id))
    conn.commit()
    for row in cursor:
        if row[0]=='Cards':
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT file,productID from COMPANY where sub= '{}' ".format(msg))  
            conn.commit()                             
            keyf=[]
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT file,productID,description,COUNT(productID),sub,price from COMPANY where sub= '{}' ".format(msg))
                conn.commit()
                for row in cursor:
                    print(row[0])
                    df=row[0].split("Card Number : ")
                    df=df[1]
                    df=df.split("Expiration Date :")
                    df=df[0]
                    df= str(df)[:6]
                    dd=row[0].split("DOB : ")
                    dd=dd[1]           
                    print(dd)
                    c=[InlineKeyboardButton('{}-{}'.format(df,dd), callback_data=row[1])]
                    keyf.append(c)
                    mm='Product - {}\n\n🔹Total cards: {}\n🔹Price: {}$\n🔹Extra Information: Please read the rules before purchasing if you have not read them before'.format(row[4],row[3],row[5],)
                b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
                keyf.append(b)
                reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True )
                context.bot.send_message(chat_id=update.effective_user.id,text=mm,reply_markup=reply_markup)            
                return PDB 
        else:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT file,productID from COMPANY where sub= '{}' ".format(msg))  
            conn.commit()                             
            keyf=[]
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT file,productID,description,COUNT(productID),sub,price from COMPANY where sub= '{}' ".format(msg))
                conn.commit()
                for row in cursor:
                    print(row[0])
                    df=row[0].split("PP login : ")
                    df=df[1]
                    df=df.split("PP password : ")
                    df=df[0]
                    df= df.split("@")[1]
                    c=[InlineKeyboardButton('PP Login-{}'.format(df), callback_data=row[1])]
                    keyf.append(c)
                    mm='Product - {}\n\n🔹Total logs: {}\n🔹Price: {}$\n🔹Extra Information: Please read the rules before purchasing if you have not read them before'.format(row[4],row[3],row[5],)
                b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
                keyf.append(b)
                reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True )
                context.bot.send_message(chat_id=update.effective_user.id,text=mm,reply_markup=reply_markup)            
                return PDB            
def pdb(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)    
    if msg=='🌎Main Menu':
        keyboard =[[InlineKeyboardButton("Accounts", callback_data="acc1"),InlineKeyboardButton("Cards", callback_data="car1")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text='What you want to buy?',reply_markup=reply_markup)
        return BUTTON
    else:       
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT ct from COMPANY where ID= {} ".format(update.effective_user.id))
        conn.commit()
        for row in cursor:
            if row[0]=='Cards':
                c=update.callback_query.message.message_id
                context.bot.delete_message(chat_id=update.effective_user.id,
                                    message_id=c)
                conn = sqlite3.connect('wallet.db')
                cursor=conn.execute("UPDATE COMPANY set pid = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
                conn.commit()
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT file,price,sub from COMPANY where productID= '{}' ".format(msg))  
                conn.commit()                             
                keyf=[]
                jobs = cursor.fetchall()
                if len(jobs) !=0:
                    conn = sqlite3.connect('shop.db')
                    cursor = conn.execute("SELECT file,price,sub,category from COMPANY where productID= '{}' ".format(msg))
                    conn.commit()   
                    for row in cursor:                      
                        print(row[0])
                        df=row[0].split("Card Number : ")
                        df=df[1]
                        df=df.split("Expiration Date :")
                        df=df[0]
                        df= str(df)[:6]
                        dd=row[0].split("DOB : ")
                        dd=dd[1]           
                        print(dd)
                        m='{} - {}\n\nSelected Bin: {}\n🔹Price: ${}\n🔹Extra Information: Please read the rules before purchasing if you have not read them before.'.format(row[3],row[2],df,row[1])
                        keyboard =[[InlineKeyboardButton("Buy now", callback_data="16"),InlineKeyboardButton("Back", callback_data="200")]]
                        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                        context.bot.send_message(chat_id=update.effective_user.id,text=m,reply_markup=reply_markup)
                        return BUTTON
                else:
                    keyboard =[[InlineKeyboardButton("🌎Main Menuu", callback_data="200")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text='This category contain no product',reply_markup=reply_markup)
                    return BUTTON
            else:
                c=update.callback_query.message.message_id
                context.bot.delete_message(chat_id=update.effective_user.id,
                                    message_id=c)
                conn = sqlite3.connect('wallet.db')
                cursor=conn.execute("UPDATE COMPANY set pid = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
                conn.commit()
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT file,price,sub from COMPANY where productID= '{}' ".format(msg))  
                conn.commit()                             
                keyf=[]
                jobs = cursor.fetchall()
                if len(jobs) !=0:
                    conn = sqlite3.connect('shop.db')
                    cursor = conn.execute("SELECT file,price,sub,category from COMPANY where productID= '{}' ".format(msg))
                    conn.commit()   
                    for row in cursor:                      
                        print(row[0])
                        df=row[0].split("PP login : ")
                        df=df[1]
                        df=df.split("PP password : ")
                        df=df[0]
                        df= df.split("@")[1]
                        m='{} - {}\n\nSelected Bin: {}\n🔹Price: ${}\n🔹Extra Information: Please read the rules before purchasing if you have not read them before.'.format(row[3],row[2],df,row[1])
                        keyboard =[[InlineKeyboardButton("Buy now", callback_data="16"),InlineKeyboardButton("Back", callback_data="200")]]
                        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                        context.bot.send_message(chat_id=update.effective_user.id,text=m,reply_markup=reply_markup)
                        return BUTTON
                else:
                    keyboard =[[InlineKeyboardButton("🌎Main Menuu", callback_data="200")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text='This category contain no product',reply_markup=reply_markup)
                    return BUTTON               
def wall(update,context):
    msg=update.message.text
    try:
                gty=float(msg)
                client = Client(api_key=API_KEY)
                charge = client.charge.create(name='Telegram botShop',
                                description='Pay to add credit to your wallet',
                                pricing_type='fixed_price',
                                local_price={ 
                                "amount": gty, 
                                                "currency": "USD"
                            })
                linka=charge["hosted_url"]
                coda=charge["id"] 
                codad=charge["addresses"]
                dd=codad["bitcoin"]
                codax=charge["pricing"]
                codav=codax["bitcoin"]
                ddv=codav["amount"]

                dda=codad["litecoin"]
                codaxa=charge["pricing"]
                codava=codaxa["litecoin"]
                ddva=codava["amount"]
                print(ddva)

                ddb=codad["ethereum"]
                codaxb=charge["pricing"]
                codavb=codaxb["ethereum"]
                ddvb=codavb["amount"]


                conn = sqlite3.connect("wallet.db")  
                conn.execute("UPDATE COMPANY set link = '{}', code='{}', ppr='{}',balance='1000' where ID = {}".format(linka,coda,gty,int(update.effective_user.id)))
                conn.commit()
                conn.close()
                keyboard =[[InlineKeyboardButton("🔙 Cancel Trnsacation", callback_data="200")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text=str(dd))
                context.bot.send_message(chat_id=update.effective_user.id,text="Payment link and address",reply_markup=reply_markup)                
                return BUTTON
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Price without symbol. Only in digit',reply_markup=reply_markup)
        return BUTTON
def jos(update,context):
    msg=update.message.text
    if msg=='💳 Market':
        keyboard =[[InlineKeyboardButton("Accounts", callback_data="acc1"),InlineKeyboardButton("Cards", callback_data="car1")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='What you want to buy?',reply_markup=reply_markup)
        return BUTTON
    elif msg=='💰 Wallet':  
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT balance from COMPANY where ID= {} ".format(update.effective_user.id))
        conn.commit()
        for row in cursor:
            keyboard =[[InlineKeyboardButton("Top up", callback_data="bal")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='🆔 : {}\n🏦You currently have ${} in your wallet.\n\nTo add more please click on "Top Up" and select the amount you would like to add to your wallet.'.format(str(update.effective_user.id),str(row[0])),reply_markup=reply_markup)
            return BUTTON          
    elif msg=='🔮 Rules':        
        context.bot.send_message(chat_id=update.effective_user.id,text=weop)
    elif msg=='📃 FAQ':  
        ret="Frequently Asked Questions:\n\nImportant: You can use any Wallet and it will work just fine\n\nHow to top up?\n1. Click ’Wallet’\n2. Select ‘Top Up’\n3. Select the amount u wish the top up\n4. Click the link provided or manually send the amount. Priority transactions are received quicker.\n\nYou will be credited after your transaction has confirmed.\n\nNote: If you're using CASHAPP to send BTC, make sure to use PRIORITY .\n\nHow do I receive Order?\nOnce you load your account (topped up), You can continue to the Market Section to select the bin you want. The bot will send your files instantly after the order is complete."
        context.bot.send_message(chat_id=update.effective_user.id,text=ret)
    elif msg=='📜 Channel Updates':  
        a=1
def ab(update,context):
    msg=update.message.text
    global nm
    nm=msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Descripton of product',reply_markup=reply_markup)
    return UOL
def uol(update,context):
    query = update.callback_query
    msg=query.data
    global pro
    pro =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Product Details',reply_markup=reply_markup)
    return CATE

def cate(update,context):
    msg=update.message.text
    global descp
    descp =msg
    if pro=='Cards':
        try:
            df=msg.split("Card Number : ")
            df=df[1]
            df=df.split("Expiration Date :")
            df=df[0]
            df= str(df)[:6]
            dd=msg.split("DOB : ")
            dd=dd[1]           
            print(dd)
            keyboard =[[InlineKeyboardButton("5 USD BASE-A1", callback_data="5 USD BASE-A1")],[InlineKeyboardButton("10 USD BASE-A1", callback_data="10 USD BASE-A1")],
                    [InlineKeyboardButton("15 USD BASE-A1", callback_data="15 USD BASE-A1")],[InlineKeyboardButton("60 USD D+P-BASE-HQ", callback_data="60 USD D+P-BASE-HQ")],
                    [InlineKeyboardButton("35 USD BASE-HQ", callback_data="35 USD BASE-HQ")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send Cards',reply_markup=reply_markup)
            return ULAW
        except:
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Wrong Format.Send product detials for CARDS',reply_markup=reply_markup)
            return CATE

    elif pro=='Accounts':
        try:
            df=msg.split("PP login :")
            df=df[1]
            df=df.split("PP password : ")
            df=df[0]
            keyboard =[[InlineKeyboardButton("0.75 USD PayPal-B1", callback_data="0.75 USD PayPal-B1")],[InlineKeyboardButton("2 USD PP-A1 Checked", callback_data="2 USD PP-A1 Checked")],
                    [InlineKeyboardButton("2 USD YAHOO-A1", callback_data="2 USD YAHOO-A1")],[InlineKeyboardButton("60 USD SMTP - HQ", callback_data="60 USD SMTP - HQ")],
                    [InlineKeyboardButton("18 USD RDP - HQ", callback_data="18 USD RDP - HQ")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Select account',reply_markup=reply_markup)
            return ULAW
        except:
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Wrong Format.Send product detials for ACCOUNTS',reply_markup=reply_markup)
            return CATE
    elif msg=='100':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99"),InlineKeyboardButton("🔊 Announcement", callback_data="916")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
def ulaw(update,context):
    query = update.callback_query
    msg=query.data
    global stua
    stua=msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Price without symbol. Only in digit',reply_markup=reply_markup)
    return FIL
def pid(update,context):
    msg=update.message.text
    global pri
    pri=msg

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Product file',reply_markup=reply_markup)
    return FIL

def fil(update,context):
    msg=update.message.text
    yu= random.randint (0,999999)
    try:
        msg=float(msg)
        conn = sqlite3.connect('shop.db')
        conn.execute("INSERT INTO COMPANY (name,category,price,file,productid,sub,description) \
                            VALUES ( '{}','{}','{}','{}','{}','{}','{}')".format('0',pro,msg,descp,yu,stua,'0'))
        conn.commit()
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Product added successfully" ,reply_markup=reply_markup)
        return BUTTON
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Price without symbol. Only in digit',reply_markup=reply_markup)
        return FIL   
def main():
  updater = Updater("5926612760:AAHBHmiJd5YVOqjqgSUXSbHijS-eoLGtV7U", use_context=True)
  dp = updater.dispatcher
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start),MessageHandler(Filters.regex('^(💳 Market|💰 Wallet|🔮 Rules|📃 FAQ|📜 Channel Updates)$'), jos)],

        states={
            
        BUTTON: [CallbackQueryHandler(button)],
        AB: [MessageHandler(Filters.text, ab),CallbackQueryHandler(button)],
        CATE: [MessageHandler(Filters.text, cate),CallbackQueryHandler(button)],
        UOL: [CallbackQueryHandler(uol)],
        PDB: [CallbackQueryHandler(pdb)],
        DELC: [CallbackQueryHandler(delc)],
        GBS: [CallbackQueryHandler(gbs)],
        ULAW: [CallbackQueryHandler(ulaw)],
        FIL: [MessageHandler(Filters.text, fil),CallbackQueryHandler(button)],
        PID: [MessageHandler(Filters.text, pid),CallbackQueryHandler(button)],
        WALL: [MessageHandler(Filters.text, wall),CallbackQueryHandler(button)],
        JE: [MessageHandler(Filters.text, je),CallbackQueryHandler(button)],

        },  
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()