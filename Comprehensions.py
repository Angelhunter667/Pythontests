xs = [1, 2, 3, 4, 5]

ys = []
zs = []

for x in xs:
    ys.append(x * x)

print(xs)
print(ys)

for y in ys:
    xs.append(y + x)

print(xs)
print(ys)

for iterable in ys:
    zs.append(iterable + iterable)

print(zs)
