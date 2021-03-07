#Building server using Socket API

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
s.bind((ipAddress, 9999))
s.listen(5)
while True:
    cc, addr = s.accept()
    print("Connection established with ", addr)
    data = cc.recv(1024)
    print(data)
    
s.close()