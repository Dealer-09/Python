import random          
random_num=random.randint(1, 100) #Generate a random number
while True:
  try:    #user inputs a valid number
    guess_num=int(input("Guess the number between 1 and 100"))
    if guess_num < random_num:       #main logic
      print("Too low!") 
    elif guess_num > random_num:
      print("Too high!") 
    else: 
      print("You guessed the number")
      break
  except ValueError:    #If invalid number print error
    print("Please enter a valid number")