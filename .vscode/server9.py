import socket
import threading

# Server configurations
HOST = '127.0.0.1'
PORT = 1234

# Handle client communication
def handle_client(client_socket):
    try:
        # Send greeting
        client_socket.send(b"Server: Hello!")
        print("Server: Hello sent")

        # File transfer
        file_name = "server_file.txt"

        # Create a sample file
        with open(file_name, "wb") as f:
            f.write(b"This is a sample file content.")  

        # Send the file
        with open(file_name, "rb") as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)

        # Send marker to indicate the end of file transfer
        client_socket.send(b"<END_FILE>")  
        print("File sent")

        # Calculator
        while True:
            expression = client_socket.recv(1024).decode('utf-8')

            if expression.lower() == "exit":
                print("Client disconnected.")
                break

            try:
                result = str(eval(expression))
            except Exception as e:
                result = f"Error: {str(e)}"

            client_socket.send(result.encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# Start server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server started. Waiting for clients...")

while True:
    client, addr = server_socket.accept()
    print(f"Client connected: {addr}")
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
