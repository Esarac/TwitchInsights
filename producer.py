from kafka import KafkaProducer
from json import dumps
import time
import requests
from decouple import config

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['localhost:29092']
)

run = True
while run:
    # run = False

    tokenRes = requests.post(
        'https://id.twitch.tv/oauth2/token',
        json={
            'client_id':config('CLIENT_ID'),
            'client_secret':config('CLIENT_SECRET'),
            'grant_type':'client_credentials',
        }
    ).json()

    dataRes = requests.get(
        'https://api.twitch.tv/helix/chat/chatters?broadcaster_id=123268481&moderator_id=123268481',
        # 'https://api.twitch.tv/helix/users?login=esarac567',
        headers = {
            # 'Authorization':f'Bearer {tokenRes["access_token"]}',
            'Authorization':f"Bearer {config('ESARAC_TOKEN')}",
            'Client-Id':config('CLIENT_ID'),
        }
    )

    # print(dataRes.json())

    data = dataRes.json()['data']
    if len(data) > 0:
        producer.send("viewers-topic", value={
                "author":"Esarac",
                "data": data,
            }
        )
    
    time.sleep(1)

'https://id.twitch.tv/oauth2/authorize?response_type=token&scope=moderator:read:chatters&client_id=q2rjik5a87jljijow202xogb85zk4g&redirect_uri=http://localhost'