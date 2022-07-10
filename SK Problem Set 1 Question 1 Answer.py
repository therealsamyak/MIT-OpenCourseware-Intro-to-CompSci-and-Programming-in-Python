
#User Input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#Defining More Variables
#Down payment is assumed to be 25% total cost
portion_down_payment = 0.25*total_cost
current_savings = 0
# r is 4%
r = 0.04
months = 0


# Math
while current_savings < portion_down_payment:
        months += 1
        current_savings += current_savings*r/float(12)
        current_savings += portion_saved*annual_salary/float(12)

print("Number of months: " + str(months))

