import sys
from collections import Counter

if len(sys.argv) < 2:
    print("Użycie: python3 top_bledy.py plik.log")
    sys.exit(1)

plik = sys.argv[1]
licznik = Counter()

with open(plik) as f:
    for linia in f:
        if "ERROR" in linia:
            tresc = linia.split(" ", 3)[3].strip()
            licznik[tresc] += 1

for tresc, ile in licznik.most_common():
    print(f"{ile} {tresc}")
