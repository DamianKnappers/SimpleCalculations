while True:
    print("A = Gemiddelde berekenen")
    print("B = Bij elkaar optellen")
    print("C = Hoogste getal in een reeks getallen")
    choice = 0
    opt = input("Kies A B of C: ")
    if opt == 'A':
        choice = 1
    elif opt == 'B':
        choice = 2
    elif opt == 'C':
        choice = 3
    else:
        print("Vul een van de 3 opties in om door te gaan, let op hoofdletters")

    if choice == 1:
        print("U heb gekozen voor antwoord A")
        num = int(input("Hoeveel getallen?: "))
        total_sum = 0

        for n in range(num):
            numbers = float(input("Geef nummer: "))
            total_sum += numbers
        avg = total_sum/num
        print("Gemiddelde is :", avg)

    elif choice == 2:
        print("U heb gekozen voor antwoord B")
        i = 0
        som = 0
        num = int(input("Hoeveel getallen wilt u bij elkaar rekenen?: "))

        while i < num:
            getal = int(input("Geef een getal op: "))
            som = som + getal
            i = i + 1
        print("Uitkomst is: ", som)
    elif choice == 3:
        maxn = 0
        print("U heb gekozen voor antwoord C")
        i = 0
        nummers = int(input("Hoeveel nummers?: "))
        while i < nummers:
            getal = int(input("Geef een getal: "))
            i = i + 1
            if maxn < getal :
                maxn = getal
        print("Het hoogste nummer is: ", maxn)

    while True:
        answer = input('Opnieuw het programma draaien (ja/nee): ')
        if answer in ('ja', 'nee'):
            break
        print('Invalid input.')
    if answer == 'ja':
        continue
    else:
        print("Tot ziens")
        break
