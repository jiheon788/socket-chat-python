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

serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(('', port))
# serverSock.listen(1)

print('waiting...')

connectionSock, addr = serverSock.accept()

print(f'Success connect: {str(addr)}')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass