database = {}
import random

def init():
    isValidSelection = False
    print("Welcome to Python National Bank")

    while isValidSelection == False:
         haveAccount = int(input("Do you have an account with us?: Press 1 (for yes) or 2 (for no). \n"))
         if(haveAccount == 1):
             isValidSelection = True
             login()
         elif(haveAccount == 2):
            isValidSelection = True
            print(register())
         else:
             print("You have selected an invalid option. Please try again.")

def login():
    print("**** LOGIN ****")

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberByUser = int(input("Please enter your account number. \n"))
        password = input("Please enter your password. \n")
        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberByUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True
                else:
                    print('Invalid account number or password. Please try again')


    bankOperation(userDetails)



def register():
    print('**** Register your new account. *****')
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a secure password to use: \n")

    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password,]

    print("Your account has been created.")
    print("Your account number is: %d" % accountNumber)

    login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1])) 
    
    selectedOption = int(input("What service do you need? (1) Deposit, (2) Withdrawal, (3) Logoff, (4) Exit. \n")) 

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logoff()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected. Please try again")
    bankOperation(user)
        

def withdrawalOperation():
    print("**** WITHDRAW ****")
    print("Your current balance is $%s" % currentBalance())
    if(currentBalance() <= 0):
        print("Insufficient funds in your account.")
    else:
        withdrawalAmount = int(input("How much money would you like to withdraw from your account? \n"))
        updatedBalance = currentBalance() - withdrawalAmount
        print("Your new balance is $%s " % updatedBalance)
        print("** Thank you for choosing National Python Bank. **")
        exit()
        

def depositOperation():
    print("**** DEPOSIT ****")
    print("Your current balance is $%s" % currentBalance())
    depositAmount = int(input("How much money would you like to deposit into your account? \n"))
    newBalance = currentBalance() + depositAmount
    print("Your new balance is $%s" % newBalance) 
    print("** Thank you for choosing National Python Bank. **")
    exit()
    


def logoff():
    print("Logoff")
    login()

def generateAccountNumber():
    print("Generating your Account Number")

    return random.randrange(1111111111,9999999999)

def currentBalance():
   return random.randint(0,100)
  

    


    
#def updatedBalance():
    

## BANK SYSTEM ##
init()

