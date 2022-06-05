class Budget():

    def __init__(self,monthly_income,monthly_budget):
        self.monthly_income=monthly_income
        self.monthly_budget=monthly_budget

    all_monthly_transactions={}         # what is the difference between having this here and having it under the init method?

    total_monthly_expenses=0

    def change_monthly_income(self,new_monthly_income):           #would this be better to use a getter/setter?
        self.monthly_income=new_monthly_income

june_2022=Budget(4000,3500)

# food: [[chic-fil-a,300,3/12/21],