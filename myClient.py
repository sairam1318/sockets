import socket

cc = socket.socket()

cc.connect(('DESKTOP-5TG645N', 11111))

print(cc.recv(1024).decode())

cc.close()