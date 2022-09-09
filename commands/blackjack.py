import random
import time
from utility.dataBridge import *
from utility.clearConsole import clearConsole
from commands.loadAnimation import loadAnimation
from commands.viewBalance import viewBalance
from commands.setBalance import setBalance
from utility.balHandler import balHandler
from utility.exitProgram import exitProgram

deck = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
faces = ["Jack", "Queen", "King"]
nums = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]
only_cards = []
full_cards = []
player_cards = []
dealer_cards = []
stand = False
divider = "---------------"

# https://slideplayer.com/slide/4549771/15/images/11/Main+Activity+Diagram.jpg
# https://svg.template.creately.com/i541ys2v2

# https://www.blackjacksimulator.net/


def dealCards(amount):
    only_cards.clear()
    full_cards.clear()
    for _ in range(amount):
        rand_card = random.choice(deck)
        rand_suit = random.choice(suits)
        only_cards.append(rand_card)
        full_cards.append(f"{rand_card} {rand_suit}")
    return full_cards, only_cards


def calculateCards(full_cards, only_cards, Type):
    total = 0
    for face in faces:  # Check for Blackjack.
        if face in only_cards and "Ace" in only_cards:  # If face and ace is present...
            return "Blackjack!"  # Get a Blackjack!

    for card in only_cards:  # For card in hands
        if card in faces:  # If card is a face...
            total += 10  # Add 10 to the total.
        if card == "Ace":  # Process ace...
            if total + 11 > 21:  # If total greater than 21...
                total += 1  # Ace counts as 1...
            else:
                total += 11  # Ace counts as 11.
        if card in nums:
            total += int(card)
    if total > 21:
        return "Bust!"

    for i in full_cards:
        if Type == "Player":
            player_cards.append(i)
        else:
            dealer_cards.append(i)

    return total


def firstCycle():
    player = calculateCards(*dealCards(2), "Player")
    dealer = calculateCards(*dealCards(1), "Dealer")

    if player == 21:
        return True
    if dealer == 21:
        return False

    return player, dealer


def mainCycle(hitOrStand, Player, Dealer):
    global stand
    if hitOrStand[0] == "h":
        Player += calculateCards(*dealCards(1), "Player")
        return Player, "Player"
    else:
        stand = True
        Dealer += calculateCards(*dealCards(1), "Dealer")
        if Dealer < 17:
            Dealer += calculateCards(*dealCards(1), "Dealer")
        return Dealer, "Dealer"


def winHandler(Player, Dealer, betAmount):
    if stand:
        if Dealer < Player:
            print(f"You won {betAmount}!")
            balHandler(False, betAmount)
        if Player < Dealer:
            print(f"The Dealer won!")
            balHandler(True, betAmount)
        if Player == Dealer:
            print(f"You tied with the Dealer!")
        return True

    if Dealer == 21:
        print("Dealer has hit a Blackjack!")

    if Player == 21:
        print(f"You hit a Blackjack and won {betAmount}!")

    if Dealer > 21:
        print(f"The Dealer bust and you won {betAmount}!")

    if Player > 21:
        print("You bust!")

    if Player > 21 or Dealer == 21:  # Loss condition
        balHandler(True, betAmount)
        return True
    if Dealer > 21 or Player == 21:  # Win condition
        balHandler(False, betAmount)
        return True


def betHandler():
    bal = viewBalance(True)
    x = inputWrapper("Do you want to bet? >").lower()
    if x[0] == "y":
        betAmount = int(inputWrapper("Enter bet amount >"))
        if betAmount > bal:
            clearConsole()
            print("Bet amount exceeds balance.")
            return True, betAmount
    else:
        betAmount = 0
    return False, betAmount


def resetVars():
    global stand
    only_cards.clear()
    full_cards.clear()
    player_cards.clear()
    dealer_cards.clear()
    stand = False


def againHandler():
    x = inputWrapper("Do you want to play again? >").lower()
    if x[0] == "y":
        clearConsole()
        resetVars()
        blackjack()
    else:
        time.sleep(TIMEOUT)


def inputWrapper(Text):
    try:
        return input(Text)
    except KeyboardInterrupt:
        exitProgram()


def blackjack():
    x, bet_amount = betHandler()

    if x:
        againHandler()
        return

    loadAnimation()
    clearConsole()
    player, dealer = firstCycle()  # Deal the first 3 cards.

    while True:  # Main gameLoop
        if winHandler(player, dealer, bet_amount):
            time.sleep(TIMEOUT)
            break

        print(f"Your deck: {player_cards}\nDealer's deck: {dealer_cards}")
        print(f"Your total: {player}\nDealer total: {dealer}")
        print(divider)

        (total, type) = mainCycle(
            inputWrapper("Hit or Stand? >").lower(), player, dealer
        )

        if type == "Player":
            player = total
        else:
            dealer = total

        loadAnimation()
        clearConsole()

        time.sleep(TIMEOUT)

    againHandler()
