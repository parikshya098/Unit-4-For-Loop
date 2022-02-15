n = int(input("Enter a number: "))
x = 0
lst = []

for x in range (n):
  x +=1
  lst.append(x)
  print(''.join([str(x) for x in lst]))