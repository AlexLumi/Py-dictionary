

print("Coding Dictionary")
level = input ("What level of programming are you?: ")
level = level.lower()

def beginner():
    learn = input ("Hello " + level + " What do you want to learn today?")
    learn = learn.strip()
    learn = learn.lower()
    beginner_list =  {"Print": "This will print the string"}
    if learn in beginner_list:
        print (beginner_list.get(learn))

if level == "beginner" or "novice":
    beginner()

