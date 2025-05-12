import socket

c = socket.socket()

try:
    c.connect(('localhost', 9999))
    name = input("Enter Your name: ")
    c.send(bytes(name, 'utf-8'))

    print("Server Response:", c.recv(1024).decode())

except Exception as e:
    print("Error:", e)

finally:
    c.close()
