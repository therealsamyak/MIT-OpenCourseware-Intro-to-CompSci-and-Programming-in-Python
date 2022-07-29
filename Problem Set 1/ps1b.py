
#User Input
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

#Defining More Variables
#Down payment is assumed to be 25% total cost
portion_down_payment = float(0.25)*float(total_cost)
current_savings = 0
# r is 4%
r = 0.04
months = 0
Month_Six_Counter = 0 

# Math
while current_savings < portion_down_payment:
    months += 1
    current_savings += float(current_savings)*float(r)/float(12)   
    current_savings += float(portion_saved)*float(annual_salary)/float(12)
    float(current_savings)

    #checking for multiple of 6
    Month_Six_Counter += 1
    if Month_Six_Counter == 6:
        annual_salary += annual_salary*semi_annual_raise
        Month_Six_Counter = 0
        
print("Number of months: " + str(months))

