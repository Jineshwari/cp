import socket

# Server configurations
SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Receive greeting
greeting = client_socket.recv(1024).decode('utf-8')
print(f"Server: {greeting}")

# File reception
file_name = "received_file.txt"
with open(file_name, "wb") as f:
    while True:
        data = client_socket.recv(1024)
        if b"<END_FILE>" in data:
            # Remove the marker before writing the file
            f.write(data.replace(b"<END_FILE>", b""))
            break
        f.write(data)

print("File received")

# ✅ Move on to the calculator
print("\n💡 Calculator (Type 'exit' to quit)")

while True:
    expression = input("Enter arithmetic expression (or 'exit' to quit): ")

    client_socket.send(expression.encode('utf-8'))

    if expression.lower() == "exit":
        break

    result = client_socket.recv(1024).decode('utf-8')
    print(f"Result: {result}")

client_socket.close()
