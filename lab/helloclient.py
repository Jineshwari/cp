import socket

c = socket.socket()
c.connect(('localhost', 12345))

print(" Server Connected.........")

c.send("Hello Server...........".encode())

reply = c.recv(1024).decode()
print("Server Says : ", reply)



c.close()
