# constant that represents the % of the total cost that must be made as a down payment
portion_down_payment = .25

# constant - semi-annual raise %
semi_annual_raise = .07

# Dollars the user had saved already ofr the house
current_savings = 0

# constant - cost of dream home
total_cost = 1000000

# constant - number of months to save for
months = 36

# annual return rate
r = 0.04


# ask the user for there annual salary
annual_salary = int(input("Enter your annual salary: "))


# money needed for down payment
down_payment = portion_down_payment*total_cost


# max and min % that can be saved
max_guess = 1000
min_guess = 0

# sets up counter to count the number of steps it takes
counter = 0

# defines saved money
saved_money = 0

# sets up guess variable
guess = max_guess/2

possible = True

# loops through and checks of the amount of money saved is equal to the amount of money needed
while abs(saved_money - down_payment) >= 100:

    # resets numbers
    annual_salary_copy = annual_salary
    saved_money = 0

    # calculates money saved at the guess rate

    # converts the guess to a %
    guess_percentage = guess / 1000

    # loops through each year and adds the annual return rate
    for i in range(months//12):
        saved_money += saved_money*r

        # adds semi-annual raise to salary
        annual_salary_copy += annual_salary_copy*semi_annual_raise
        annual_salary_copy += annual_salary_copy*semi_annual_raise

        saved_money += annual_salary_copy*guess_percentage

    # checks if the guess was to high or to low and then changes value accordingly
    if(saved_money > down_payment):
        max_guess = guess
        guess = guess - ((max_guess-min_guess)/2)
    elif(saved_money < down_payment):
        min_guess = guess
        guess = ((max_guess-min_guess)/2) + guess

    # checks if guess is to high
    if(guess > max_guess-1):
        print("It is not possible to pay the down payment in three years.")
        possible = False
        break

    # increases counter
    counter += 1

# checks if ist possible to get the down payment in 3 years
if possible:
    print(f"Best savings rate: {guess/1000}")
    print(f"Steps in bisection search: {counter}")
