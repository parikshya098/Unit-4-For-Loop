answer = 0
num1 = int(input('Enter number of cards: '))
total = num1 
for i in range(num1 - 1):
  num1 =int(input('Enter card: '))
  answer += num1
for i in range(total):
  total += i
  i += num1
total -= answer
print("Missing card: {} ".format(total))