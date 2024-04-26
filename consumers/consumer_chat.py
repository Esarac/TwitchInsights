from kafka import KafkaConsumer
from decouple import Config, RepositoryEnv
import os
import pyodbc
import pandas as pd
from datetime import datetime

# Env values
ENV_PATH = os.path.join(os.path.dirname(__file__), '../.env')
env = Config(RepositoryEnv(ENV_PATH))
server = env.get('DB_SERVER')
database = env.get('DB_DATABASE') 
username = env.get('DB_USERNAME')
password = env.get('DB_PASSWORD')

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
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Consume
print('Consumer Running!')
for record in consumer:
    print(f'~New record inserted')
    cursor.execute("INSERT INTO Twitch.MessagesStg (Date,MsgResponse) values(?,?)", datetime.fromtimestamp(float(record.timestamp)/1000), record.value)
    cnxn.commit()

cursor.close()
    