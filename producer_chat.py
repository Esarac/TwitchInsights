from kafka import KafkaProducer
from decouple import config as env
from emoji import demojize
import socket

# Kafka producer config
producer = KafkaProducer(
    value_serializer=lambda m: m.encode('utf-8'),
    bootstrap_servers=['localhost:29092']
)

# Socket config and connection
config = {
    'server' : 'irc.chat.twitch.tv',
    'port' : 6667,
    'nickname' : 'ScrapingBot',
    'token' : env('CHAT_TOKEN'),
    'channel' : '#Esarac567',
}

sock = socket.socket()
sock.connect((config['server'], config['port']))

sock.send(f"PASS {config['token']}\n".encode('utf-8'))
sock.send(f"NICK {config['nickname']}\n".encode('utf-8'))
sock.send(f"JOIN {config['channel']}\n".encode('utf-8'))

# Get messages
run = True
while run:
    # run = False
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
        producer.send("messages-topic", value=demojize(resp))