
class Budget:
    #so the way I have this set up I don't plan on creating an overall Monthly Budget initiation so much as all the monthly categories...I set up different classes for them just to work on parent/child...but with the way I have it set up would I even need to do this? (aside from the fact that I changed the string dunder)
    monthly_income=4000
    budgeted_expenses=3500
    all_actual_expenses=0
    all_monthly_transactions={}         # what is the difference between having this here and having it under the init method
    all_budget_categories_status={}

    def __init__(self,name,monthly_budget):
        self.name=name
        self.monthly_budget=monthly_budget
        self.remaining_budget=monthly_budget
        self.total_spent=0
        self.transactions={f"Total {self.name} expenses": 0,}   #how would I put a $ in front of the number? (easiest way)
        self.percentage_of_income=round((self.monthly_budget/Budget.monthly_income)*100)      #since I'm rounding to the nearest whole, how would I make it so all of them add up to 100?
        Budget.all_monthly_transactions[self.name]=[]
        Budget.all_budget_categories_status[self.name]=f"${self.total_spent} spent out of {self.monthly_budget}."
        #Budget.all_budget_categories_status[self.name]=[[{self.total_spent}],[{self.monthly_budget}]]


    def transaction(self,expense_name,expense_amount, date):                #I started out wanting to put this in each of my children class, but it would've been a lot of repeated code,
        if expense_name in self.transactions:
            self.transactions[expense_name].append([expense_amount, date])
        else:
            self.transactions[expense_name]=[expense_amount, date]               #but I wanted to be able to change my variable names based on child name... any advice?
        self.transactions[f"Total {self.name} expenses"]+=expense_amount
        Budget.all_monthly_transactions[self.name].append([expense_name,expense_amount, date])
        Budget.all_actual_expenses+=expense_amount
        self.remaining_budget-=expense_amount
        self.total_spent+=expense_amount
        #Budget.all_budget_categories_status[self.name][0][0]+=expense_amount
    
    def __str__(self):
        return f"You currently have ${self.remaining_budget} left to spend out of your ${self.monthly_budget} {self.name} budget. {self.name} is {self.percentage_of_income}% of your monthly income."

    def get_overall_stats():
        return f"Your monthly income is ${Budget.monthly_income}, your budgeted expenses are ${Budget.budgeted_expenses}, your actual expenses for the month are ${Budget.all_actual_expenses}. The amount you have spent in each category is:\n{Budget.all_budget_categories_status}"


    def change_monthly_income(new_monthly_income):           #would this be better to use a getter/setter?
        Budget.monthly_income=new_monthly_income


    
