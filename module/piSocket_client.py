from socket import *
from select import *
import sys
from time import ctime

HOST = '172.31.32.166'
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)  # 서버에 접속하기 위한 소켓을 생성한다.

try:
    clientSocket.connect(ADDR)  # 서버에 접속을 시도한다.

except Exception as e:
    print('%s:%s' % ADDR)
    sys.exit()

print('connect is success')

while True:
    sendData = input("input data : ")
    clientSocket.send(sendData.encode())