
"""
Fibonacci-Folge, hier mit zwei Variablen p und s,
die sich abwechselnd um die jeweiligen Summen erhöhen;
die ersten beiden Werte werden dabei erstmal nur gesetzt;
die Anzahl an Ausgaben ist in diesem Beispiel die doppelte Anzahl
der Schritte zu i, zzgl. der beiden Startwerte
(also: output-count = 2 * step-count + 2)
"""

p = 0
s = 1
print(p)
print(s)
for i in range(0, 10):
    p += s
    print(p)
    s += p
    print(s)
print()
