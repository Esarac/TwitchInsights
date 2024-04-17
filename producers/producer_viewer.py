from kafka import KafkaProducer
from json import dumps
import time
import requests
from decouple import Config, RepositoryEnv
import os

# Env values
ENV_PATH = os.path.join(os.path.dirname(__file__), '../.env')
env = Config(RepositoryEnv(ENV_PATH))
client_id = env.get('TW_API_ID')
client_secret = env.get('TW_API_SECRET')
channel_token = env.get('TW_API_TOKEN')

# Kafka producer config
producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['localhost:29092']
)

# Get viewers
run = True
while run:
    # run = False

    # Request token
    tokenRes = requests.post(
        'https://id.twitch.tv/oauth2/token',
        json={
            'client_id':client_id,
            'client_secret':client_secret,
            'grant_type':'client_credentials',
        }
    ).json()

    # Request viewers
    dataRes = requests.get(
        'https://api.twitch.tv/helix/chat/chatters?broadcaster_id=123268481&moderator_id=123268481',
        # 'https://api.twitch.tv/helix/users?login=esarac567',
        headers = {
            # 'Authorization':f'Bearer {tokenRes["access_token"]}',
            'Authorization':f"Bearer {channel_token}",
            'Client-Id':client_id,
        }
    )

    # Send info to kafka
    data = dataRes.json()['data']
    if len(data) > 0:
        producer.send("viewers-topic", value={
                "author":"Esarac",
                "data": data,
            }
        )
    
    # Wait 1 Second
    time.sleep(1)

# Url to get channel token
'https://id.twitch.tv/oauth2/authorize?response_type=token&scope=moderator:read:chatters&client_id=q2rjik5a87jljijow202xogb85zk4g&redirect_uri=http://localhost'