version = "1.1.1"
add = 1
A_Point = '0'
B_Point = '0'
print("Versione:", version)
while True:
    input = '0'
    del(input)
    print('A=', A_Point, 'B=', B_Point)
    input = input('> ')

    if input == 'help':
        print("")
        print("Aggiungi --[argomento]")
        print("")
        print("Scegli la sezione che ti interessa")
        print("--add_point = Guida al aggiungere punti")
        print("--remove_point = Guida al rimuovere punti")
        print("--exit Guida al uscita dal programma")
        print("")
        continue

    if input == 'help --add_point':
        print("")
        print("Aggiungere punti")
        print("")
        print("Per aggiugere un punto ad una squadra digita la lettera assegnata alla squadra")
        print("")
        print("ESEMPIO")
        print("a")
        print("")
        continue

    if input == 'help --remove_point':
        print("")
        print("Rimuovere punti")
        print("")
        print("Per rimuovere un punto ad una squadra digita la lettera assegnata alla squadra seguita da un -")
        print("")
        print("ESEMPIO")
        print("b-")
        print("")
        continue

    if input == 'help --exit':
        print("")
        print("Uscire")
        print("")
        print("Per uscire digita exit")
        print("")
        print("ESEMPIO")
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
        print ("Uscita...")
        exit(0)

    else:
        print("Comando errato, digita help per informazioni sul utilizzo del software o visita https://github.com/Vincenzo160/Simple-point-counter/wiki per visitare la wiki ufficiale")

