num = int(input("Enter N: "))

if num > 1:
    for i in range(2, int(num/2)+1):
       if (num % i) == 0:
        print('COMPOSITE')
        break
    else:
        print('PRIME') 
else:
    print('COMPOSITE')