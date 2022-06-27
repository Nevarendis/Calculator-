print("Witaj w moim kalkulatorze")

print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")
p = int(input("Podaj pierwszą liczbę: "))
r = int(input("Podaj drugą liczbę: "))
e= input("Wybierz działanie: ")

if e == "1":
    e = p+r
elif e == "2":
    e = p-r
elif e == "3":
    e = p*r
elif e == "4":
    e = p/r

print(e)
