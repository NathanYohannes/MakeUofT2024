import socket as soc
import os
s = soc.socket()
host = '0.0.0.0'
port = 12345
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
s.bind(('',port))
s.listen(1)
c,addr = s.accept()
while True:
    print(c.recv(2048).decode('ascii'))