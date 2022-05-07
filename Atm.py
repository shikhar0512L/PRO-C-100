class atm(object):
    def __init__(self, card_num, pin):
        self.card_num = card_num
        self.pin = pin

    def Check_balance(self):
        print('Your balance is 99999999999999999999')

    def widral(self, amount):
        new_amount = 99999999999999999999-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance " + str(new_amount))


def main():
    cardNumber = input("Enter your card number: ")
    pin = input("Enter your pin: ")

    newUser = atm(cardNumber, pin)
    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        newUser.Check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        newUser.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
