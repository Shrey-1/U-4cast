import firebase_admin
import time
import csv
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import numpy as np
from cleaning import clean_data
cred = credentials.Certificate("D:\\Projects\\U-4cast\\credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://u-4cast-93360-default-rtdb.asia-southeast1.firebasedatabase.app/start'
})

while(True):
    ref = db.reference('start')
    snapshot = ref.order_by_key().get()
    v=snapshot.popitem()
    print(v[1])
    with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)  
        writer.writerow(v)
    data = pd.read_csv("data.csv")
    clean_data(data)
    time.sleep(180)