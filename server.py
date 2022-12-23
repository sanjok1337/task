import socket

def caesar_encrypt(plaintext, shift):
    """
    Encrypts the given plaintext using a Caesar cipher with the given shift.
    """
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shift_ch
        else:
            ciphertext += ch
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using a Caesar cipher with the given shift.
    """
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            plaintext += shift_ch
        else:
            plaintext += ch
    return plaintext

# Server code

HOST = 'localhost'
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Waiting for a client to connect...")
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

while True:
    message = client_socket.recv(1024).decode()
    if message == "":
        break
    elif message[0] == "e":
        message = message[1:]
        message = caesar_decrypt(message, 3)
    print(f"Received from client: {message}")
    message = input("Enter a message to send to the client (enter 'e' to encrypt): ")
    if message[0] == "e":
        message = message[1:]
        message = caesar_encrypt(message, 3)
    client_socket.sendall(message.encode())

client_socket.close()
server_socket.close()