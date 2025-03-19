

import random
def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐',]

    return [ random.choice(symbols)for _ in range(3)]

def print_row(row):
    print("*********")
    print("-".join(row))
    print("*********")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐':
            return bet*20
    return 0

def main():
    balance =100
    print("*********************")
    print("welcome to python slots")
    print("*********************")
    print("symbols: 🍒🍉🍋🔔⭐")
    print("*********************")

    while balance > 0:
        print(f"current balance ${balance}")

        bet = input("enter bet: ")
        if not bet.isdigit():
            print("enter valid bet")
            continue
        bet =int(bet)
        if bet > balance:
            print("insufficient funds")
            continue
        if bet< 0:
            print("enter valid bet")
            continue
        balance-= bet

        row = spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"you won: ${payout}")
        else:
            print("you lost....try again")
        balance+=payout
        if balance < 1:
            print("you are now homeless")






if __name__ == '__main__':
    main()
