import socket

host = socket.gethostname()   # get local machine name
port = 12345  # Make sure it's within the > 1024 $$ <65535 range

s = socket.socket()
s.bind(("192.168.159.8", port))

s.listen(1)
client_socket, adress = s.accept()
print("Connection from: " + str(addr))
while True:
    data = c.recv(1024).decode('utf-8')
    if not data:
        break
    print('From online user: ' + data)
    data = data.upper()
    c.send(data.encode('utf-8'))
    c.close()
