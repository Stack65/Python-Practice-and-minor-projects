def show_balance(balance):
    print(f"your balance is ${balance:.2f}")
def deposit():
    amount = float(input("enter amount to deposit: "))
    if amount < 0:
        print("you cannot deposit negative amount")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("enter amount to withdraw: "))
    if amount > 0:
        print("not enough funds")
        return 0
    elif amount < 0:
        print("Enter an amount greater than 0")
        return 0
    else :
        return amount

def main():
    is_running =True
    balance = 0
    while is_running:
        print("********************")
        print("Banking Program")
        print("********************")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
           balance+= deposit()
        elif choice == "3":
           balance -= withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you for using Banking py6thon")
if __name__ == "__main__":
    main()
