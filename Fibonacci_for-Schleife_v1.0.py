"""
Fibonacci-Folge, mit drei Variablen k, p und s,
die sich abwechselnd um die jeweiligen Summen erhöhen;
die ersten beiden Werte werden dabei im ersten Durchlauf einfach nur gesetzt
"""

p = 0
s = 1
for i in range(0, 8):
    if i > 0:
        k = p + s
        print(k)
        p = s + k
        print(p)
        s = k + p
        print(s)
    else:
        print(p)
        print(s)
print()
