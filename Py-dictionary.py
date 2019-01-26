
print("Py Dictionary")
level = input ("What do you want to do understand? (general Terms) ")
level = level.lower()


def gen_terms():
    knowledge = input("Do you want see the table of contents?(Highly Suggested) ")
    knowledge = knowledge.lower()
    gen_terms =  [">>>","abs","argument","argparse","assert","assignment","block","break","class","compiler","continue","if","else","elif",
                    "def","dictionary","distutils","__future__", "easy_install","exceptions","filter","float","for","if","import","int","lambda","list","map"
                    "object", "pass","reduce","set","setuptools","slice","str","string","try","tuple","while","with","yield"]
    if knowledge == "yes":
        print ("Cool! Hello, what do you want to learn today?")
        print (gen_terms)
        term = input()
        term = help(term)
        print (term)
    else:
        term = input("")
        help(term)
if level == "general term" or "general terms":
    gen_terms()
    