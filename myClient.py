# basic client program to interact with Server
import socket

cc = socket.socket()
host = '165.22.14.77'
port = 9999
cc.connect((host, port))

print(cc.recv(1024).decode())

cc.close()