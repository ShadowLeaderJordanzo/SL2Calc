def checkName(name): 
    answer = input("Is your name " + name + "? ")

    if answer.lower() == "yes":
        print("Hello,", name)
    else:
        print("we're sorry about that, m'lady")

checkName("Bober")