"""Client creation using Socket API"""
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
c.connect((ipAddress, 9999))
c.send(b"Hai connection")
    
c.close()
