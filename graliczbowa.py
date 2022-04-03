# Gra liczbowa
# from random import randint, w tej instrukcji nie trzeba dawać random.randint tylko samo randint wystarczy

import random

print("Witaj w grze liczbowej")
print("\nCzy wybrane przez ciebie liczny będą trafne ?")
liczba1 = random.randint(1,49)
liczba2 = random.randint(1,49)
liczba3 = random.randint(1,49)
liczba4 = random.randint(1,49)
liczba5 = random.randint(1,49)
liczba6 = random.randint(1,49)

print("Podaj 6 liczb z zakresu od 1 do 49")
l1uzytkownik = int(input("Liczba 1: "))
while (l1uzytkownik > 49) or (l1uzytkownik < 1):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l1uzytkownik = int(input("liczba 1: "))
l2uzytkownik = int(input("Liczba 2:"))
while (l2uzytkownik > 49) or (l2uzytkownik < 1) or (l2uzytkownik == l1uzytkownik):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l2uzytkownik = int(input("liczba 2: "))
l3uzytkownik = int(input("Liczba 3:"))
while (l3uzytkownik > 49) or (l3uzytkownik < 1) or (l3uzytkownik == l2uzytkownik) or (l3uzytkownik == l1uzytkownik):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l3uzytkownik = int(input("liczba 3: "))
l4uzytkownik = int(input("Liczba 4:"))
while (l4uzytkownik > 49) or (l4uzytkownik < 1) or (l4uzytkownik == l2uzytkownik) or (l4uzytkownik == l1uzytkownik) \
        or (l4uzytkownik == l3uzytkownik):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l4uzytkownik = int(input("liczba 4: "))
l5uzytkownik = int(input("Liczba 5:"))
while (l5uzytkownik > 49) or (l5uzytkownik < 1) or (l5uzytkownik == l2uzytkownik) or (l5uzytkownik == l1uzytkownik) \
        or (l5uzytkownik == l3uzytkownik) or (l5uzytkownik == l4uzytkownik):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l5uzytkownik = int(input("liczba 5: "))
l6uzytkownik = int(input("Liczba 6:"))
while (l6uzytkownik > 49) or (l6uzytkownik < 1) or (l6uzytkownik == l2uzytkownik) or (l6uzytkownik == l1uzytkownik) \
        or (l6uzytkownik == l3uzytkownik) or (l6uzytkownik == l4uzytkownik) or(l6uzytkownik == l5uzytkownik):
    print("Błędna liczba, podaj nową z zakresu od 1 do 49")
    l6uzytkownik = int(input("liczba 6: "))

print("Wylosowane liczby to: ", liczba1, liczba2, liczba3, liczba4, liczba5, liczba6)
print("Twoje liczby to: ", l1uzytkownik, l2uzytkownik, l3uzytkownik, l4uzytkownik, l5uzytkownik, l6uzytkownik)

komputer = (liczba1, liczba2, liczba3, liczba4, liczba5, liczba6)
uzytkownik =(l1uzytkownik, l2uzytkownik, l3uzytkownik, l4uzytkownik, l5uzytkownik, l6uzytkownik)
trafienia = set(komputer) & set(uzytkownik)
ilość_trafien = len(trafienia)

if komputer == uzytkownik:
    print("\nTrafiłeś '6' ! Wygrywasz miliony")
else:
    print("\nTrafiłeś:", ilość_trafien)

if ilość_trafien > 0:
    print("\nLiczby wspólne: ", trafienia)
else:
    print("\nPróbuj dalej. Powodzenia ! ")

input("\nNaciśnij enter aby zakończyć program ")
