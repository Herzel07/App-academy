# STEP 1:
# Start an intentional infinite loop.
# This means the program will keep running
# until we use break to stop it.
while True:

# STEP 2:

# Ask the player to enter a score. 
# We use input() only because theuser might type 
# a number or the word "stop".
score = input("Enter your game score or type 'stop' to quit: ")


# STEP 3:
# Clean the user's input before checking it.
# .strip() removes extra spaces.
# .lower() changes the word to lowercase.
#
# This means all of these will work:
# stop
# STOP
# Stop
#   stop
if score.strip().lower() == "stop"

# Tell the player that the sesssion is ending.
print("Game session ended!")


# break stops the while loop completely.
break


# STEP 4:
# If the input was not "stop",
# convert the score from text into an integer.
score = int(score)


# STEP 5:
# Check whether the score is greater than 100.
if score > 100:

# This runs when the score is above 100.
print("Wow! That's a new high score!")


# STEP 6:
# If the score is 100 or below,
# this message will be displayed.
else:
  print("Good try, keep playing!")


