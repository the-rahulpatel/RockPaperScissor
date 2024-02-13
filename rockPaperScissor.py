import random

TOTAL = 0
def game_commands():
    print('Here are the game commands\n-->Press y to Play\n-->Press q to Quit,\n-->Press r for Rock,\n-->Press p for Paper,\n-->Press s for Scissor')



def check_valid(user_input):
    if user_input.lower() in ['r', 'p', 's']:
        return True
    return False

def computer_move():
    return random.choice(['Rock','Paper','Scissor'])

def user_move(user_input):
    if user_input == 'r':
        return "Rock"
    elif user_input == 's':
        return 'Scissor'
    else:
        return 'Paper'

def count_noter(a):
    global TOTAL
    TOTAL += a
    return None

def evaluate(u,c):
    if u != c:
        if u == 'Rock':
            if c == 'Paper':
                count_noter(-1)
                return "Paper beats Rock"
            else:
                count_noter(1)
                return "Rock beats Scissor"
        elif u == 'Paper':
            if c == 'Rock':
                count_noter(1)
                return "Paper beats Rock"
            else:
                count_noter(-1)
                return "Scissor beats Paper"
        elif u == 'Scissor':
            if c == 'Rock':
                count_noter(-1)
                return "Rock beats Scissor"
            else:
                count_noter(1)
                return "Scissor beats Paper"
    else:
        count_noter(0.5)
        return 'draw'
        
def game():
    while True:
        try:
            tries = int(input("How many tries would you like to choose? "))
        except:
            print('retry')
            continue
        break

    current = 0
    while current != tries:
        user_input = input("Enter your move: ")
        if check_valid(user_input):
            u = user_move(user_input)
            print(f"Your move: {u}")
            c = computer_move()
            print(f"AI's move {c}")
            evaluate(u,c)
        else:
            print("Invalid input")
        current += 1
    
    if TOTAL != 0:
        if TOTAL > 0:
            if TOTAL > tries/2:
                print('You won')
            else:
                print("You lost")
        else:
            print('You lost')

    else:
        print('draw')

def reset_total():
    global TOTAL
    TOTAL = 0
    return None
def restart():
    a = input("type w to restart or q to exi ")
    if a.lower() == 'w':
        reset_total()
        game()
    exit()
if __name__ == "__main__":
    a = input("Press 'y' to play the game ")
    if a.lower() != 'q':
        if a.lower() == 'y':
            game_commands()
            game()
            restart()
    else:
        exit()




