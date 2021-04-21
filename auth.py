import random
import validation
import database
from getpass import getpass

def init():

    is_valid_selection = False
    print("Welcome to Python National Bank")

    have_account = int(input("Do you have an account with us?: Press 1 (for yes) or 2 (for no). \n"))

    if have_account == 1:
        is_valid_selection = True
        login()
    elif have_account == 2:
        is_valid_selection = True
        print(register())
    else:
        print("You have selected an invalid option. Please try again.")


def login():
    print("**** LOGIN ****")

    account_number_by_user = input("Please enter your account number. \n")

    is_valid_account_number = validation.account_number_validation(account_number_by_user)

    if is_valid_account_number:

        password = getpass("Please enter your password. \n")

        user = database.authenticated_user(is_valid_account_number, password)
        if user:
            bank_operation(user)

        print('Invalid account number or password. Please try again')
        login()
    else:
        init()


def register():
    print('**** Register your new account. *****')

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")

    password = getpass("Please create a secure password to use: \n")

    account_number = generate_account_number()



    # database[accountNumber] = [first_name, last_name, email, password, 0]

    is_user_created = database.create(account_number, first_name, last_name, email, password)
    
    if is_user_created:
        print("Your account has been created.")
        print("Your account number is: %d" % account_number)
        login()
    else:
        print("Something went wrong, please try again.")
        register()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selected_option = int(input("What service do you need? (1) Deposit, (2) Withdrawal, (3) Logoff, (4) Exit. \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        logoff()

    elif selected_option == 4:
        exit()

    else:
        print("Invalid option selected. Please try again")

    bank_operation(user)


def withdrawal_operation(user_data):
    print("**** WITHDRAW ****")
    print("Your current balance is $%s" % current_balance(user_data[4]))
    if current_balance(user_data[4]) <= 0:
        print("Insufficient funds in your account.")
    else:
        database.user_withdrawal(user_data[4])
        exit()

        #withdrawal_amount = int(input("How much money would you like to withdraw from your account? \n"))
        # updated_balance = current_balance(user_details) - withdrawal_amount

def deposit_operation(user_data):
    print("**** DEPOSIT ****")
    print("Your current balance is $%s" % current_balance(user_data[4]))
    database.user_deposit(user_data[4])
    exit()


def logoff():
    print("Logoff")
    login()


def generate_account_number():
    print("Generating your Account Number")

    return random.randrange(1111111111, 9999999999)


def current_balance(user_data):
    balance = user_data[4]
    return user_data[4]


# def updatedBalance():


## BANK SYSTEM ##
init()
