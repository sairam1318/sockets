import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)


msg = "From client "
c.sendto(msg.encode("UTF-8"), (ipAddress, 9999))
data, add = c.recvfrom(4096)
print(str(data))

c.close()