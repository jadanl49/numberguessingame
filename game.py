import random

#select a random number between 1-10
random_var1 = random.randint(1, 10)
print(f"Random Integer: {random_var1}")
incorrect_list = []
#while input that accepts arguments and breaks when the correct answer is given
z = int(input("What did you guess?"))
while True:  
    if z != random_var1:
        print("wrong answer")
        if z > random_var1:
            print("a bit lower")
            incorrect_list.append(z)
        if z < random_var1:
            print("a bit higher")
            incorrect_list.append(z)
        z = int(input("Guess again!"))

    if z == random_var1:
        print("you guessed right!")
        print("here are your incorrect guesses",incorrect_list)
        break
                
            




#make list of wrong guesses

