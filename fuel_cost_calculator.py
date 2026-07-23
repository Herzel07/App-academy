distance = float(input("Distance in kilometers: "))
petrol_price = float(input("Price per liter: "))
liters_needed = distance / 10
total_cost = round(liters_needed * petrol_price, 2)
print(f"Total fuel cost: R{total_cost}")
