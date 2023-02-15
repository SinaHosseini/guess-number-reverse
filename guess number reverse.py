import random

user_number = int(input("enter your guess: "))
print("\nfor continue enter\n 1.GO Up\n or\n 2.GO DOWN\n in any level\n")
computer_number = random.randint(0, 50)
print("a random number was selected", computer_number)
tried = 1

while True:

    if computer_number == user_number:
        print("""\tmy guess is correct
        i win🥳""")
        print("i try ", tried, "time")
        break

    elif computer_number > user_number:
        dastor = input("enter go down\n")
        dastor = dastor.lower()
        if dastor == "go down":
            computer_number = random.randint(0, computer_number)
            print("new guess is ", computer_number)
            tried += 1

    elif computer_number < user_number:
        dastor = input("enter go up\n")
        dastor = dastor.lower()
        if dastor == "go up":
            computer_number = random.randint(computer_number, 50)
            print("new guess is ", computer_number)

            tried += 1


print("well done")
