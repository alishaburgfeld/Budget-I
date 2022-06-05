# from budget import Budget
from classes.budget import Budget

class Food(Budget):
    def __init__(self,monthly_food_budget):
        self.monthly_food_budget=monthly_food_budget
        self.remaining_food_budget=monthly_food_budget
        self.transactions={}
        self.percentage_of_income=round(Budget.monthly_income/self.monthly_food_budget)

    def transaction(self,expense_name,expense_amount, date):                #I started out wanting to put this in my parent class since
        self.transactions[expense_name]=[expense_amount, date]              #I will use it for all children, but I wanted to be able to change my variable names based on child name... any advice?
        self.transactions["Total food expenses"]+=expense_amount
        Budget.all_monthly_transactions["Food"].append([expense_name,expense_amount, date])
        Budget.total_monthly_expenses+=expense_amount
        self.remaining_food_budget-=expense_amount

    def __str__(self):
        print(f"You currently have {self.remaining_food_budget} left to spend out of your {self.monthly_food_budget} monthly food budget. Food is {self.percentage_of_income}% of your monthly income.")

# june_2022_food=Food(700)

# print(june_2022_food)
