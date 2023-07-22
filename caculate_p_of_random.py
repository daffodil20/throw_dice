import random
a = 0
b = 0
c = 0
d = 0
f = 0
e = 0
for i in range(0,10000):
    dice = [1,2,3,4,5,6]
    user = random.choice(dice)
    if user == 1:
        a += 1
    if user == 2:
        b += 1
    if user == 3:
        c += 1
    if user == 4:
        d += 1
    if user == 5:
        e += 1
    if user == 6:
        f += 1
    p1 = a/10000
    p2 = b/10000
    p3 = c/10000
    p4 = d/10000
    p5 = e/10000
    p6 = f/10000
print(p1,p2,p3,p4,p5,p6)