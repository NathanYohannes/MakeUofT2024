import socket as soc
s = soc.socket()
host = soc.gethostname()
port = 8080
#s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
s.connect(("192.168.159.8", port))
s.listen(1)
c,addr = s.accept()
while True:
    print(c.recv(2048).decode('ascii'))