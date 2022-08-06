# constant that represents the % of the total cost that must be made as a down payment
portion_down_payment = .25

# Dollars the user had saved already ofr the house
current_savings = 0

# annual return rate
r = 0.04


# ask the user for there annual salary
annual_salary = int(input("Enter your annual salary: "))

# ask the user how much they are going to save for each month for there house
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))

# ask the user for the cost of there dream home
total_cost = int(input("Enter the cost of your dream home: "))

# money needed for down payment
down_payment = portion_down_payment*total_cost

months = 0

# loops through each month checking if the user has saved enough money
while current_savings < down_payment:
    # adds the return on investment
    current_savings += (current_savings*r)/12

    # adds the money made this month
    current_savings += portion_saved * (annual_salary / 12)

    # adds 1 to the number of months
    months += 1

# returns months to user
print(f"Number of months: {months}")
