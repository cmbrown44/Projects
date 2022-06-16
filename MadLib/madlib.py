"""
 Python Project MadLib by Charlie Brown
MadLibs with string concatenation

Github: cmbrown44

"""
def madlib():
    adj1 = input("Adjective: ")
    adj2= input("Adjective: ")
    adj3= input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")

    madlib = f"My name is {noun1 } {noun2 } {noun3 }, commander of the Armies of the North, General of the Felix Legions, " \
         f"{adj1} servant to the true emperor, {noun4 }{noun5 }. Father to a {adj2} son, husband to a {adj3} wife. " \
         f"And I will have my vengeance, in this life or the next. "

    print(madlib)

madlib()



