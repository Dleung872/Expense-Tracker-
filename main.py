import os
from datetime import datetime
from time import sleep

expense_categories = set([])
expenses = [

]
#input 1
def category_making(): #makes a category
    category = input("Create a new expense category: ")
    expense_categories.add(category)
    print('category added')
    sleep(1)
    print("\033c")
    
#input 2
def category_delet(): #removeing category
    cat_list = sorted(list(expense_categories))
    for id, cats in enumerate(cat_list):
        print(f'{id+1}. {cats}')
    user_cat_removal = int(input('which category id to remove: '))
    cat_actual_name = cat_list[user_cat_removal-1]
    expense_categories.remove(cat_actual_name)
    sleep(1)
    print('\033c')
    
#input 3
def open_category(): #open the categories
    cat_list = sorted(list(expense_categories))
    if len(cat_list) == 0:
        print('you have no categories')
        input('press ENTER to continue')
        print('\033c')
        return
    for id, cats in enumerate(cat_list):
        print(f'{id+1}. {cats}')
    user_open_cats = int(input('which category would you like to open\n> '))
    print('\033c')
    
    filtered_exp = []
    for exp in expenses:
        if exp["category"] == cat_list[user_open_cats-1]:
            filtered_exp.append(exp)
            
    if len(filtered_exp) == 0:
        print('you got nothing in here')
        sleep(1)
        print('\033c')
        
    else:
        for exp in filtered_exp:
            print(f"{exp['item']}: {exp['amount']}")
            input('\npress ENTER to continue')
            print('\033c')
            
#input 4        
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
    for item in expenses:
        print(f'{item}')
    sleep(1)
    print('\033c')

def expense_to_category():  #putting the expenses into a category
    for id, object in enumerate(expenses):
        print(f'{id+1}. {object}')
    user_item_choice = int(input('pick expense id to add to a category: '))
    the_item = expenses[user_item_choice-1]
    cat_list = sorted(list(expense_categories))
    for id, cats in enumerate(cat_list):
        print(f'{id+1}. {cats}')
    user_cat_choice = int(input('add to which category: '))
    the_item['category'] = cat_list[user_cat_choice-1]
    sleep(2)
    print('\033c')

#input 5
def remove_expenses():
    cat_list = sorted(list(expense_categories))
    for id, cats in enumerate(cat_list):
        print(f'{id+1}. {cats}')
    user_cat_choice = int(input('remove from which category: '))
    print('')
    
    list_filter = []
    for id, object in enumerate(expenses):
        if object['category'] == cat_list[user_cat_choice-1]:
            list_filter.append(object)
            
    for id, object in enumerate(list_filter):
        print(f'{id+1}. {object}')
        
    user_item_choice = int(input('pick expense id to remove from a category: '))
    the_item = list_filter[user_item_choice-1]
    the_item['category'] = ""
    sleep(1)
    print('\033c')
    
#main funtion
def main():
    while True:
        print("Menu:") 
        print("----------categories----------")
        print("1. create category")
        print("2. remove category")
        print("3. open category")
        print("----------items----------")
        print("4. add item")
        print('5. remove item')
        print("--------------------------")
        choice = input("Choose an option: (1/2/3/4)\n> ")
        
        if choice == "1":
            print('\033c')
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
            print('\033c')
            open_category()
            
        elif choice == '4':
            add_number_check()
            expense_to_category()
            
        elif choice == '5':
            print('\033c')
            remove_expenses()
        
main()