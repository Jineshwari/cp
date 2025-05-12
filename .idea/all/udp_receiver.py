import socket
import os

# 🔹 Receiver IP and Port (Listen for incoming files)
RECEIVER_IP = "0.0.0.0"  # Listen on all network interfaces
RECEIVER_PORT = 5005

# 🔹 UDP Config
CHUNK_SIZE = 1024  # 1KB chunk size

def receive_file():
    """Receive a file over UDP and save it."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((RECEIVER_IP, RECEIVER_PORT))
    print(f"📥 Listening for incoming files on {RECEIVER_IP}:{RECEIVER_PORT}...")

    # Receive file metadata
    data, sender_addr = sock.recvfrom(1024)
    filename, file_size = data.decode().split("|")
    file_size = int(file_size)

    # Create the received file
    save_path = os.path.join(os.getcwd(), filename)
    with open(save_path, "wb") as f:
        bytes_received = 0

        while bytes_received < file_size:
            chunk, sender_addr = sock.recvfrom(CHUNK_SIZE)
            f.write(chunk)
            bytes_received += len(chunk)

            # Send ACK to sender
            sock.sendto("ACK".encode(), sender_addr)

    print(f"✅ File '{filename}' received successfully and saved as '{save_path}'.")
    sock.close()

if __name__ == "__main__":
    receive_file()
