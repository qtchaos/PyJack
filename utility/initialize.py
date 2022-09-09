from utility.inputHandler import inputHandler


def initialize():
    inputHandler("What is your name?", Save=True, fileName="name")
    inputHandler("Input your starting balance.", Save=True, fileName="balance")
