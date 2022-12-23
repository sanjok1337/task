# Client code
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





HOST = 'localhost'
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter a message to send to the server (enter 'e' to encrypt): ")
    if message[0] == "e":
        message = message[1:]
        message = caesar_encrypt(message, 3)
    client_socket.sendall(message.encode())
    message = client_socket.recv(1024).decode()
    if message == "":
        break
    elif message[0] == "e":
        message = message[1:]
        message = caesar_decrypt(message, 3)
    print(f"Received from server: {message}")

client_socket.close()