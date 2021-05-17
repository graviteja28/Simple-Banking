import random

account = {}


def main():
    while 1:
        n = int(input("1. create an account\n" + "2. Log into account\n" + "0. Exit\n"))
        if n == 1:
            createaccount()
        elif n == 2:
            r = logintoaccount()
            if r == 2:
                break
        elif n == 0:
            print("Bye!")
            break


def createaccount():
    inputpin = random.randint(1000, 10000)
    # x=random.choice([400000,340000,370000,510000,550000])
    y = random.randint(10 ** 9, 10 ** 10)
    cardnumber = str(400000) + str(y)
    print("Your card has been created")
    print("Your card number")
    print(cardnumber)
    print("Your card pin")
    print(inputpin)
    account[cardnumber] = inputpin


def logintoaccount():
    x1 = 1
    while x1 != 0:
        cardnumber = input("Enter your card number:")
        pin = int(input("Enter your PIN"))
        if len(cardnumber) == 16:
            if (cardnumber in account) and account[cardnumber] == pin:
                print("You successfully logged in!")
                while 1:
                    print("1. Balance\n" + "2. Log out\n" + "0. Exit\n")
                    n1 = int(input())
                    if n1 == 1:
                        print("Balance: 0")
                        return 0
                    elif n1 == 2:
                        print("You have successfully logged out!")
                        return 0
                    elif n1 == 0:
                        print("Bye!")
                        return 2
            else:
                print("Wrong card number or PIN!")
                return 0
        else:
            print("Wrong card number or PIN!")
            return 0


main()
