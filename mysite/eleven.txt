print("This game is easy, all you have to do is to supply a number between 1 and 4.")
print("The number you choose will be accumulated into a total and the first one to eleven WINS!!!")
print("")
print("Do you want to play? (Yes/No): ")
start = input()
while start == "Yes" or "No":
    if start == "Yes":
        print("Let's play!")
        break
    elif start == "No":
        exit()
    else:
        print("Error - Invalid answer. Try again (Yes/No): ")
        start = input()
print("What dificulty do you want? (Easy/Medium/Hard)")
dif = input()
while dif == "Easy" or "Medium" or "Hard":
    if dif == "Easy":
        print("Do you want to play it Easy? Okay then.")
        break
    elif dif == "Medium":
        print("Medium? You are respectable.")
        break
    elif dif == "Hard":
        print("Ha ha ha! You don't stand a chance!")
        break
    else:
        print("Error - Invalid answer. Try again (Easy/Medium/Hard): ")
        dif = input()
print("Do you want to go first? (Yes/No)")
first = input()
while first == "Yes" or "No":
    if first == "Yes":
        print("You start!")
        break
    elif first == "No":
        break
    else:
        print("Error - Invalid answer. Try again (Yes/No): ")
        first = input()
while dif == "Easy":
    if first == "Yes":
        print("(1/2/3/4)")
        choice = input()
        while 0 < choice < 5:
            if choice