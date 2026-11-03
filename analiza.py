import sys

if len(sys.argv) < 2:
    print("Użycie: python3 analiza.py plik.log")
    sys.exit(1)

plik = sys.argv[1]
licznik = {"ERROR": 0, "WARNING": 0, "INFO": 0}

with open(plik) as f:
    for linia in f:
        for poziom in licznik:
            if poziom in linia:
                licznik[poziom] += 1

print(f"Analiza pliku: {plik}")
for poziom, ile in licznik.items():
    print(f"{poziom}: {ile}")
