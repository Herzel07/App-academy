secret_password = input("password ") 
clean_password = (secret_password.strip())
secret_password = (clean_password[0] + clean_password[-1])
print(f"Your password hint:{secret_password.upper()}")
