# -*-coding:Utf-8 -*

"""Ce fichier contient le code du serveur de jeu.

Exécutez-le avec Python pour lancer le serveur

"""

from serverFunctions import *
import socket
import select


host = ''
port = 42000
# statut de la partie :
#  - WAITING tant que les joueurs se connectent
#  - PLAYING pendant toute la durée de la partie
#  - FINISHED quand la partie est terminée
gameStatus = "WAITING"
playerNumber = 0


# On charge les maps existantes
maps = loadMaps()

# On propose de choisir une carte
map = chooseMap(maps)

print("Waiting for players...")

# On établit la connexion
mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainConnection.bind((host, port))
mainConnection.listen(5)
print("Server listening on port {}".format(port))

players = []
# Boucle principale du jeu, qui tourne jusqu'à ce que la partie finisse
while gameStatus != "FINISHED":
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    askToPlay, wlist, xlist = select.select([mainConnection], [], [], 0.05)

    if gameStatus == "WAITING":

        for connection in askToPlay:
                playerConnection, info = connection.accept()
                playerNumber = playerNumber + 1
                message = ("Welcome, you are player" + str(playerNumber)).encode()
                playerConnection.send(message)
                print("Player {} is connected !".format(playerNumber))
                # On ajoute le socket connecté à la liste des clients
                players.append(playerConnection)
    else:
        print("Connection refused, the game already started")
        connection.close()

    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    playersToRead = []
    try:
        playersToRead, wlist, xlist = select.select(players, [], [], 0.05)
    except select.error:
        pass
    else:
        for player in playersToRead:
            # Client est de type socket
            receivedMessage = player.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            receivedMessage = receivedMessage.decode()
            print("Reçu {}".format(receivedMessage))
            player.send(b"5 / 5")
            if receivedMessage == "fin":
                gameStatus = "FINISHED"
            elif receivedMessage.lower() == "c":
                gameStatus = "PLAYING"

print("Closing connections")
for player in players:
    player.close()
mainConnection.close()
