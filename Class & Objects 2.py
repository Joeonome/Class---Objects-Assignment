class Budget:
    """
    This is a Budget class, as prepared for my Zuri assignment
    """
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        
       

    def deposit(self):
    
        isdepositAmount = False
        while isdepositAmount == False:
     
            try:
                depositAmount = int(input("How much do you want to deposit? \n"))
                isdepositAmount = True
                
            except ValueError:
                print("Please enter a valid number")

        depositBal = depositAmount + self.amount
        print(f"Your {self.category} category has been updated to %d" %depositBal)
        return self.amount
       
            
    def withdrawal(self):
        iswithdrawalAmount = False
        while iswithdrawalAmount == False:
     
            try:
                withdrawAmount = int(input("How much do you want to withdraw? \n"))
                iswithdrawalAmount = True
                
            except ValueError:
                print("Please enter a valid number")
        
        withdrawBal = self.amount - withdrawAmount
        print(f"Your {self.category} category has been updated to %d" %withdrawBal)
        return self.amount


    def bal(self):
        print("Computing your balance....")
        print(f"Your balance is {self.amount}")


    def transferOfBalances(self):
       
        isTransferAmount = False
        while isTransferAmount == False:
     
            try:
                transferAmount = int(input("How much do you want to transfer? \n"))
                isTransferAmount = True
                
            except ValueError:
                print("Please enter a valid number")
                 
        selectedCategory = ["Food", "Clothing", "Rent", "Entertainment", "Education"]
        

        isTransferCategory = False
        while isTransferCategory == False:

            transferCategory = input("Which category will u like to transfer to? \n")
            
            if(transferCategory in selectedCategory):
                isTransferCategory = True
                print("****** Transferring *******")
            else:
                print("Incorrect Category")

        self.amount = self.amount - transferAmount
        print(f"Your {self.category} has been updated to {self.amount}")
        print("Your " + transferCategory + " has been credited with %d" %transferAmount)
        return self.amount


    """
    This is the property of the budget
    """

item1 = Budget("Food", 1600)
   
item2 = Budget("Clothing", 2000)
   
item3 = Budget("Rent", 60000)
   
item4 = Budget("Entertainment", 15000)
  
item5 = Budget("Education", 100000)
    
print(item1.category)
print(item2.amount)
item3.deposit()
item4.withdrawal()
item4.bal()
item5.transferOfBalances()