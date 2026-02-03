import os
from datetime import datetime
from time import sleep

expense_categories = set(["thing", "another"])
expenses = [
    {
       'item': 'Hi im first! Apple orANGES/474875225allan zukerbiurg',
       'amount': '3.1415926535897932384626433832795028841971',
       'category': ''
    },
        {
       'item': 'i am second, six seven allan zukerb145145iurg',
       'amount': '3.1415926535897932384626433832795028841971',
       'category': ''
    },
            {
       'item': 'i am third, idk kill epstein allan zu145145145kerbiurg',
       'amount': '3.1415926535897932384626433832795028841971',
       'category': ''
    },
        {
       'item': 'fourth, aaaaaallan z14622362366ukerbiurg',
       'amount': '3.1415926535897932384626433832795028841971',
       'category': ''
    },
        {
       'item': 'last. daeth.allan zuk89999999erbiurg',
       'amount': '3.1415926535897932384626433832795028841971',
       'category': ''
    }

]

def category_making(): #makes a category
    category = input("\nCreate a new expense category: ")
    expense_categories.add(category)
    print('category added')
    sleep(1)
    print("\033c")

def category_delet(): #removeing category
    for cats in expense_categories:
        print(f'categories: {cats}')
    user_cat_remove = input('pick one to remove: ')
    if user_cat_remove != cats in expense_categories:
        print('\nthis category does not exist')
        input('press Enter to continue')
        print('\033c')
    else:
        expense_categories.remove(user_cat_remove)
        print('removed')
        sleep(1)
        print('\033c')

def antidisestablishmentarianism(): #open the categories
    for cats in expense_categories:
         print(f'categories: {cats}')
    user_open_cats = input('which category would you like to open\n> ')
    for exp in expenses:
        if exp["category"] == user_open_cats:
            print(f"- {exp["item"]}")


def expense_to_category():  #putting the expenses into a category
    for id, exp in enumerate(expenses):
        print(f"{id+1}, {exp["item"]}")
    uin = input("what u want brochacho> ")
    target_expense = expenses[int(uin)-1]
    
    #print("USER CHOSE THIS : >>>>>>>>" + target_expense["item"])
    
    print("Available Categories:")
    for cats in expense_categories:
        print(f'- {cats}') 
    user_pick = input('pick one to add expense: ')
    target_expense["category"] = user_pick
    
    
            
def add_expenses(item, amount):
    expenses.append(
        {
            'item': item,
            'amount': amount,
            'category': ''
        }
    )

def add_number_check():
    user_item = input('\nitem: ')
    while True:
        user_expense = (input('amount: '))
        try:
            user_expense = float(user_expense)
            break
        except:
            print("input numberic amount")
            continue
    add_expenses(user_item, user_expense)
    print(expenses)
    sleep(1)
    print('\033c')
    
def remove_expenses():
    for index, item in enumerate(expenses):
        print(f"{index+1}. {item["item"]}")
    user_removal = int(input('\nwhich number item would you like to remove?: '))
    expenses.pop(user_removal-1)


# def expense_calculation():

            
            
def main():
    while True:
        print("Menu:") 
        print("1. create category")
        print("2. remove category")
        print("3. open category")
        print("4. assign category to an item")
        choice = input("Choose an option: (1/2/3/4)\n> ")
        
        if choice == "1":
            category_making()
           
        elif choice == '2':
                if len(expense_categories) == 0:
                    input('you have no catergory\npress Enter to continue')
                    print('\033c')
                    continue
                else:
                    print('')
                    category_delet() 
                    
        elif choice == '3':
            antidisestablishmentarianism()
            
        elif choice == '4':
            expense_to_category()
        # elif choice == "2":
        #     expense_to_category()
        #     add_number_check()
            
        # elif choice == '3':
        #     remove_expenses()
        
        # elif choice == '4':
        #     for index, item in enumerate(expenses):
        #         print(f"{index+1}. {item["item"]}")
        #     input('press ENTER to continue')
        #     print('\033c')

main()