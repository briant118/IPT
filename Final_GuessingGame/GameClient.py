import socket
import json

HOST = "localhost"
PORT = 7777

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # User name
    user_name = input("Enter Name: ").strip()
    s.sendall(user_name.encode())

    # Header
    data = s.recv(1024)
    print(data.decode().strip())

    # User chose level
    user_level = input("Enter Level: ").strip()
    s.sendall(user_level.encode())

    tries = 0
    while True:
        user_guess = input("Enter Guess: ").strip()
        s.sendall(user_guess.encode())
        reply = s.recv(1024).decode().strip()
        tries += 1
        if "Correct" in reply:
            print(reply)
            break
        print(reply)

    # Saving data
    data_to_save = {
        "name": user_name,
        "level": user_level,
        "tries": tries
    }

    with open("game_data.json", "a") as file:
        json.dump(data_to_save, file)
        file.write('\n')

    with open("game_data.json", "r") as file:
        for line in file:
            data = json.loads(line)
            print("Name:", data["name"])
            print("Difficulty:", data["level"])
            print("Tries:", data["tries"])

    s.close()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
