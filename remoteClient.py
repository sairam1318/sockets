"""For putty """
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAddress = '165.22.14.77'
c.connect((ipAddress, 9999))

c.send(bytes("Hey Remote server..", "utf-8"))
    
data = c.recv(1024)
print(data)
c.close()

