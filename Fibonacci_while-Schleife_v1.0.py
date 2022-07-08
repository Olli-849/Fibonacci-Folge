"""
Fibonacci-Folge, hier mit zwei Variablen p und s,
die sich abwechselnd um die jeweiligen Summen erhöhen;
die ersten beiden Werte werden dabei erstmal nur gesetzt;
"""

p = 0    # Startzahl 1
s = 1    # Startzahl 2
cnt = 2  # Zähler für die Anzahl
rg = 20  # vorbestimmte (gerade) Anzahl der zu ermittelnden Zahlen
print(p)
print(s)
while cnt < rg:
    cnt += 2
    p += s
    print(p)
    s += p
    print(s)
print()
