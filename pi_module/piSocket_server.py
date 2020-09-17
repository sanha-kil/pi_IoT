import socket 
from _thread import *


# 쓰레드에서 실행되는 코드입니다. 

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다. 
def connectFlask(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 



    # 클라이언트가 접속을 끊을 때 까지 반복합니다. 
    while True: 

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1] , data.decode())
            print(status)

            if data.decode() == 'LIGHT ON':
                status['light'] = data.decode()
            elif data.decode() == 'LIGHT OFF':
                status['light'] = data.decode()
            elif data.decode() == 'BLIND UP':
                status['blind'] = data.decode()
            elif data.decode() == 'BLIND DOWN':
                status['blind'] = data.decode()
            else:
                continue

            if data.decode() == 'light':
                client_socket.send(str(status['light'])) 
            elif data.decode() == 'blind':
                client_socket.send(str(status['blind'])) 
            else:
                client_socket.send(data) 

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 


HOST = ''
PORT = 10000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

status = {
    'light' : 'LIGHT OFF',
    'blind' : 'BLIND UP'
}
print(status)

print('server start')

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다. 

while True: 

    print('wait')


    client_socket, addr = server_socket.accept() 
    start_new_thread(connectFlask, (client_socket, addr)) 

server_socket.close() 