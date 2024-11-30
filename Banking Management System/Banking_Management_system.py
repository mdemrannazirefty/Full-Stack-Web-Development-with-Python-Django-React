# Banking Management system
class Bank:
    def __init__(self,uName,iBanance):
        self.name=uName
        self.balance=iBanance
    def Balance(self):
        return self.balance
    
    def Deposite(self,amount):
        if amount>=0:
            self.balance+=amount
            print("Deposite Successfull")
            return self.balance
        else:
            print("Invalid amount")
            return self.balance

    def Withdraw(self,w_amount):
        if w_amount >= 0:
            if w_amount <= self.balance:
                self.balance -= w_amount
                print("Withdraw Successfull")
                return self.balance
            else:
                print("Insufficient Balance")
                return self.balance
        else:
            print("Invalid amount")
            return self.balance

b =Bank("MD. EMRAN NAZIR EFTTY", 10000)
print("***********Welcome To Bank Management System**************")
print(f"BAccount Holder Name: {b.name}")
print()
while True:
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print()

    option = int(input("Choose any option: "))
    if option == 1:
        print(f"Your Current Balance: {b.Balance()}")
    elif option == 2:
        d_amount = int(input("Enter Deposit amount: "))
        b.Deposite(d_amount)
        print(f"Current Balance: {b.Balance()}")
        print()
    elif option == 3:
        w_amount = int(input("Enter Withdraw amount: "))
        b.Withdraw(w_amount)
        print(f"Current Balance: {b.Balance()}")
        print()
    elif option == 4:
        print("Thank you for using Bank Management System")
        break
    else:
        print("Invalid option")
