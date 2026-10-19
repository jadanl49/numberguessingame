import random

#select a random number between 1-10
random_var1 = random.randint(1, 10)
print(f"Random Integer: {random_var1}")

#while input that accepts arguments and breaks when the correct answer is given
for i in range(1):
    incorrect_list = []
    z = int(input("What did you guess?"))
    while True:
        if z == random_var1:
            print("you guessed right!")
            
            break
        else:
            print("wrong answer")
            incorrect_list.append(1)
            if z > random_var1:
                print("a bit lower")
                break
            
            if z < random_var1:
                print("a bit higher")
                break
            



#var == random number 
#tells if input is less or greater

#make list of wrong guesses




