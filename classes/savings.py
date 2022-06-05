from classes.budget import Budget
class Savings(Budget):

    def __init__(self, name, monthly_goal):
        self.name=name
        self.monthly_goal=monthly_goal        
        self.remaining_to_save=monthly_goal
        self.total_saved=0
        self.transactions={f"Total {self.name}": 0,}
        self.percentage_of_income=round(Budget.monthly_income/self.monthly_goal)      #since I'm rounding to the nearest whole, how would I make it so all of them add up to 100?
        Budget.all_monthly_transactions[self.name]=[]
        Budget.all_budget_categories_status[self.name]=f"${self.total_saved} saved out of a goal of {self.monthly_goal}."

    def transaction(self,transaction_name,transaction_amount, date):                #I started out wanting to put this in each of my children class, but it would've been a lot of repeated code,
        self.transactions[transaction_name]=[transaction_amount, date]               #but I wanted to be able to change my variable names based on child name... any advice?
        self.transactions[f"Total {self.name}"]+=transaction_amount
        Budget.all_monthly_transactions[self.name].append([transaction_name,transaction_amount, date])
        Budget.all_budget_categories_status[self.name]=f"${self.total_saved} saved out of {self.monthly_goal}."
        self.remaining_to_save-=transaction_amount
        self.total_saved+=transaction_amount


    def __str__(self):
        return f"You have saved a total of ${self.total_saved} out of your monthly goal of ${self.monthly_goal}."