import pickle
import random
import socket
import sys
from _thread import *

from game import Game

server = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

games = {}
james = []
p = 1
playerCount = 0

def threaded_client(conn, gameId, p, addr):
    global playerCount
    global game
    conn.send(str.encode(str(p)))
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]

                if not data:
                    print(addr[0] + " disconnected")
                    break
                else:
                    if data == "reset":
                        game.resetGame()
                    elif data != "get":
                        data = convertStringToCoords(data)
                        game.update(int(data[0]),int(data[1]))
                    conn.sendall(pickle.dumps(game))
        except socket.error as e:
            print(e) 
            break
    playerCount -= 1
    game.ready = False
    game.resetGame()
    conn.sendall(pickle.dumps(game))
    conn.close()

def convertStringToCoords(strin):
    strin = strin.split(",")
    return strin

while True:
    conn, addr = s.accept()
    print(addr[0] + " connected")
    playerCount += 1
    gameId = (playerCount - 1)//2
    if playerCount % 2 == 1:
        p = random.choice([-1, 1])
        games[gameId] = Game(gameId)
        games[gameId].players += 1
        print("Creating a new game...")
    else:
        pass
        games[gameId].ready = True
        p = p * -1

    start_new_thread(threaded_client,(conn, gameId, p, addr))
