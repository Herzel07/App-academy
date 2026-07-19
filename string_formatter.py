first_name = input("users first name")
last_name = input("users last name")
short_bio = input("bio: ")
username = f"{first_name[0]} {last_name}"
print(f"{username.lower()}")
full_name = first_name + " " + last_name
print(full_name.title())
bio = (short_bio.strip())
no_of_characters = (len(short_bio.strip()))
updated_bio = bio.replace("I am", "I'm")
print(f"{full_name.title()} {updated_bio}{no_of_characters}")

