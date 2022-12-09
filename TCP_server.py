from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input('나: ')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print(f"상대방: {recvData.decode('utf-8')}")

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
# AF_INET에서 ''는 INADDR_ANY를 의미, 모든 인터페이스와 연결가능
serverSock.listen(1)
# 상대의 접속 대기

print('waiting...')

connectionSock, addr = serverSock.accept()
# 상대가 접속하면 실행, 새로운 소켓과 상대의 어드레스 패밀리 반환

print(f'Success connect: {str(addr)}')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass