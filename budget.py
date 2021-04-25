class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    
    def depsoit(self, amount):
        self.amount += amount
        return "You have sucesssfully deposited ${} into your {} category.".format(amount, self.category)

    def budget_balance(self):
        return "This is your current balance: ${}".format(self.amount)

    def check_balance(self, amount):
        withdraw_amount = self.amount - amount

        transfer_amount = self.amount - amount

        if withdraw_amount < self.amount:
          # print("Your balance is: ${}".format(self.amount))
           return True

        elif transfer_amount < self.amount:
            #print("You have gone over your bugdet. Your balance is: ${}".format(self.amount))
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn ${} from your {} category.".format(amount, self.category)

    def transfer(self, amount, category):
        self.check_balance(amount)
        if self.check_balance(amount) == True:
            transfer_amount_1 = self.amount - amount
            return "You have successfully transferred ${} to {} category".format(transfer_amount_1, category)
        else:
            return "You don't have enough money to transfer"
        #transfer between two instantiated categories
    

food_category = Category("Food", 500)
clothing_category = Category("Clothing", 250)
car_expenses = Category("Car Expenses", 700)

#print(clothing_category.depsoit(150))
#print(clothing_category.budget_balance())
#print(food_category.withdraw(200))
#print(food_category.budget_balance())
#print(food_category.check_balance(500))
print(car_expenses.transfer(600, "Food"))
print(clothing_category.transfer(150, 'Car Expenses'))