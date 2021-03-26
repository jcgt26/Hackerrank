import random

def guess(x):
    random_number = random.randint(1,x)
    print(random_number)
    done = False
    while(not done):
        number = int(input("Give me the number! "))
        if(number == random_number):
            done = True
            print("That's it")
        elif(number > random_number):
            print("Maybe something lower man.. ")
        else:
            print("I do need something bigger buddy")


if __name__=="__main__":
    guess(25)
