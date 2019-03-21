# -*-coding:Utf-8 -*

import socket

host = "localhost"
port = 42000
serverConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverConnexion.connect((host, port))

print "Connection established on port {}".format(port)

messageToSend = b""
while messageToSend != b"fin":
    messageToSend = raw_input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    messageToSend = messageToSend.encode()
    # On envoie le message
    serverConnexion.send(messageToSend)
    receivedMessage = serverConnexion.recv(1024)
    print(receivedMessage.decode()) # Là encore, peut planter s'il y a des accents

print "Connection closed"
serverConnexion.close()