import json
import string
import random


def home_page():
    print('HNGBank Staff Platform')
    print('''Type
1 -> STAFF LOGIN
2 -> CLOSE APP''')

    log = ('1', '2')
    entry_choice = ''

    while not entry_choice:
        choice = str(input('>> '))
        if choice in log:
            entry_choice = choice
        else:
            print('Type 1 or 2')
    return sign_on(entry_choice)


database = [{'username': 'kunle.o',
            'password': 'ko1234',
                        'email': 'kunle.oye@hng.com',
                        'fullname': 'kunle oye'},
                       {'username': 'stanley.e',
                        'password': 'se1234',
                        'email': 'stanley.eyinka@hng.com',
                        'fullname': 'stanley eyinka'}]
drop = json.dumps(database, indent=2)
with open('staff.txt', 'w') as user_info:
    user_info.write(drop)


def sign_on(entry_choice):
    if entry_choice == '1':
        username = input('Username: \n')
        password = input('Password: \n')

        with open('staff.txt') as user_details:
            drop1 = json.load(user_details)
            for contents in database:
                if contents['username'] == username and contents['password'] == password:
                    print('Access Grant. Welcome to the Customer Portal')
                    break
            else:
                print('Wrong username or password. \n Try Again')

        return banking_options()
    else:
        print('Goodbye')

def banking_options():
    print('Banking Options')
    print('''Type
1 -> Create New Bank Account
2 -> Check Account Balance
3 -> Logout
''')

    bank_choice = ('1', '2', '3')
    entry_choice1 = ''

    while not entry_choice1:
        choice1 = str(input('>> '))
        if choice1 in bank_choice:
            entry_choice1 = choice1
        else:
            print('Type 1 or 2')
    return customer_append(entry_choice1)


def customer_append(entry_choice1):
    if entry_choice1 == '1':
        account_name = input('Account Name: ')
        opening_balance = (input('Opening Balance: '))
        account_type = input('Account Type: ')
        account_email = input('Account Email: ')

        with open('customer.txt', 'w') as customer_details:
            for items in customer_details:
                customer_details.write(account_name)
                customer_details.write(opening_balance)
                customer_details.write(account_type)
                customer_details.write(account_email)
                random_length = 10
                account_number = ''.join(map(str, [random.randint(1, 9) for r in range(random_length)]))
                print("Customer's Account Number: ", account_number)
                customer_details.write(account_number)
        return banking_options()
    elif entry_choice1 == 2:
        with open('customer.txt',) as customer_database:
            customer_database.read()
            print(customer_database)
        return banking_options()
    else:
        print('Goodbye')
        return sign_on()


home_page()