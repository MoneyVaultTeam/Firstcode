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
import logging

from telegram import LabeledPrice, ShippingOption
import pickle
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
API_KEY = "adf3ae04-a8a9-4f24-925d-afe4ab2f547f"
client = Client(api_key=API_KEY)
wc=['Welcome to user panel']
man=[]
heelp=['Admin will update soon']
BUTTON,AB,PHO,PID,CAT,ALI,FIL,PDB,PDVM,MCAT,BBUY,DELETE,DELCAT,SH,HALP,JE,MODF,MODFF=range(18)
def start(update, context):
    bnm=update.message.from_user
    global ms
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
        cursor.execute("INSERT INTO COMPANY (ID,balance ,link,code,pid,ppr,ct,amount,payment,quantity) \
            VALUES ({}, '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(user),"0","0","0","0","0","0","0","0","0"))
        connection.commit()
        connection.close()
        conn = sqlite3.connect('oo.db')
        conn.execute("INSERT INTO COMPANY (ID,pid,pname,number,type,amount) \
                VALUES ('{}', '{}','{}', '{}','{}','{}')".format(str(update.effective_user.id),"0","0","0","0","0")) 
        conn.commit()
    print(update.effective_user.id)
    user = update.message.from_user
    usa=str(update.effective_user.id)
    if usa == "80751603v0" or usa == "871671600" or usa== "1394902938" or usa in man:
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("Add category", callback_data="32"),InlineKeyboardButton("Delete Category", callback_data="90")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99")],
                 [InlineKeyboardButton("🙋‍♂️ Welome message", callback_data="912"),InlineKeyboardButton("❓ Set Help / Support", callback_data="913")]
                 ,[InlineKeyboardButton("🔊 Announcement", callback_data="916"),InlineKeyboardButton("Modify the Product's file", callback_data="3344")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
    else:
        loc_keyboard1 = KeyboardButton(text="🛒 Products")
        loc_keyboard2 = KeyboardButton(text="📝 Orders")
        loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
        keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON

def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    if a== '1':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send name of product',reply_markup=reply_markup)
        return AB
    elif a=='200':
        loc_keyboard1 = KeyboardButton(text="🛒 Products")
        loc_keyboard2 = KeyboardButton(text="📝 Orders")
        loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
        keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON
    elif a=="3344":
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send productID of product to modify its file',reply_markup=reply_markup)
        return MODF
    elif a== '32':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send name of category to add',reply_markup=reply_markup)
        return MCAT
    elif a=='99':
        style = xlwt.easyxf('font: bold 1, color black;')
        conn = sqlite3.connect('orders.db') 
        cursor = conn.execute("SELECT ID,price,quantity,oid,date,productID from COMPANY ")
        conn.commit() 
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            f = open("orders.txt", "w",encoding="utf-8")
            conn = sqlite3.connect('orders.db') 
            cursor = conn.execute("SELECT ID,price,quantity,oid,date,productID from COMPANY ")
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
            sheet.write(i, 5, "quantity",  style)
            sheet.write(i, 6, "order_date+time",  style)
            for row in cursor:
                    i=i+1
                    j=j+1
                    inv=row[0]
                    vgy=row[1]
                    xdrt=row[2]
                    sheet.write(i, 1, row[3], style)
                    sheet.write(i, 2, row[0], style)
                    sheet.write(i, 3, row[5],  style)
                    sheet.write(i, 4, row[1],  style)
                    sheet.write(i, 5, row[2],  style)
                    sheet.write(i, 6, row[4],  style)
            workbook.save("orders.xls")
            keyboard =[[InlineKeyboardButton("Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_document(chat_id=update.effective_user.id,document=open('orders.xls', 'rb'),reply_markup=reply_markup)
        else:
                keyboard =[[InlineKeyboardButton("❌", callback_data="100")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="You have no orders",reply_markup=reply_markup)
                return BUTTON

    elif a=='100':
        keyboard =[[InlineKeyboardButton("➕ Product", callback_data="1"),InlineKeyboardButton("❌ Product", callback_data="2")],
                 [InlineKeyboardButton("Add category", callback_data="32"),InlineKeyboardButton("Delete Category", callback_data="90")],
                 [InlineKeyboardButton("🛒 Orders", callback_data="99")],
                 [InlineKeyboardButton("🙋‍♂️ Welome message", callback_data="912"),InlineKeyboardButton("❓ Set Help / Support", callback_data="913")]
                 ,[InlineKeyboardButton("🔊 Announcement", callback_data="916"),InlineKeyboardButton("Modify the Product's file", callback_data="3344")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
        return BUTTON
    elif a=='2':
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send ProductID to delete',reply_markup=reply_markup)
            return DELETE
    elif a=="912":
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send Welcome Message',reply_markup=reply_markup)        
            return SH 
    elif a=="913":
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send help/support message',reply_markup=reply_markup)
            return HALP
    elif a== '916':

            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send announcement message',reply_markup=reply_markup)
            return JE
    elif a== '16':
        cc=update.callback_query.message.caption
        cc=cc.replace("$","")
        dv=update.callback_query.message.photo[-1].file_id
        fg=cc
        cf=update.callback_query.message.message_id
        df=cc.split("𝐈𝐃:  ")
        df=df[1]
        df=df.split("𝐏𝐫𝐢𝐜𝐞:   ")
        df=df[0]
        df=df.strip()
        dd=cc.split("𝐏𝐫𝐢𝐜𝐞:   ")
        dd=dd[1]
        dd=dd.split("𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  ")
        dd=dd[0]
        dd=dd.strip()     
        f = open( '{}.txt'.format(df), 'r' )
        lines = f.readlines()   
        lines=len(lines)     
        conn = sqlite3.connect('wallet.db')
        conn.execute("UPDATE COMPANY set pid = '{}',ppr='{}' where ID = {}".format(df,dd,int(update.effective_user.id)))
        conn.commit()
        context.bot.send_message(chat_id=update.effective_user.id,text="We have {} numbers left \nSend amount of numbers you want to buy.".format(lines))
        return BBUY 
    elif a=='90':
        keyf=[]
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 

        context.bot.send_message(chat_id=update.effective_user.id,text="Select the category to delete",reply_markup=reply_markup)  
        return DELCAT
    elif a== '927':   
      connection = sqlite3.connect("wallet.db")  
      cursor = connection.cursor()  
      cursor.execute("SELECT code FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
      for names in cursor:
        inv=names[0]
      aa=client.charge.retrieve(inv)
      b=aa['timeline']
      a=0
      for names in b:
        ax=names['status']
        if ax=="NEW":
          a=4
      for names in b:
        ax=names['status']
        if ax=="EXPIRED":
          a=3
      for names in b:
        ax=names['status']
        if ax=="PENDING":
          a=2
      for names in b:
        ax=names['status']
        if ax=="COMPLETED":
          a=1
      a=1
      if a==1:
        #cv=aa['payments']
        #for names in cv:
          #  vb=names['value']['local']['amount']
          #  vb=float(vb)
            conn = sqlite3.connect('wallet.db')
            cursor = conn.execute("SELECT pid,ppr,payment,quantity from COMPANY  where ID = {}".format(int(update.effective_user.id)))
            conn.commit()
            keyf=[]
            for row in cursor:   
                gyo=row[0]
                gtr=float(row[1])
                print(gyo)
                paid=row[2]
                qquantiy=row[3]
            
            x=gyo
            opo =int(qquantiy)
            f = open( '{}.txt'.format(x), 'r' )
            lines = f.readlines()
            vv=lines[0]
            vv=str(vv)
            n=int(opo)
            count=0 
            sib=" Numbers \n"
            for i in range(n):   
                
                sib=sib+lines[count]+">>"
                count+=1
            print(sib)
            with open('{}.txt'.format(str(update.effective_user.id)), 'w') as f:
                f.write((sib))
            f.close()
            p=int(opo)
            cp=0
            for j in range(p):
                cp+=1
                f = open( '{}.txt'.format(x),'w' )
                f.write( ''.join( lines[cp:] ) )
                f.close()
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_document(chat_id=update.effective_user.id,document=open('{}.txt'.format(str(update.effective_user.id),'rb')) ,caption="Here is your delivery\nThank you ",reply_markup=reply_markup)
            conn = sqlite3.connect("wallet.db")  
            conn.execute("UPDATE COMPANY set link = '{}', code='{}' where ID = {}".format('0','0',int(update.effective_user.id)))
            conn.commit()
            conn.close()
            yu= random.randint (0,999999)
            xg=er.today().strftime("%m/%d/%Y, %H:%M:%S")
            conn = sqlite3.connect('orders.db')
            conn.execute("INSERT INTO COMPANY (ID,price,oid,quantity,date,productID) \
                                VALUES ('{}', '{}','{}', '{}','{}','{}')".format(str(update.effective_user.id),paid,yu,qquantiy,xg,gyo))
            conn.commit()
      elif a==2:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")],[InlineKeyboardButton("Check Again", callback_data="927")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Your Transcation is detected please wait for confirmation and then click Check Again button",reply_markup=reply_markup)
        return BUTTON
      elif a==3:
            conn = sqlite3.connect("wallet.db")  
            conn.execute("UPDATE COMPANY set link = '{}', code='{}' where ID = {}".format('0','0',int(update.effective_user.id)))
            conn.commit()
            conn.close()
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Transcation Expired!",reply_markup=reply_markup)
            return BUTTON
      else:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")],[InlineKeyboardButton("Check Again", callback_data="927")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="No Transcation is detected yet",reply_markup=reply_markup)
        return BUTTON
    elif a== '9270': 
            conn = sqlite3.connect("wallet.db")  
            conn.execute("UPDATE COMPANY set link = '{}', code='{}' where ID = {}".format('0','0',int(update.effective_user.id)))
            conn.commit()
            conn.close()
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Transcation cleared!\n Go to products to buy again",reply_markup=reply_markup)
            return BUTTON
def sh(update,context):
    a=update.message.text
    wc.pop(0)
    wc.append(a)
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Welcome message updated",reply_markup=reply_markup)
    return BUTTON
def halp(update,context):
    a=update.message.text
    heelp.pop(0)
    heelp.append(a)
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Help/Support message updated",reply_markup=reply_markup)
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
def delcat(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('cat.db')
    cursor = conn.execute("DELETE from COMPANY where cat='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Category Deleted",reply_markup=reply_markup)
    return BUTTON
def delete(update,context):
    msg=update.message.text
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT productID from COMPANY  where productID = '{}'".format(str(msg)))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("DELETE  from COMPANY where productID='{}'".format(msg))
        conn.commit()

        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Product Deleted",reply_markup=reply_markup)
        return BUTTON
    else:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid ProductID",reply_markup=reply_markup)
        return DELETE
def modf(update,context):
    msg=update.message.text
    global mpd
    mpd=msg
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT productID from COMPANY  where productID = '{}'".format(str(msg)))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send new file to replace",reply_markup=reply_markup)
        return MODFF
    else:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send VALID ProductID",reply_markup=reply_markup)
        return MODF  
            
def modff(update,context):
    sd=update.message.document.file_id
    filef = context.bot.getFile(update.message.document.file_id)
    filef.download('{}.txt'.format(mpd))
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="ProductID Modified",reply_markup=reply_markup)
    return BUTTON
def bbuy(update,context):
    msg=update.message.text
    try:
        print(msg)
        msg=int(msg)
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT pid,ppr from COMPANY  where ID = {}".format(int(update.effective_user.id)))
        conn.commit()
        keyf=[]
        for row in cursor:   
            gyo=row[0]
            gtr=float(row[1])
            print(gyo)
        gtr=gtr*msg
        f = open( '{}.txt'.format(gyo), 'r' )
        liness = f.readlines()   
        liness=len(liness)
        liness=int(liness)
        print(liness)
        if msg<=liness:
            connection = sqlite3.connect("wallet.db")  
            cursor = connection.cursor()  
            cursor.execute("SELECT code,link FROM COMPANY where id= {}".format(int(update.effective_user.id)) )
            for names in cursor:
             inv=names[0]
             inv1=names[1]
             if inv=="0":
                client = Client(api_key=API_KEY)
                charge = client.charge.create(name='Telegram botShop',
                                description='Pay to add credit to your wallet',
                                pricing_type='fixed_price',
                                local_price={ 
                                "amount": gtr, 
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
                conn.execute("UPDATE COMPANY set link = '{}', code='{}', quantity='{}', payment='{}' where ID = {}".format(linka,coda,msg,gtr,int(update.effective_user.id)))
                conn.commit()
                conn.close()
                keyboard =[[InlineKeyboardButton("I have paid", callback_data="927")],[InlineKeyboardButton("🔙 Cancel Trnsacation", callback_data="200")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="BTC address: {}\nBTC amount: {}\n\n LTC address: {}\nLTC amount: {}\n\nETH address: {}\nETH amount: {}‼️ MAKE SURE TO USE PRIORITY FEE FOR FASTER\nCONFIRMATION\n‼️ Deposits are permanent and non refundable\n‼️ Double Check the BTC amount before sending\n‼️ Anything under the amount spesificed above will be considered as a Donation\n🔸 You will be funded once the BTC is confirmed\n⚠️ By Sending you agree to whats mentioned above and you will lose 10% if you underpay".format(dd,ddv,dda,ddva,ddb,ddvb),reply_markup=reply_markup)
                return BUTTON  
             else:
                keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")],[InlineKeyboardButton("Check Again", callback_data="927"),InlineKeyboardButton("Clear", callback_data="9270")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="You have pending transaction. Check again or clear to get new receipt. Thanks",reply_markup=reply_markup)
                return BUTTON
        else:
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Please try with less amount we have {} numbers left'.format(str(liness)),reply_markup=reply_markup)
            return BBUY  
    except: 
       context.bot.send_message(chat_id=update.effective_user.id,text="Send amount as number only")
       return BBUY 
def jos(update,context):
    msg=update.message.text
    print(msg)
    if msg=='🛒 Products':
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c) 
        b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
        keyf.append(b) 
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select a category to see its products",reply_markup=reply_markup)
        return PDB
    elif msg=="⁉️ Help/Support":
                keyboard = [[InlineKeyboardButton("🔙 Main Menu", callback_data='200')]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                context.bot.send_message(chat_id=update.effective_user.id,text=heelp[0],reply_markup=reply_markup)                       
                return BUTTON
    elif msg=="📝 Orders":
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("SELECT price from COMPANY where ID ='{}'".format(str(update.effective_user.id)))
        conn.commit()
        jobs = cursor.fetchall()
        if len(jobs) !=0:
                cursor = conn.execute("SELECT ID,price,quantity,oid,date,productID from COMPANY where ID ='{}'".format(str(update.effective_user.id)))
                conn.commit()
                orderss='Orders'
                for row in cursor:
                    g="Order Number: "+row[3]+"\nOrder Date: "+row[4]+"\nProductID: "+row[5]+"\nPayment: "+row[1]+"$"+"\nQuantity:"+row[2]+'\n\n'
                    orderss=orderss+g
                keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text=orderss,reply_markup=reply_markup)
                return BUTTON
        else:
                
                    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You have no orders.",reply_markup=reply_markup)
                    return BUTTON
def pdb(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)    
    c=update.callback_query.message.message_id
    context.bot.delete_message(chat_id=update.effective_user.id,
                        message_id=c)
    if msg=="🌎Main Menu":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    elif msg=="200":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    else:
        conn = sqlite3.connect('wallet.db')
        cursor=conn.execute("UPDATE COMPANY set ct = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
        conn.commit()
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name from COMPANY where category= '{}' ".format(msg))  
        conn.commit()                             
        keyf=[]
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name from COMPANY where category= '{}' ".format(msg))
            conn.commit()
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("🌎Main Menu", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Select Name of Product to view",reply_markup=reply_markup)            
            return PDVM
        else:
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no Items',reply_markup=reply_markup)
            return BUTTON
def pdvm(update,context):
    query = update.callback_query
    msg=query.data
    print(msg)
    if msg=="🌎Main Menu":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
    elif msg=="200":
            loc_keyboard1 = KeyboardButton(text="🛒 Products")
            loc_keyboard2 = KeyboardButton(text="📝 Orders")
            loc_keyboard4 = KeyboardButton(text="⁉️ Help/Support")
            keyboard = [[loc_keyboard1,loc_keyboard2],[loc_keyboard4]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup) 
    else:
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT ct from COMPANY where ID={} ".format(str(update.effective_user.id)))
        conn.commit()
        for names in cursor:
            hjj=names[0] 
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name,description,price,productID,photoid from COMPANY where category= '{}'  AND name='{}' ".format(hjj,msg))                              
            keyf=[]
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT name,description,price,productID,photoid  from COMPANY where category= '{}'  AND name='{}' ".format(hjj,msg)) 
                for row in cursor:                               
                    m="𝐍𝐚𝐦𝐞:  "+row[0]+"\n𝐈𝐃:  "+row[3]+"\n𝐏𝐫𝐢𝐜𝐞:   "+row[2]+"$"+"\n𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:  "+row[1]+"\nPrice is for 1 number."
                    keyboard =[[InlineKeyboardButton("🛒 Buy", callback_data="16"),InlineKeyboardButton("🔙 Cancel", callback_data="200")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                    context.bot.send_photo(chat_id=update.effective_user.id,photo=row[4],caption=m,reply_markup=reply_markup)
                    return BUTTON   
            else:
                        keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
                        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                        context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no Items',reply_markup=reply_markup)
                        return BUTTON
def ab(update,context):
    msg=update.message.text 
    global nm
    nm =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='send product logo.',reply_markup=reply_markup)
    return PHO 
def pho(update,context):
    msg=update.message.photo[-1].file_id
    global pha
    pha =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Product Description',reply_markup=reply_markup)
    return PID
def pid(update,context):
    msg=update.message.text
    global des
    des=msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Price of 1 number.',reply_markup=reply_markup)
    return CAT
def cat(update,context):
    msg=update.message.text
    global pc
    pc =msg
    try:
        float(msg)
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True,one_time_keyboard=True) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select category for this product",reply_markup=reply_markup)
        return ALI
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Price of product without currency symbol',reply_markup=reply_markup)
        return CAT
def ali(update,context):
    query = update.callback_query
    msg=query.data
    global cata
    cata=msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Text file of product.',reply_markup=reply_markup)
    return FIL 
def fil(update,context):
    msg=update.message.document.file_id
    yu= random.randint (0,999999)
    file1 = context.bot.getFile(update.message.document.file_id)
    file1.download('{}.txt'.format(yu))
    conn = sqlite3.connect('shop.db')
    conn.execute("INSERT INTO COMPANY (name,description,price,productID,photoid,category) \
                        VALUES ('{}', '{}','{}','{}','{}','{}')".format(nm,des,pc,yu,pha,cata))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Product added successfully" ,reply_markup=reply_markup)
    return BUTTON
def mcat(update,context):
    msg=update.message.text
    conn = sqlite3.connect('cat.db')
    conn.execute("INSERT INTO COMPANY (cat) \
                        VALUES ('{}')".format(msg))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="category added successfully" ,reply_markup=reply_markup)
    return BUTTON
    
def main():
  updater = Updater("5828423949:AAHdAVeIrKsTD6heyWhxbQtl871pZiqM8Uo", use_context=True)
  dp = updater.dispatcher
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start),MessageHandler(Filters.regex('^(🛒 Products|📝 Orders|☎️ Contact us|⁉️ Help/Support)$'), jos)],

        states={
            
        BUTTON: [CallbackQueryHandler(button)],
        PDB: [CallbackQueryHandler(pdb)],
        PDVM: [CallbackQueryHandler(pdvm)],
        AB: [MessageHandler(Filters.text, ab),CallbackQueryHandler(button)],
        PHO: [MessageHandler(Filters.photo, pho),CallbackQueryHandler(button)],
        PID: [MessageHandler(Filters.text, pid),CallbackQueryHandler(button)],
        CAT: [MessageHandler(Filters.text, cat),CallbackQueryHandler(button)],
        ALI: [CallbackQueryHandler(ali)],
        FIL: [MessageHandler(Filters.document, fil),CallbackQueryHandler(button)],
        MCAT: [MessageHandler(Filters.text, mcat),CallbackQueryHandler(button)],
        BBUY: [MessageHandler(Filters.text, bbuy),CallbackQueryHandler(button)],
        DELETE: [MessageHandler(Filters.text, delete),CallbackQueryHandler(button)],
        DELCAT: [CallbackQueryHandler(delcat)],
        SH: [MessageHandler(Filters.text, sh),CallbackQueryHandler(button)],
        JE: [MessageHandler(Filters.text, je),CallbackQueryHandler(button)],
        HALP: [MessageHandler(Filters.text, halp),CallbackQueryHandler(button)],
        MODF :[MessageHandler(Filters.text, modf),CallbackQueryHandler(button)],
        MODFF: [MessageHandler(Filters.document, modff),CallbackQueryHandler(button)],

        },  
        fallbacks=[CommandHandler('start', start)],
        allow_reentry=True
    )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()