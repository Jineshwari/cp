import socket
import threading
import time
import random

# Network settings
HOST = "127.0.0.1"
PORT = 12345
WINDOW_SIZE = 4  # Sliding window size
TOTAL_FRAMES = 10  # Total number of frames to send

# Sender variables
base = 0  # First frame in window
next_seq_num = 0  # Next frame to send

# Receiver variables
expected_frame = 0  # Expected frame to be received

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

def receiver():
    global expected_frame
    print("[Receiver] Listening for frames...")

    while expected_frame < TOTAL_FRAMES:
        data, addr = sock.recvfrom(1024)
        frame = int(data.decode())

        # Simulate ACK loss (20% chance)
        if random.random() < 0.2:
            print(f"[Receiver] Frame {frame} received, but ACK lost!")
            continue

        if frame == expected_frame:
            print(f"[Receiver] Frame {frame} received, sending ACK {frame}")
            sock.sendto(str(frame).encode(), addr)
            expected_frame += 1  # Move to next expected frame
        else:
            print(f"[Receiver] Out-of-order frame {frame} received, discarding!")

def sender():
    global base, next_seq_num
    sock.settimeout(2)  # Set timeout for ACKs

    print("[Sender] Starting transmission...")

    while base < TOTAL_FRAMES:
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"[Sender] Sending frame {next_seq_num}")
            sock.sendto(str(next_seq_num).encode(), (HOST, PORT))
            next_seq_num += 1

        try:
            ack, _ = sock.recvfrom(1024)
            ack = int(ack.decode())
            print(f"[Sender] ACK {ack} received")

            if ack >= base:
                base = ack + 1  # Slide window forward

        except socket.timeout:
            print(f"[Sender] Timeout! Resending from frame {base}")
            next_seq_num = base  # Restart from base

    print("[Sender] Transmission complete!")

# Start both sender and receiver as separate threads
threading.Thread(target=receiver, daemon=True).start()
threading.Thread(target=sender).start()
