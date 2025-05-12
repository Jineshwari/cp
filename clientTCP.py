import socket

c = socket.socket()
c.connect(('localhost',12345))

c.send(" Hello from cliden".encode())

reply = c.recv(1024).decode()
print("Message form server : ", reply)

with open('file.txt','rb') as f:
    file_data = f.read()
    c.send(file_data)

print("File sent successfully")