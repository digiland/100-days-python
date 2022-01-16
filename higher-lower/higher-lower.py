from art import logo, vs
import random
from game_data import data

print(logo)

a = random.choice(data)
b = random.choice(data)
data.remove(a)
data.remove(b)

score = 0


# clear console
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(a, b, score):
    print(f"Compare A; {a['name']}, a {a['description']} from {a['country']}")
    print(f"Compare B; {b['name']}, a {b['description']} from {b['country']}")
    choice = input("Choose A or B:").lower()
    if choice == "a" and a['follower_count'] > b['follower_count']:
        print("A wins!")
        score += 1
        print(f"Score: {score}")
        a = b
        b = random.choice(data)
        data.remove(b)
        clear()
        compare(a, b, score)
    elif choice == "b" and b['follower_count'] > a['follower_count']:
        print("B wins!")
        score += 1
        print(f"Score: {score}")
        a = b
        b = random.choice(data)
        data.remove(b)
        clear()
        compare(a, b, score)
    else:

        print(f"Game over your score is {score}")


compare(a, b, score)
