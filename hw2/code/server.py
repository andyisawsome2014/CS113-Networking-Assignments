#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
#Fill in start
serverport = 6789
serverSocket.bind(('',serverport))
serverSocket.listen(1)
print ("The server is ready to receive")
#Fill in end
while True:

    #Establish the connection

    print ("Ready to serve...")
    connectionSocket, addr = serverSocket.accept() #Fill in start Fill in end
    print(addr)

    try:

        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print(message)
        f = open(filename[1:], "rb")
        outputdata = f.read()#Fill in start Fill in end
        print("output is" + str(outputdata))
        #Send one HTTP header line into socket
            #Fill in start
        httpheader = "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nData: Today\r\nContent-Length:"+str(len(outputdata))+"\r\nContent-Type: text/html\r\n\r\n"
        print(httpheader)
        connectionSocket.send(httpheader.encode())
            #Fill in end
        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()
    except IOError:
#         #Send response message for file not found
#             #Fill in Start
         responseContent="<!doctype html><html><body><h1>404 Not Found<h1></body></html>"
         response= "HTTP/1.1 404 Not Found\r\nContent-Length:"+str(len(responseContent))+"\r\nContent-Type: text/html\r\n\r\n"+responseContent
         connectionSocket.send(response.encode())
#             #Fill in end
#         #Close client socket
         connectionSocket.close()
#         #Fill in start
#         #Fill in end

serverSocket.close()