#热爱学习的CXQ
from socket import *

IP='127.0.0.1'
ServerPort=50000
Buflen=1024

clientsock=socket(AF_INET, SOCK_STREAM)
clientsock.connect((IP,ServerPort))

while True:
    data =input(">>> ")
    if data=='exit':
        break
    clientsock.send(data.encode())

    recved = clientsock.recv(Buflen)
    # 如果返回空bytes，表示对方关闭了连接
    if not recved:
        break

    print(recved.decode())
clientsock.close()
