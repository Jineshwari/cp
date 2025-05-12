import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Server is listening.......")

conn,addr = s.accept()
print("Server is connected to : ", addr)

msg = conn.recv(1024).decode()
print("Client Says : ", msg)

conn.send("Hello client from server ***".encode())

print("File transfer started...")

with open("ex.txt", 'wb') as f :
    data = conn.recv(1024)
    f.write(data)

print("file Received successfully......")

s.close()