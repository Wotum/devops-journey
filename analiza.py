import sys

plik = sys.argv[1]
bledy = 0

with open(plik) as f:
    for linia in f:
        if "ERROR" in linia:
            bledy += 1

print(f"Błędy w {plik}: {bledy}")
