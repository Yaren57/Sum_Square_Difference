A = 0
for i in range(1001):
    x = pow(i, 2)
    A = A + x
print("The sum of the squares of the first ten natural numbers is", A)

b = 0
for i in range(1001):
    y = i
    b = b +y
B = b*b
print("The square of the sum of the first ten natural numbers is", B)

sonuc = B - A
print(sonuc)