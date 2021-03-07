import socket

sc = socket.socket()

host = '165.22.14.77'
port = 9999

sc.bind((host, port))

sc.listen(2)

while True:
	cc, addr = sc.accept()
	print("Connection established")

	cc.send(bytes("Dude congratulations", "utf-8"))

	cc.close()