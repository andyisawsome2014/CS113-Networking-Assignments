from socket import *
import sys

server_host=sys.argv[1]
server_port = sys.argv[2]
file_name=sys.argv[3]

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((server_host,int(server_port)))
httpRequest = "GET /"+file_name+" HTTP/1.1\r\nHost: "+server_host+":"+server_port+"\r\nConnection: keep-alive\r\nUser-agent: Malcolm\r\nAccept-language: en"

clientSocket.send(httpRequest.encode())
response = clientSocket.recv(1024)
final=""
while response:
    final+=response.decode()
    response = clientSocket.recv(1024)
print (final)

clientSocket.close()