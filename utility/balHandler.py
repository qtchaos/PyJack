from commands.viewBalance import viewBalance
from commands.setBalance import setBalance


def balHandler(Subtract=False, Amount=0):
    if Subtract:
        setBalance(True, viewBalance(True) - Amount)
    else:
        setBalance(True, viewBalance(True) + Amount)
