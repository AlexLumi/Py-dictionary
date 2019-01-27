def gen_terms():
    knowledge = input("Do you want to see the table of contents?(Highly Suggested): ")
    knowledge = knowledge.lower()
    gen_terms =  ["abs","argument","argparse","assert","assignment","block","break","class","compiler","continue","if","else","elif",
                    "def","dictionary","distutils","__future__", "easy_install","exceptions","filter","float","for","if","import","int","lambda","list","map"
                    "object", "pass","reduce","set","setuptools","slice","str","string","try","tuple","while","with","yield"]
    if knowledge == "yes" or "yea":
        print (gen_terms)
        print (" ")
        print ("Cool! Hello, what do you want to learn today?")
        term = input()
        term = help(term)
        print (term)
        if term not in gen_terms:
            print("You might want to get the table of contents because what you chose is not in the list")
#--------------------------------------------------------------------------------------------------------------

def strings():
    knowledge = input("Do you want to see the table of contents? (Highly Suggested): ")
    knowledge = knowledge.lower()
    string_dict = {"capitalize": "Capitalizes first letter of string", 
                    "islower":"Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise", 
                    "isnumeric":"Returns true if a uncode string contains only numeric characters and false otherwise",
                    "isspace":"Returns true if string contains only whitespace characters and false otherwise",
                    "istitle": "Returns true if string is properly 'titlecased' and false otherwise",
                    "len": "Returns the length of the string",
                    "lower": "Converts all uppercase letters in string to lowercase",
                    "strip": "Removes space on the left and right of the sting",
                    "max":"Returns the max alphabetical character from the string str",
                    "min": "Returns the min alphabetical character from the string str",
                    "title": "Returns 'titlecased' version of string, that is, all words begin with uppercase and the rest are lowercase ",
                    "upper": "Converts lowercase letters in string to uppercase"} 

    if knowledge == "yes" or "yea":
        string_list = []
        for i in string_dict.keys():
            string_list.append(i)
        print (string_list)
        print(" ")
        input("Press Enter")
        print(" ")
        choose = input("Which one of those do you want to learn about: ")
        choose = choose.lower()
        if choose in string_dict:
            print(" ")
            print ( choose + ": "  + string_dict.get(choose))

#---------------------------------------------------------------------------------------------------
def exerises():
    print ("There are 5 exerises for you to test your skills.")
    input ("Press Enter")
    print (" ")
    num = input("If you don't mind me asking? What excerises were you on if you are returning: ")
    if int(num) == 1:
        print ("Insert the missing part of the code needed to output 'Hello World': ")
        x = 0
        while x < 10:
            answer = input()
            if str(answer) == "print":
                print ("Correct")
                x = 10
            else:
                print("Try Again")
                x = x + 1
    num = int(num) + 1
    if int(num) == 2:
        print("Comments in Python are written with a special character, which one? ")
        x = 0
        while x < 10:
            answer = input()
            if str(answer) == "#":
                print ("Correct")
                x = 10
            else:
                print ("Try Again")
                x = x + 1
    num = num + 1
    if int(num) == 3:
        print ("Create a variable named x and assign the value 50 to it. ")
        x = 0
        while x < 10:
            answer = input()
            if str(answer) == "x = 50" or "x=50":
                print ("Correct")
                x = 10
            else:
                print ("Try Again")
                x = x + 1
    num = num + 1
    if int(num) == 4:
        print ("Use the 'len' method to print the length of the string. (x = 'Hello World') ")
        x = 0
        while x < 10:
            answer = input()
            if str(answer) == "print(len(x))" or "print (len(x))":
                print ("Correct")
                x = 10
            else:
                print ("Try Again")
                x = x + 1
    num = num + 1
    if int(num) == 5:
        print ("Convert the value of 'txt' to upper case. (txt = 'Hello World') ")
        print ("txt = ____________")
        x = 0
        while x < 10:
            answer = input()
            if str(answer) == "txt.upper()":
                print ("Correct")
                x = 10
            else:
                print ("Try Again")
                x = x + 1
    num = num + 1
    if int(num) == 6:
        print ("Congrats! You completed all the exercises.") 
                

#----------------------------- Beginning ------------------------------------------------------------

print("Py Dictionary")
print(" ")
print ("What do you want to do understand or do? (General Terms, Strings, Exerises): ")
level = input()
level = level.lower()

if str(level) == "general terms":
    gen_terms()
if str(level) == "strings":
    strings()
if str(level) == "exerises":
    exerises()