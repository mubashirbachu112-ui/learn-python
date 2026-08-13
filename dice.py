import random
while True:
    Dice = int(input("How many dice to roll or :"))
    total = 0
    for i in range(Dice):
        roll = random.randint(1,6)
        print(f"dice says:{roll}")
        total = total + roll
        print(f"total score:{total}")
        

