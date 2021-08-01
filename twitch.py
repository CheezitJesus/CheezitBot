import socket

server = "irc.chat.twitch.tv"
port = 6667
nickname = "qoghfks"
token = "oauth:rg2dws0mpivjd0zdpw3jtu62li2vo5"
channel = "#epicseven"


def checkline(line):
    print(line.find("#epicseven :"))
    line = line[line.find("#epicseven :"):]
    line = line[12:]
    if "https://ko.surveymonkey.com" not in line:
        return 0
    

sock = socket.socket()
sock.connect((server,port))
sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')
 
print(resp)


import logging

logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s-%(message)s',
            datefmt='%Y-%m-%d+%H:%M:%S',
            handlers=[logging.FileHandler('chat.log',encoding='utf-8')])

logging.info(resp)

while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
        logging.info(resp)
        print(resp)
        checkline(resp)
sock.close()

