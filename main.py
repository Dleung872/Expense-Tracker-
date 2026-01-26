from time import sleep

expenses = []

def add(item, amount):
    expenses.append(
        {
            'item': item,
            'amount': amount
        }
    )

def main():
    while True:
        print('1. add\n2. see list\n3. remove\n4. exit')
        user_input = input("> ")
        if user_input == '1' or user_input == 'add':
                user_item = input('item: ')
                user_expense = input('amount: ')
                add(user_item, user_expense)
                print(expenses)
                sleep(3)
                print('\033c')
                continue
        
        elif user_input == '4' or user_input == 'exit':
            print('bye')
            sleep(0.5)
            print('\033c')
            return
main()