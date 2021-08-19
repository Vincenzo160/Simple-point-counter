# init
import random
version = "1.1.3"
add = 1
A_Point = '0'
B_Point = '0'
print("Version:", version)
input = ""

# functions
# hel = help
# exit = exit
def hel(input):
    if input == "help":
        print("")
        print("Add --[argument]")
        print("")
        print("Choose the section that interests you")
        print("--add_point = Guide to adding points")
        print("--remove_point = Guide to remove points")
        print("--random Guide to randomize the score")
        print("")
    
    if input == "help --add_point":
        print("")
        print("Add points")
        print("")
        print("To add a point to a team, type the letter assigned to the team")
        print("")
        print("EXAMPLE")
        print("a")
        print("")
    
    if input == 'help --remove_point':
        print("")
        print("Remove points")
        print("")
        print("To remove a point from a team, type the letter assigned to the team followed by a -")
        print("")
        print("EXAMPLE")
        print("b-")
        print("")

    if input == 'help --random':
        print("")
        print("Randomize")
        print("")
        print("To randomize the score type random followed by the letter assigned to the team, or just type random to randomize both the team")
        print("")
        print("EXAMPLE")
        print("random")
        print("")
    
    if input == 'help --reset':
        print("")
        print("Reset the score")
        print("")
        print("To reset the score, type reset followed by the letter assigned to the team, or simply type reset to randomize reset teams")
        print("")
        print("EXAMPLE")
        print("resetb")
        print("")
def exi():
        print("Exting...")
        exit(0)

# input
while True:
    input = '0'
    del(input)
    print('A=', A_Point, 'B=', B_Point)
    input = input('> ')
    # input check
    # help
    if input == "help" or input == "help --add_point" or input == "help --remove_point" or input == "help --exit" or input == "help --random" or input == "help --reset":
        hel(input)
        continue
    # adding
    if input == "a" or input == "A":
        A_Point = float(A_Point) + float(1)
        continue
    if input == "b" or input == "B":
        B_Point = float(B_Point) + float(1)
        continue
    if input == "ab" or input == "AB":
        A_Point = float(A_Point) + float(1)
        B_Point = float(B_Point) + float(1)
        continue
    # removing
    if input == "a-" or input == "A-":
        A_Point = float(A_Point) - float(1)
        continue
    if input == "b-" or input == "B-":
        B_Point = float(B_Point) - float(1)
        continue
    if input == "ab-" or input == "AB-":
        A_Point = float(A_Point) - float(1)
        B_Point = float(B_Point) - float(1)
        continue
    # random
    if input == "random":
        A_Point = float(random.randint(int(1), int(100)))
        B_Point = float(random.randint(int(1), int(100)))
        continue
    if input == "randoma" or input == "randomA":
        A_Point = float(random.randint(int(1), int(100)))
        continue
    if input == "randomb" or input == "randomB":
        B_Point = float(random.randint(int(1), int(100)))
        continue
    # reset
    if input == "reset":
        B_Point = float(0)
        A_Point = float(0)
        continue
    if input == "reseta" or input == "resetA":
        A_Point = float(0)
        continue
    if input == "resetb" or input == "resetB":
        B_Point = float(0)
        continue
    # return
    if input == "":
        continue
    # exit
    if input == "exit":
        print("Exting...")
        exit(0)
    # incorrect
    else:
        print("Incorrect command, type help for information on using the software or visit https://github.com/Vincenzo160/Simple-point-counter/wiki to visit the official wiki")
    