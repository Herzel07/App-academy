name =input("first name: ")
surname = input("surname: ")
age = int(input("age: "))
favorite_number = float(input("favorite number: "))

full_name = name + "" + surname

print(f"Welcome, {full_name}")
print(full_name.upper())
print(full_name.title())

age_in_months = age * 12
print(age_in_months)
