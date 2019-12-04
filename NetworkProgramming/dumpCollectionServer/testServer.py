import socket
import threading
import time

def handleClient(clientSock, clientAddr):
    data = b""
    while True:
        temp = clientSock.recv(4096)
        if len(temp) == 0:
            break
        data+=temp
    print("Recieved: "+data.decode())
    with open("dump/datadump-{}-{}-{}.bin".format(clientAddr[0], clientAddr[1], time.time()),"ab") as datalog:
        datalog.write(data)
    clientSock.close()

LHOST, LPORT = "0.0.0.0", 4444

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((LHOST, LPORT))
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serverSocket.listen(10)
print(f"Server listening on {LHOST}:{LPORT}")

while True:
    clientSock, clientAddr = serverSocket.accept()
    print("GOT CONNECTION "+clientAddr[0]+":"+str(clientAddr[1]))
    threading.Thread(target=handleClient, args=(clientSock, clientAddr,)).start()
