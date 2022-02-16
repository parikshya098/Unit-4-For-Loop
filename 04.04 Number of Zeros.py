x = int(input('Enter N: '))
count = 0
for i in range(x):
    a = int(input('Enter number: '))
    if (a == 0):
        count = count + 1

print("Number of zeros:",count)