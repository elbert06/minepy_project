a = input()
m = 0
s = len(a)
a = a.lower()
for h in a:
    s -= 1
    m += (ord(h)-64) * (26 ** s)
print(m)