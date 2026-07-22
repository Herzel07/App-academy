# Addition, subtraction, and 
# multiplication do not need a safety check
# because they can work with zero as the second number

num1 = float(input("first number: "))
num2 = float(input("second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Check if the second number is zero before 
# doing division
# because Python cannot divide by zero
# These three (/, //, %) go inside because they 
# depend on num2 not being zero.
# Addition, subtraction, multiplication can
# stay above this block because they cannot crash.
if num2 == 0:
# Store error messages instead of crashing the calculator.
    division = "Cannot divide by zero" 
    floor_division = "Cannot divide by zero"
    modulus = "Cannot divide by zero"
else:
# If num2 is not zero, it is safe go ahead and perform these calculations
   division = num1 / num2 
   floor_division = num1 // num2 
   modulus = num1 % num2
