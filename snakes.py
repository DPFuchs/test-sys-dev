import random

position = 0
snakes = [11,21,66, 78]
sp = [7, 3, 23, 12]
ladders = [3, 32, 50, 65]
lp = [5, 10, 20, 10]
i = 0
while True:
    d = input("Press D to roll a dice!: ")
    if d.lower() == "d":
        i += 1
        dice = random.randrange(1,7)
        print(f"You rolled a {dice}")
        if position + dice < 100:
            position += dice
        if position + dice == 100:
            print("You win!!!!")
            print(f"You had to roll {i} times")
            break
        for x in range(4):
            if snakes [x] == position:
                position -= sp[x]
                print("You were bitten")
            if ladders[x] == position:
                position += lp[x]
                print("You climbed!")
        print(f"You are at {position}")
    else:
        print("Enter valid input")