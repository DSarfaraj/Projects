a, b = 0, 1
length = 10
print(a, b, end=' ')
for i in range(length):
    c = a + b
    print(c, end=' ')
    a = b
    b = c