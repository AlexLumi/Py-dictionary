print("Py Dictionary")
print(" ")
level = input ("What do you want to do understand or do? (General Terms, Strings): ")
level = level.lower()


def gen_terms():
    knowledge = input("Press Enter")
    check = True
    gen_terms =  ["abs","argument","argparse","assert","assignment","block","break","class","compiler","continue","if","else","elif",
                    "def","dictionary","distutils","__future__", "easy_install","exceptions","filter","float","for","if","import","int","lambda","list","map"
                    "object", "pass","reduce","set","setuptools","slice","str","string","try","tuple","while","with","yield"]
    if check:
        print (gen_terms)
        print (" ")
        print ("Cool! Hello, what do you want to learn today?")
        term = input()
        term = help(term)
        print (term)
        if term not in gen_terms:
            print("You might want to see the table of contents again because what you chose is not in the list")
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
                    "max":"Retruns the max alphabetical character from the string str",
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
if level == "general term" or "general terms":
    gen_terms()
    
elif level =="strings" or "string":
    strings()
    