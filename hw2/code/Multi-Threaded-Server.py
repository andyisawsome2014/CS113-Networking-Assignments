from socket import *
import threading

threads=[]

class clientThread(threading.Thread):
    def __init__(self,connectionSocket):
        threading.Thread.__init__(self)
        self.connectionSocket=connectionSocket
    def run(self):

        try:
            message = self.connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:], "rb")
            outputdata = f.read()
            print("output is" + str(outputdata))

            httpheader = "HTTP/1.1 200 OK\r\nConnection: close\r\nData: Today\r\nContent-Length:" + str(
                len(outputdata)) + "\r\nContent-Type: text/html\r\n\r\n"
            print(httpheader)
            self.connectionSocket.send(httpheader.encode())

            for i in range(0, len(outputdata)):
                self.connectionSocket.send(outputdata[i:i + 1])
            self.connectionSocket.send(b'\r\n\r\n')
            self.connectionSocket.close()

        except IOError:

            responseContent = "<!doctype html><html><body><h1>404 Not Found<h1></body></html>"
            response = "HTTP/1.1 404 Not Found\r\nContent-Length:" + str(
                len(outputdata)) + "Content-Type: text/html\r\n\r\n" + responseContent
            self.connectionSocket.send(response.encode())

            self.connectionSocket.close()





serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',6789))
serverSocket.listen(10)
print("Main thread is running and listening")
while True:
    print("ready to serve")
    connectionSocket, addr = serverSocket.accept()
    newthread = clientThread(connectionSocket)

    threads.append(newthread)
    newthread.start()

for each in threads:
    each.join()

serverSocket.close()