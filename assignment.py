#! python3

# SD Computing Studies Assignment

from random import randint


def numGuess():
    x = randint(1, 100)
    y = 0
    z = 0
    while y != x:
        z += 1
        y = int(input("Enter a number from 1 to 100: "))
        if y < x:
            print("The number is higher")
        elif y > x:
            print("The number is lower")
        elif y == x:
            print(f"That is the number, you had a total of {z} guesses")
            break


def coinToss():
    x = randint(0, 1)
    q = input("Heads or Tails? ").strip()
    if x == 1 and q == "Heads":
        print("Heads, you were correct")
    elif x == 1 and q == "Tails":
        print("Heads, you were incorrect")
    elif x == 0 and q == "Tails":
        print("Tails, you were correct")
    elif x == 0 and q == "Heads":
        print("Tails, you were incorrect")


def RPS():
    q = ""
    x = randint(0, 2)
    while q != "Rock" or q != "Paper" or q != "Scissors":
        q = input("Rock, Paper, or Scissors? ").strip()
        if q == "Rock": 
            if x == 0: print("Opponent chose Rock, you Tied")
            elif x == 1: print("Opponent chose Paper, you Lose")
            elif x == 2: print("Opponent chose Scissors, you Win")
            break
        if q == "Paper": 
            if x == 0: print("Opponent chose Rock, you Win")
            elif x == 1: print("Opponent chose Paper, you Tied")
            elif x == 2: print("Opponent chose Scissors, you Lose")
            break
        if q == "Scissors": 
            if x == 0: print("Opponent chose Rock, you Lose")
            elif x == 1: print("Opponent chose Paper, you Win")
            elif x == 2: print("Opponent chose Scissors, you Tied")
            break


def DnD():
    x = randint(3,18)