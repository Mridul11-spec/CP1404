import random
picks = int(input("How many quick picks "))

for i in range(0, picks):
    for picks in range(6):
        print(random.randint(1, 45), end=" ")
    print("")
