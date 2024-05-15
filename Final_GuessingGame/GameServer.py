import socket
import random

HOST = ""
PORT = 7777

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))
SERVER.listen(5)
print(f"Server listening on port {PORT}!")


def generate_random_int(level):
    if level == 'a':
        return random.randint(1, 50)
    elif level == 'b':
        return random.randint(1, 100)
    elif level == 'c':
        return random.randint(1, 1000)
# game score


Starting_game = """
>>>GUESSING GAME<<<
Choose your difficulty level:
a = Low (1-50)
b = Medium (1-100)
c = High (1-1000)
"""

while True:
    socketclient, addr = SERVER.accept()
    print(f"New client connected: {addr[0]}")
    socketclient.sendall(Starting_game.encode())

    User_name = ''
    while not User_name:
        User_name = socketclient.recv(1024).decode().strip()
    print(f"User name: {User_name}")

    User_level = ''
    while not User_level:
        User_level = socketclient.recv(1024).decode().strip()
        print(f"Player chosen level: {User_level} ")

    game_random_number = generate_random_int(User_level)
    randm = game_random_number

    while True:
        User_guess = socketclient.recv(1024)
        guess = int(User_guess.decode().strip())
        print(f'user guess {guess}')

        if guess == randm:
            socketclient.sendall(b"Correct Answer!")
            break
        elif guess > randm:
            socketclient.sendall(b"Lower!")
            continue
        elif guess < randm:
            socketclient.sendall(b"Higher!")
            continue
    socketclient.close()
