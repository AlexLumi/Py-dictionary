
print("Coding Dictionary")
level = input ("What level of programming are you?: ")
level = level.lower()


def beginner():
    learn = input ("Hello " + level + " what do you want to learn today?")
    learn = learn.strip()
    learn = learn.lower()
    beginner_list =  {"print": "This will print the string"}
    if learn in beginner_list:
        print ( learn.title() + ": " + beginner_list.get(learn))

if level == "beginner" or "novice" or "potato":
    beginner()
    choice = input("Do you want to keep researching in beginner ")
    if choice == "yes" or "yea" or "ya":
        beginner()
    else:
        print("Bye!")

