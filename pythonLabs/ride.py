height = int(input("WHat is your height (cm)?"))
credits = int(input("How many credits do you have?"))
if height >= 137 and credits >= 10:
  print("enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You're too short.")
elif height >= 137 and credits < 10:
  print("you're too poor.")
else:
  print("Not only are you too poor, you are too short. Get outof my sight before I demolish you and scatter your atoms across the cosmos.")