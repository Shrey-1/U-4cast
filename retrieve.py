import firebase_admin
import time
import csv
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("D:\\Projects\\U-4cast\\credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esp8266-real-time-61351-default-rtdb.asia-southeast1.firebasedatabase.app/start'
})

while(True):
    ref = db.reference('start')
    snapshot = ref.order_by_key().get()
    v=snapshot.popitem()
    with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)  
        writer.writerow(v)
    time.sleep(15)