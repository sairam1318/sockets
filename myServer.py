import socket

sc = socket.socket()

# host = socket.gethostname()

sc.bind(('DESKTOP-5TG645N', 11111))

sc.listen(2)

while True:
	cc, addr = sc.accept()
	print("Connection established")

	cc.send(bytes("Dude congratulations", "utf-8"))

	cc.close()