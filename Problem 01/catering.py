# Get user input

adultMeals = int(input('Please enter the number of adult meals: '))
childMeals = int(input('Please enter the number of child meals: '))
gratuity = float(input('Please enter the percentage of gratituity: '))
depositPaid = float(input('Please enter the amount of deposit paid: '))

gratuity = gratuity / 100

#Assign the fixed values
COST_OF_ADULT_MEAL = 30
COST_OF_CHILD_MEAL = COST_OF_ADULT_MEAL/2
TAX_RATE = 20/100

# Calculate cost
mealCost = COST_OF_ADULT_MEAL * adultMeals + COST_OF_CHILD_MEAL * childMeals
tax = TAX_RATE * mealCost
gratuityAmount = mealCost * gratuity

totalCost = mealCost + tax + gratuityAmount

owingAmount = totalCost - depositPaid

# Print the output
print('Meal Cost: $%.2f' %mealCost)
print('Gratuity: $%.2f' %gratuityAmount)
print('Tax: $%.2f' %tax)
print('Total Cost: $%.2f' %totalCost)
print('Deposit: $%.2f' %depositPaid)
print('Amount Owing: $%.2f' %owingAmount)
