import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
s.bind((ipAddress, 9999))


data, addr = s.recvfrom(4096)
print(data)
msg = "Hai from server"
s.sendto(msg.encode("utf-8"), addr)

s.close()