import random
def pickadiceexperament():
    dice = [1, 2, 3, 4, 5, 6]
    result = random.choice(dice)
    prob = dice.count("6") / len(dice)
    print("Probability of picking a 6 dice is", prob)
    if result == "6":
       print("you got the number 6")
    else:
        print("Better luck next time")
pickadiceexperament()