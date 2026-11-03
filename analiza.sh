#!/bin/bash
PLIK="$1"

echo "Analiza pliku: $PLIK"
echo "Błędy:     $(grep -c ERROR $PLIK)"
echo "Ostrzeżenia: $(grep -c WARNING $PLIK)"
echo "Info:      $(grep -c INFO $PLIK)"
