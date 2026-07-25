# STEP 1:
# Create a fixed bank balance.
# The user is NOT asked for this value.
Balance = 500

# STEP 2:
# Ask the user how much money they want to withdraw.
# We use int() because money is entered as a number.
withdrawal_amount = int(input("Enter withdrawal amount:"))


# STEP 3:
# Check if the withdrawal amount is invalid.
# We check this FIRST because negative numbers
# are also less than the balance
if withdrawal_amount <= 0:
     print("Invalid amount. You must withdraw more than RO.")

# STEP 4:
# If the amount is valid, check if the user
# has enough money in the account. elif withdrawal amount <= balance:
elif withdrawal_amount <= balance:
# Deduct the money from the balance.
         balance = balance - withdrawal_amount

# Display the new balance.
print(f"Withdrawal successful! Remaining balance: R{balance}")


# STEP 5:
# If the amount is greater than the balance,
# the withdrawal cannot be completed.

else:
    print("Declined. Insufficient funds.")
