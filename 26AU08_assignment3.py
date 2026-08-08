class UPI:

    def pay(self, amount):
        print("Paying by UPI")
        print("Payment of " + str(amt) + " successful via UPI")


class NetBanking:

    def pay(self, amount):
        print("Paying by NetBanking")
        print("Payment of " + str(amt) + " successful via NetBanking")

class CreditCard:

    def pay(self, amount):
        print("Paying by CreditCard")
        print("Payment of " + str(amt) + " successful via CreditCard")

class DebitCard:

    def pay(self, amount):
        print("Paying by DebitCard")
        print("Payment of " + str(amt) + " successful via DebitCard")


class PAYMENT:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def start(self, amount):
        self.payment_method.pay(amount)

choice = int(input("Enter your choice: 1.UPI 2.NetBanking 3.CreditCard 4.DebitCard \n"))
amt = float(input("Enter the amount to be paid: "))
if choice == 1:
    t = PAYMENT(UPI())
    t.start(amt)
elif choice == 2:
    t = PAYMENT(NetBanking())
    t.start(amt)
elif choice == 3:
    t = PAYMENT(CreditCard())
    t.start(amt)
elif choice == 4:
    t = PAYMENT(DebitCard())
    t.start(amt)
else:
    print("Invalid choice")

