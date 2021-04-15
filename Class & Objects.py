class Budget:
    """
    This is a Budget class, as prepared for my Zuri assignment
    """
    def __init__(self, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
       

   # def Deposit(self):

    #def Withdrawal(self):

    #def TransferOfBalances(self):

    """
    This is the property of each item in each category
    """

food = Budget(
    {
        "Rice": 1600
    },
    {
        "Beans": 1400
    },
    {
        "Garri": 600
    }
    ) 

clothing = Budget(
    {
        "Jacket": 2000
    },
    {
        "Native": 5000
    },
    {
        "Shoe": 15000
    }
    ) 
rent = Budget(
    {
        "Home": 60000
    },
    {
        "Store": 20000
    },
    {
        "Office": 30000
    }
    ) 
entertainment = Budget(
    {
        "Music": 15000
    },
    {
        "Movies": 20000
    },
    {
        "Vacation": 40000
    }
    ) 
education = Budget(
    {
        "Textbooks": 100000
    },
    {
        "Stethoscope": 50000
    },
    {
        "Fees": 150000
    }
    )

print(food.item1)
print(education.item2)