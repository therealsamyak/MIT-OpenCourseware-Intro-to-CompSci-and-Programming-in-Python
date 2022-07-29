#User Input
initial_annual_salary = float(input("Enter your starting annual salary: "))
annual_salary = initial_annual_salary
total_cost = 1000000
semi_annual_raise = .07

#math variables
portion_down_payment = float(0.25)*float(total_cost)
current_savings = 0
r = 0.04
months = 0
Month_Six_Counter = 0

#bisection search variables
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = (high+low)/2.0
portion_saved = float(guess)/float(10000)

#overflow prevention
infinite_detector = 0

#salary test booleans
rich = False
wealthy = False

#checking 100% savings to see if they can afford
while months < 36:
    months += 1
    current_savings += float(current_savings)*float(r)/float(12)   
    current_savings += 1*float(annual_salary)/float(12)
    float(current_savings)
     
    #checking for multiple of 6
    Month_Six_Counter += 1
    if Month_Six_Counter == 6:
        annual_salary += annual_salary*semi_annual_raise
        Month_Six_Counter = 0    

if portion_down_payment > current_savings:
   rich = False

else:
    rich = True

# loop for bisections search
while abs(portion_down_payment - current_savings) > epsilon and rich:
    #reset attempt
    current_savings = 0.0
    months = 0
    annual_salary = initial_annual_salary
    
    #math for amount saved in 3 years
    while months < 36:
        months += 1
        current_savings += float(current_savings)*float(r)/float(12)   
        current_savings += float(portion_saved)*float(annual_salary)/float(12)
        float(current_savings)
         
        #checking for multiple of 6
        Month_Six_Counter += 1
        if Month_Six_Counter == 6:
            annual_salary += annual_salary*semi_annual_raise
            Month_Six_Counter = 0        

    #modifying guess
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    
    #new guess
    guess = (high+low)/2.0
    portion_saved = float(guess)/float(10000)
    num_guesses += 1

    #overflow prevention
    if portion_saved < 0.00001:
        wealthy = True
        break

#closing statements
if rich and not wealthy:
    print("Best Savings Rate: " + str(portion_saved))
    print("Steps in bisection search: " + str(num_guesses))

elif not rich and not wealthy:
    print("It is not possible to pay the downpayment in three years. ")

else:
    print("You don't need this calculator :)")