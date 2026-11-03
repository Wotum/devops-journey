imie = "Bartek"
liczba = 3
print(f"Cześć, {imie}. Liczba błędów: {liczba}")
print(type(imie))
print(type(liczba))
cena = 19.99
aktywny = True
print(type(cena))
print(type(aktywny))

bledy = ["Brak połączenia z bazą", "Timeout płatności", "Błąd autoryzacji"]

for blad in bledy:
    print(f"Wykryto: {blad}")
print("Koniec")
