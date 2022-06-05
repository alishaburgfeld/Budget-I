from classes.budget import Budget


june_2022_food=Budget("June 2022 Food", 700)

print(june_2022_food)

june_2022_food.transaction("chic-fil-a",21.57, "Jun 5")

print(june_2022_food.transaction)
print(june_2022_food.remaining_budget)
# print(june_2022_food)
# print(Budget.actual_expenses)
# print(Budget.all_monthly_transactions)
# print(Budget.get_overall_stats())