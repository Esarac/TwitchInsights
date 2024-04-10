from kafka import KafkaConsumer
from decouple import config as env
import pyodbc
import pandas as pd
from datetime import datetime

# Kafka consumer config
consumer = KafkaConsumer(
    'messages-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='messages-group-1',
    value_deserializer=lambda m: m.decode('utf-8'),
    bootstrap_servers=['localhost:29092']
)

# Connect to DB
server = env('DB_SERVER')
database = env('DB_DATABASE') 
username = env('DB_USERNAME')
password = env('DB_PASSWORD')

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Consume
for record in consumer:
    print(f'~New record inserted')
    cursor.execute("INSERT INTO Twitch.MessagesStg (Date,MsgResponse) values(?,?)", datetime.fromtimestamp(float(record.timestamp)/1000), record.value)
    cnxn.commit()

cursor.close()
    