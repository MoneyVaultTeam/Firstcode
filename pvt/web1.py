import requests
from flask import Flask, request, abort
from coinbase_commerce.webhook import Webhook
import sqlite3
from telegram import Bot
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
app = Flask(name)
bot=Bot("5926612760:AAHBHmiJd5YVOqjqgSUXSbHijS-eoLGtV7U")
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        request_sig = request.headers.get('X-CC-Webhook-Signature', None)
        event = Webhook.construct_event(request_data, request_sig,"3af2c19f-d481-4925-9da6-c2e6a8684cc1")
        et=event.type
        ko=event.data.id
        am=event.data.payments
        d=am[0]
        em=d['net']["local"]["amount"]
        et=str(et)
        print(em)
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.execute("SELECT id FROM COMPANY where code='{}'".format(ko))
        for names in cursor:
            da=names[0]
        ide=da
        if et=="charge:confirmed":
            connection = sqlite3.connect("wallet.db")  
            cursor = connection.execute("SELECT balance FROM COMPANY where id='{}'".format(da))
            jobs=cursor.fetchall()
            for names in jobs:
                da=names[0]
                em =float(em)
                nb=da+float(em)
                nb=str(nb)
                conn = sqlite3.connect("wallet.db")  
                conn.execute("UPDATE COMPANY set balance = '{}' where ID = '{}'".format(nb,ide))
                conn.commit()
                conn.close()

            em=str(em)
            bot.send_message(chat_id=ide,text="{}$ is added to your account".format(em))
        else:
            bot.send_message(chat_id=da,text="Your transcation is pending will be added on confirmation")

            

 
    return 'success', 200

if name == 'main':
    app.run()