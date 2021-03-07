# Normal socket program to connect to websites
import socket

s = socket.socket()

hostName = input("Enter host name: ")
portNo = int(input("Enter port Num: "))
try:
    s.connect((hostName, portNo))

    print("Connected successfullly.")
except Exception as e:
    print(e)

"""Tried with hostName = www.python.org, and port no as 80 """