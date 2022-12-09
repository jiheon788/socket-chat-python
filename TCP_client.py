from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input('나: ')
        sock.send(sendData.encode('utf-8'))
        # utf-8로 인코딩하여 전송

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        # 소켓에서 1024바이트만큼을 가져오겠다 
        print(f"상대방 : {recvData.decode('utf-8')}")
        # utf-8로 디코딩하여 수신

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
# 인자는 어드레스 패밀리(AF_INET=IPv4), 소켓타입
clientSock.connect(('127.0.0.1', port))
# 127.0.0.1 자신에게 8080 포트로 연결

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))
#target은 실제로 스레드가 실행할 함수,  args그 함수에게 전달할 인자


# 실행
sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass