from classes.budget import Budget
from classes.savings import Savings

#Initiating Budgets
june_travel=Budget("June Travel", 150)
june_food=Budget("June Food", 700)
june_savings=Savings("June Savings", 450)
june_leisure=Budget("June Leisure", 300)
june_living=Budget("June Living", 2000)
june_miscellaneous=Budget("June Miscellaneous", 400)

#inputing one+ transaction per budget

june_food.transaction("Chic-fil-a",21.57, "Jun 5")
june_food.transaction("Chic-fil-a",30.00, "Jun 2")
june_food.transaction("Groceries",100.50, "Jun 3")
june_travel.transaction("Flight to CA", 149.23, "Jun 1")
june_living.transaction("Mortgage", 1200, "Jun 1")
june_savings.transaction("Transfer", 30, "Jun 5")
june_savings.transaction("Gift", 20, "Jun 2")
june_miscellaneous.transaction("Dog Food", 34.56, "Jun 4")
june_leisure.transaction("Laser Tag", 15.25, "Jun 5")


# testing instances:----------------------
#working:
# print(june_food)
# print(june_food.remaining_budget)
# print(june_food.total_spent)
# print(june_food.transactions)
# print(june_savings)
# print(june_savings.remaining_to_save)

#testing class attributes:-------------------
#working:
# print(Budget.all_actual_expenses)
# print(Budget.all_monthly_transactions)
# Budget.change_monthly_income(4500)      #working but doesnt update % for instances
# print(Budget.monthly_income)
# print(june_food)            #instance monthly % does not change when I change the monthly income.

#Not working:
# print(Budget.all_budget_categories_status)      #each say $0 spent
#print(Budget.get_overall_stats())      the dictionary is not being updated with the new "self.total.spent" amount
                                        #tried using line 19 and 32, but got the error "TypeError: unsupported operand type(s) for +=: 'set' and 'float'"
