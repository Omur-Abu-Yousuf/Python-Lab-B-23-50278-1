n = int(input("Enter Number: "))

a = 0
b = 1

while a < n:
    print(a)
    next_num = a + b
    a = b
    b = next_num