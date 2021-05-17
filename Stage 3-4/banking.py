import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT UNIQUE, pin TEXT, balance INTEGER DEFAULT 0);")
conn.commit()
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


def luhh(cardnumber):
    l = list(cardnumber)
    s = int(l[-1])
    for i in range(0, 15):
        if i % 2 == 0:
            if int(l[i]) * 2 > 9:
                s = s + (int(l[i]) * 2) - 9
            else:
                s += int(l[i]) * 2
        else:
            s += int(l[i])
    if s % 10 == 0:
        return True
    else:
        return False


def createaccount():
    while True:
        inputpin = random.randint(1000, 10000)
        y = random.randint(10 ** 9, 10 ** 10)
        cardnumber = str(400000) + str(y)
        if luhh(cardnumber):
            break

    print("Your card has been created")
    print("Your card number")
    print(cardnumber)
    print("Your card pin")
    print(inputpin)
    cur.execute("INSERT INTO card(number, pin, balance) VALUES (?,?,?);",(cardnumber, inputpin, 0))
    conn.commit()
    account[cardnumber] = inputpin


def logintoaccount():
    x1 = 1
    while x1 != 0:
        cardnumber = input("Enter your card number:")
        pin = input("Enter your PIN")
        if len(cardnumber) == 16:
            old_pin = cur.execute(f"SELECT pin FROM card WHERE number = {cardnumber} And pin = {pin};").fetchone()
            if type(old_pin) == type(None):
                print("Wrong card number or PIN!")
                return 0
            if  len(old_pin) == 1 and old_pin[0] == pin:
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
