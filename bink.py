import random
import time
import os


def generate_health_stat():
    six_sides = random.randint(1, 6)
    twelve_sides = random.randint(1, 12)
    pick = six_sides * twelve_sides // 2
    final_stat = pick + 10
    return f'Health: {final_stat}'


def generate_strength_stat():
    six_sides = random.randint(1, 6)
    twelve_sides = random.randint(1, 12)
    pick = six_sides * twelve_sides // 2
    final_stat = pick + 12
    return f'Strength: {final_stat}'


def generate_character(player_number):
    character_input = input(f"Name your legend as Player{player_number}: ")
    character_type = input("Character type: (Human, Elf, Wizard, Orc): ")

    if character_type.lower() in ['human', 'elf', 'wizard', 'orc']:
        health = generate_health_stat()
        strength = generate_strength_stat()

        print(f"Player {player_number}")
        print(character_input)
        print(f"Character Type: {character_type}")
        print(health)
        print(strength)

        return character_input, character_type
    else:
        print("Invalid character type. Please choose from (Human, Elf, Wizard, Orc).")
        return None, None


def battle(player1_name, player2_name):
    player1_score = 0
    player2_score = 0

    for _ in range(3):
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)

        print(f'{player1_name} rolls: {player1_roll}')
        print(f'{player2_name} rolls: {player2_roll}')

        if player1_roll > player2_roll:
            player1_score += 1
            print(f'{player1_name} wins this round!\n')
        elif player1_roll < player2_roll:
            player2_score += 1
            print(f'{player2_name} wins this round!\n')
        else:
            print("It's a draw!\n")

    if player1_score > player2_score:
        print(f'{player1_name} wins the game with {player1_score} rounds!')
    elif player1_score < player2_score:
        print(f'{player2_name} wins the game with {player2_score} rounds!')
    else:
        print("The game ends in a draw!")


if __name__ == "__main__":
    player1_name, player1_type = generate_character(1)
    player2_name, player2_type = generate_character(2)

    if player1_name and player2_name:
        battle(player1_name, player2_name)

    time.sleep(45)

    os.system('cls' if os.name == 'nt' else 'clear')
