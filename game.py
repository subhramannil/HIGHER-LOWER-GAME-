from art import logo,vs
print(logo)

import random
from game_data import data

a = []
a = random.choice(data)

b = []
b = random.choice(data)

score = 0
first_comp_called = False


def checkin():
    global score
    check = input("Who has more followers? Type 'A' or 'B': ")
    if a['follower_count'] > b['follower_count']:
        if check == 'A':
            score += 1
            print(f"You are right. your current score {score}")
            print("\n" * 100)
            return True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            return False

    if a['follower_count'] < b['follower_count']:
        if check == 'B':
            score += 1
            print("\n" * 100)
            return True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            return False


def first_comp():
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    return checkin()


def sec_comp():
    global a, b
    a = b
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(f"You are right. your current score {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    return checkin()


Game_active = True
while Game_active:
    if a == b:
        while a == b:
            b = random.choice(data)

    if not first_comp_called:
        first_comp_called = True
        if first_comp() == False:
            Game_active = False
    else:
        if sec_comp() == False:
            Game_active = False

