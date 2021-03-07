# multi threaded server 
import socket
from _thread import *

hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
port = 9999
threadCount = 0
s = socket.socket()
s.bind((ipAddress, port))
print("Connection is established...")
s.listen(9)

def clientThread(conn):
    conn.send(str("Hey, Thread is processing..."))
    while True:
        data= conn.recv(1024)
        if not data:
            break
        print(data)
        msg =bytes("Dude, How is it going").encode("UTF-8")
        conn.send(msg)
        
    conn.close
    
while True:
    conn, add = s.accept()
    start_new_thread(clientThread, (conn, ))
    threadCount += 1
    
s.close()
    
    
    
    
