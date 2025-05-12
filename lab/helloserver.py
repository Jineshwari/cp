import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Server is listening on port 12345....")

conn,addr = s.accept()
print("connected to : ",addr)


msg = conn.recv(1024).decode()
print("Client Says : ", msg)

conn.send("Hello Client............".encode())

s.close()



