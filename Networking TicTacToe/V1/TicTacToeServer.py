import socket
from _thread import *
import sys
import pickle
from game import Game

server = "XXX.XXX.XXX.XXX"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

g = Game()

def threaded_client(conn):
    global g
    conn.send(str.encode("Connected"))
    while True:
        try:
            data = conn.recv(4096).decode()
            if not data:
                print("Disconnected")
                break
            else:
                if data == "reset":
                    g.resetGame()
                elif data != "get":
                    data = convertStringToCoords(data)
                    g.update(int(data[0]),int(data[1]))
                conn.sendall(pickle.dumps(g))
        except socket.error as e:
            print(e) 
            break
    print("Lost connection")
    conn.close()

def convertStringToCoords(strin):
    strin = strin.split(",")
    return strin

while True:
    conn, addr = s.accept()
    print("Connected: ", addr)
    start_new_thread(threaded_client,(conn,))