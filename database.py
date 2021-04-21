import os
import validation

user_db_path = "data/user_record/"
user_db_path_2 = "data/auth_session/"


def create(user_account_number, first_name, last_name, email, password):

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):
        print("User already exists")
        return False

    if does_email_exist(email):
        print("User email already exists")
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + '.txt', "x")

    except FileExistsError:
        print('User file already exists')
        does_file_have_data = read(user_db_path + str(user_account_number) + '.txt')
        if not does_file_have_data:
            delete(user_account_number)

    else:
        f.write(str(user_data))
        completion_state = True

    finally:
        f.close()
        
    return completion_state


def update(user_account_number, user_data):
    balance = user_data[4]

    updated_user_data = user_data[0] + "," + user_data[1] + "," + user_data[2] + "," + user_data[3] + "," + str(user_data[4])
    f = open(user_db_path + str(user_account_number) + ".txt", "w")
    f.write(updated_user_data)
    f.close()

def user_withdrawal(user_account_number, user_data):
    balance = user_data[4]
    withdrawal_amount = int(input("How much money would you like to withdraw? \n"))
    updated_balance = balance - withdrawal_amount
    print("Your new balance is $%s " % updated_balance)
    print("** Thank you for choosing National Python Bank. **")
    return update(user_account_number, user_data)
    exit()

def user_deposit(user_account_number, user_data):
    balance = user_data[4]
    deposit_amount = int(input("How much money would you like to deposit into your account? \n"))
    updated_balance = balance + deposit_amount
    print("Your new balance is $%s" % updated_balance)
    print("** Thank you for choosing National Python Bank. **")
    return update(user_account_number, user_data)
    exit()






def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + '.txt', "r")

        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError: #FileNotFoundError
            print("User not found")

    except FileExistsError: #FileExistsError
        print("User doesn't exist")

    except TypeError: #TypeError
        print("Invalid account number format")

    else:
        return f.readline()

    return False



def delete(user_account_number):
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:
            os.remove(user_db_path + str(user_account_number) + '.txt')
            is_delete_successful = True

        except FileNotFoundError:
            print("User not found")
            return False

        finally:

            return is_delete_successful


# searches for specific things like email,
def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), "'")
        if email in user_list:
            return True
    return False

def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False

def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ",")
        if password == user[3]:
            return user

    return False

def login_session(account_number, password):
    if authenticated_user(account_number, password):
        f = open(user_db_path_2 + str(account_number) + ".txt", "x")
        user_login = True
        if user_login == False:
            delete(login_session(account_number, password))
