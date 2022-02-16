n = int(input("Enter a number: "))
a = 0
b = 1

for x in range (n):
  a = (a * 10) + b
  b = b + 1

  print(a)