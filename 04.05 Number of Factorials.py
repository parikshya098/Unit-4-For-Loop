num1 = (int(input("Enter an integer: ")))
f = 1
Sum = 0

for i in range(1, num1 + 1):
    f = f * i
    Sum += f
print(Sum)