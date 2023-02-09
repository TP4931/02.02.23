from random import randint

a = [randint(-1000, -1) for i in range(randint(5, 20))]
m = a[0]

for i in range(len(a)):
    if a[i] > m:
        m = a[i]
print(m, a)

# if x>y:
#     m=x
# else:
#     m=y
#
# z = randint(1, 100)
#
# if z>m:
#     m=z
#
# d = randint(1, 100)
#
# if d > m:
#     m = d

