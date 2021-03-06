# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:07:35 2021

@author: DELL
"""

import socket

s = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
print(ip)
