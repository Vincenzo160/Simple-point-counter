version = "1.1.1"
add = 1
A_Point = '0'
B_Point = '0'
print("Version:", version)
while True:
    input = '0'
    del(input)
    print('A=', A_Point, 'B=', B_Point)
    input = input('> ')

    if input == 'help':
        print("")
        print("Add --[argument]")
        print("")
        print("Choose the section that interests you")
        print("--add_point = Guide to adding points")
        print("--remove_point = Guide to remove points")
        print("")
        continue

    if input == 'help --add_point':
        print("")
        print("Add points")
        print("")
        print("To add a point to a team, type the letter assigned to the team")
        print("")
        print("EXAMPLE")
        print("a")
        print("")
        continue

    if input == 'help --remove_point':
        print("")
        print("Remove points")
        print("")
        print("To remove a point from a team, type the letter assigned to the team followed by a -")
        print("")
        print("EXAMPLE")
        print("b-")
        print("")
        continue

    if input == 'help --exit':
        print("")
        print("Exiting")
        print("")
        print("To exit, type exit")
        print("")
        print("EXAMPLE")
        print("exit")
        print("")
        continue


    if input == "A":
        A_Point = float(A_Point) + float(1)
        continue

    if input == "B":
        B_Point = float(B_Point) + float(1)
        continue

    if input == "a":
        A_Point = float(A_Point) + float(1)
        continue

    if input == "b":
        B_Point = float(B_Point) + float(1)
        continue

    if input == "ab":
        B_Point = float(B_Point) + float(1)
        A_Point = float(A_Point) + float(1)
        continue


    if input == "A-":
        A_Point = float(A_Point) - float(1)
        continue

    if input == "B-":
        B_Point = float(B_Point) - float(1)
        continue

    if input == "a-":
        A_Point = float(A_Point) - float(1)
        continue

    if input == "b-":
        B_Point = float(B_Point) - float(1)
        continue

    if input == "ab-":
        B_Point = float(B_Point) - float(1)
        A_Point = float(A_Point) - float(1)
        continue


    if input == "AB":
        B_Point = float(B_Point) + float(1)
        A_Point = float(A_Point) + float(1)
        continue

    if input == "":
        continue

    if input == "exit":
        print ("Exting...")
        exit(0)

    else:
        print("Incorrect command, type help for information on using the software or visit https://github.com/Vincenzo160/Simple-point-counter/wiki to visit the official wiki")

