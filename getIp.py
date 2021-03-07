
import socket

s = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
print(ip)
