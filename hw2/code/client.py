from socket import *
import sys

server_host=sys.argv[1]
server_port = sys.argv[2]
file_name=sys.argv[3]

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((server_host,int(server_port)))
httpRequest = "GET /"+file_name+" HTTP/1.1\r\nHost: "+server_host+"\r\nConnection: clse\r\nUser-agent: Malcolm\r\nAccept-language: en"

clientSocket.send(httpRequest.encode())
response = clientSocket.recv(1024)
print (response.decode())

clientSocket.close()