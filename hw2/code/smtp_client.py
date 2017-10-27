from socket import *

msg= "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"


#connection
mailserver = "localhost"

clientsocket = socket(AF_INET,SOCK_STREAM)

clientsocket.connect((mailserver,25))

recv = clientsocket.recv(1024).decode()

print(recv)

if recv[:3] != '220':
	
	print('220 reply not received from server.')


#helo
heloCommand = 'HELO crystalcove.com\r\n'

clientsocket.send(heloCommand.encode())

recv1 = clientsocket.recv(1024).decode()

print(recv1)

if recv1[:3] != '250':

	print('250 reply not received from server.')



#MAIL FROM
while True:
	mail_addr = input("Email: ")

	mail_addr_command_version = '<' + mail_addr + '>'

	mailfromCommand = 'MAIL FROM: ' + mail_addr_command_version  +'\r\n'

	clientsocket.send(mailfromCommand.encode())

	recv2 = clientsocket.recv(1024).decode()

	print(recv2)

	if recv2[:3] != '250':

		print('invalid mail address')
		
		continue
	break	



#RCPT TO
while True:
	mail_addr = input('Recipient Email: ')

	mail_addr_command_version = '<' + mail_addr + '>'

	rcpttoCommand = 'RCPT TO: ' + mail_addr_command_version  +'\r\n'

	clientsocket.send(rcpttoCommand.encode())

	recv3 = clientsocket.recv(1024).decode()

	print(recv3)

	if recv3[:3] != '250':

		print('invalid mail address')

		continue
	break


#DATA

dataCommand = 'DATA\r\n'

clientsocket.send(dataCommand.encode())

recv4 = clientsocket.recv(1024).decode()

print(recv4)


#Send message

clientsocket.send(msg.encode())

clientsocket.send(endmsg.encode())

	
#QUIT
quitCommand = 'QUIT\r\n'
	
clientsocket.send(quitCommand.encode())

recvq = clientsocket.recv(1024).decode()

print(recvq)

clientsocket.close()
