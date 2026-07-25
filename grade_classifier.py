# STEP 1: Ask for the learner's name. 
# We use input()only because a name is text.

learner_name = input("Learner name: ")


# STEP 2: Ask for the three subject marks.
# We use float(input()) because marks are numbers
# and the learner may enter decimal values.
subj1 = float(input("1st subject: "))
subj2 = float(input("2nd subject: "))
subj3 = float(input("3rd subject: "))


# STEP 3: Calculate the average.
# First we add the three marks, 
#then divide the total by 3
# because there are three subjects.
average = (subj1, subj2, subj3) / 3

# STEP 4: Assign the learner's grade.
# Python checks the conditions from top to bottom.
# Once one condition is true, it skips the remaining ones.
if average >= 80:
     grade = "A"
elif average >= 70:
     grade = "B"
elif average >= 60:
     grade = "C"
elif average > >= 50:
     grade = "D"
else:
     grade = "F"

# STEP 5: Assign Pass or Fail status.
# There are only two possible outcomes,
# so we only need if and else.
if average >= 50:
     status = "Pass"

else:
     status = "Fail"

# STEP 6: Create default intervention messages.
# An empty string means there is currently
# no intervention message to display.
intervention1 = " "
intervention2 = " "
intervention3 = " "


# STEP 7: Check each subject separately.
# We use separate if statements because more than one
# subject may need intervention at the same time.
if subj1 < 40:
    intervention1 = "Needs intervention"
if subj2 < 40:
     intervention2 = "Needs intervention"
if subj3 < 40:
    intervention3 = "Needs intervention"

# STEP 8: Display the full report card. 
# Each print() creates one line in the report.
print("\n----- STUDENT REPORT CARD -----")

print(f"Learner: {learner_name}")
print(f"Subject 1: {subj1} {intervention1}")
print(f"Subject 2: {subj2} {intervention2}")
print(f"Subject 3: {intervention3}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")
