def xor(dividend, divisor):
    """Perform XOR operation between dividend and divisor in binary division."""
    return [dividend[i] ^ divisor[i] for i in range(len(divisor))]

def crc_encode(frame, generator):
    """Encodes the frame by appending CRC bits using the generator polynomial."""
    fs, gs = len(frame), len(generator)
    extended_frame = frame + [0] * (gs - 1)  # Append zeros

    # Perform binary division
    temp = extended_frame[:]
    for i in range(fs):
        if temp[i] == 1:
            temp[i:i+gs] = xor(temp[i:i+gs], generator)

    crc_bits = temp[-(gs - 1):]  # Extract CRC
    transmitted_frame = frame + crc_bits
    return transmitted_frame, crc_bits

def crc_check(received_frame, generator):
    """Checks if received frame has errors using CRC verification."""
    fs, gs = len(received_frame) - (len(generator) - 1), len(generator)
    
    # Perform binary division
    temp = received_frame[:]
    for i in range(fs):
        if temp[i] == 1:
            temp[i:i+gs] = xor(temp[i:i+gs], generator)

    remainder = temp[-(gs - 1):]  # Extract remainder
    return remainder

def main():
    # Input Frame and Generator
    frame = list(map(int, input("\nEnter Frame (binary, space-separated): ").split()))
    generator = list(map(int, input("\nEnter Generator Polynomial (binary, space-separated): ").split()))

    # Encoding
    transmitted_frame, crc_bits = crc_encode(frame, generator)
    print("\nSender Side:")
    print("Original Frame: ", frame)
    print("Generator Polynomial: ", generator)
    print("CRC Bits: ", crc_bits)
    print("Transmitted Frame: ", transmitted_frame)

    # Simulating Receiver Side
    print("\nReceiver Side:")
    received_frame = transmitted_frame[:]  # Assume no transmission errors
    print("Received Frame: ", received_frame)

    remainder = crc_check(received_frame, generator)
    print("Remainder after CRC Check: ", remainder)

    # Check for errors
    if all(bit == 0 for bit in remainder):
        print("\n✅ Message received correctly, no errors detected.")
    else:
        print("\n❌ Error detected in the received message.")

if __name__ == "__main__":
    main()
