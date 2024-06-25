import random #The random module offers a variety of functions to generate random data

top_of_range = input("type a number:")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please type a number larger than 0 next time.')
        quit()
else:
    print('type a number')
    quit()        

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
      user_guess = int(user_guess)
    else:
      print('please type a number only')
      continue

    if user_guess == random_number:
       print("you got it;)")
       break
    elif user_guess > random_number:
          print("your guess were above the number!")
    else:
          print("your guess were below the number!")

print("you got it in" , guesses , "Guesses")
       





