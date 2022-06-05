class Budget():
    #so the way I have this set up I don't plan on creating an overall Monthly Budget initiation so much as all the monthly categories...I set up different classes for them just to work on parent/child...but with the way I have it set up would I even need to do this? (aside from the fact that I changed the string dunder)
    monthly_income=4000
    budgeted_expenses=3500
    actual_expenses=0
    all_monthly_transactions={}         # what is the difference between having this here and having it under the init method
    

    def __init__(self,name,monthly_budget):
        self.name=name
        self.monthly_budget=monthly_budget
        self.remaining_budget=monthly_budget
        self.transactions={}
        self.percentage_of_income=round(Budget.monthly_income/self.monthly_budget)      #since I'm rounding to the nearest whole, how would I make it so all of them add up to 100?

    def transaction(self,expense_name,expense_amount, date):                #I started out wanting to put this in each of my children class, but it would've been a lot of repeated code,
        self.transactions[expense_name]=[expense_amount, date]              #but I wanted to be able to change my variable names based on child name... any advice?
        self.transactions[f"Total {self.name} expenses"]+=expense_amount
        Budget.all_monthly_transactions[self.name].append([expense_name,expense_amount, date])
        Budget.actual_expenses+=expense_amount
        self.remaining_budget-=expense_amount
    
    def __str__(self):
        return f"You currently have ${self.remaining_budget} left to spend out of your ${self.monthly_budget} monthly {self.name} budget. {self.name} is {self.percentage_of_income}% of your monthly income."

    def get_overall_stats():
        print(f"Your monthly income is ${Budget.monthly_income}, your budgeted expenses are ${Budget.budgeted_expenses}, your actual expenses for the month are ${Budget.actual_expenses}.")


    def change_monthly_income(self,new_monthly_income):           #would this be better to use a getter/setter?
        Budget.monthly_income=new_monthly_income


