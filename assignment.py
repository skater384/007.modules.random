#! python3

# SD Computing Studies Assignment
import random
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
            if x == 0:
                print("Opponent chose Rock, you Tied")
            elif x == 1:
                print("Opponent chose Paper, you Lose")
            elif x == 2:
                print("Opponent chose Scissors, you Win")
            break
        if q == "Paper":
            if x == 0:
                print("Opponent chose Rock, you Win")
            elif x == 1:
                print("Opponent chose Paper, you Tied")
            elif x == 2:
                print("Opponent chose Scissors, you Lose")
            break
        if q == "Scissors":
            if x == 0:
                print("Opponent chose Rock, you Lose")
            elif x == 1:
                print("Opponent chose Paper, you Win")
            elif x == 2:
                print("Opponent chose Scissors, you Tied")
            break


def DnD():
    print("DnD Character Stat Chart")
    lis = ["strength", "intelligence", "wisdom",
           "dexterity", "constitution", "charisma"]
    for i in lis:
        x = randint(1, 6)
        y = randint(1, 6)
        z = randint(1, 6)
        print(f"{i} is {x+y+z}")


def DnD2():
    q = input("Would you like to roll 4 dice and discard lowest, or roll 3 and reroll any 1's?\n1 = 4 dice\n2 = 3 dice\n")
    print("DnD Character Stat Chart")
    lis = ["strength", "intelligence", "wisdom",
           "dexterity", "constitution", "charisma"]
    if q == "1":
        for i in lis:
            x = randint(1, 6)
            y = randint(1, 6)
            z = randint(1, 6)
            c = randint(1, 6)
            print(f"{i} is {(x+y+z+c)-min(x,y,z,c)}")

    elif q == "2":
        for i in lis:
            x = randint(1, 6)
            y = randint(1, 6)
            z = randint(1, 6)
            while x == 1 or y == 1 or z == 1:
                x = randint(1, 6)
                y = randint(1, 6)
                z = randint(1, 6)
            print(f"{i} is {(x+y+z)}")


def Dealer():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']
    deck = []
    for i in ranks:
        for j in suits:
            deck.append(i+j)
    random.shuffle(deck)
    p1 = []
    p2 = []
    p1.append(deck[0:5])
    p2.append(deck[5:10])
    del deck[0:10]
    print(f"player 1's Hand is {p1}, and player 2's Hand is {p2}")
