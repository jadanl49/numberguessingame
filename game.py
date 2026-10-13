import random

#select a random number between 1-10
random_var1 = random.randint(1, 10)
print(f"Random Integer: {random_var1}")

#while input that accepts arguments and breaks when the correct answer is given
for i in range(1):
    z = int(input("What did you guess?"))
    while True:
        if z != random_var1:
           print("wrong answer")
"""     while z != random_var1: 
        print("wrong answer")
    
    if z == random_var1:
      print("You guessed right!") """
    


#var == random number 
#tells if input is less or greater

#make list of wrong guesses
