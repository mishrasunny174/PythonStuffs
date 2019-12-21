import threading
import socket
import logging

HOST = "0.0.0.0"
threads = []
stop = False

def handle(client, addr, port):
	logger = logging.getLogger()
	# print(addr[0],":",addr[1])
	logger.warning("Connection from {} on {}".format(addr[0], port))
	client.close()


def serve(port):
	servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servSock.bind((HOST, port))
	servSock.listen(20)
	global stop
	while not stop:
		clientSock, clientAddr = servSock.accept()
		threading.Thread(target=handle, args=(clientSock, clientAddr, port)).start()

def honeypot(ports):
	for port in ports:
		threads.append(threading.Thread(target=serve, args=(port,)))
	for t in threads:
		t.start()

def main():
	logging.basicConfig(filename="connections.log", format="%(asctime)s %(message)s")
	honeypot([80, 22, 8080, 2222,3333,4444,5555])

if __name__ == "__main__":
	main()