# -*-coding:Utf-8 -*

import socket

from threading import Thread

host = "localhost"
port = 42000
serverConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverConnection.connect((host, port))

print("Connection established on port {}".format(port))


def listen():
    """Code à exécuter pendant l'exécution du thread."""
    while True:
        receivedMessage = serverConnection.recv(1024)
        print(receivedMessage.decode())

listener = Thread(target=listen)
listener.start()

messageToSend = b""
while messageToSend != b"fin":
    messageToSend = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    messageToSend = messageToSend.encode()
    # On envoie le message
    serverConnection.send(messageToSend)

print("Connection closed")
serverConnection.close()