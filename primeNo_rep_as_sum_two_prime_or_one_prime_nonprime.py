# take input
Number = int(input('Enter the Number : '))
# initialize an array
# Prime array
arr = []
# find prime numbers
for i in range(2, Number):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    # append prime numbers to array
    if flag == 0:
        arr.append(i)

# Non prime array
arr2 = [i for i in range(Number+1) if i not in arr]

f = 0
# possible combinations prime and non prime
for a in arr:
    for b in arr2:
    # if condition is True Print numbers
        if (a + b) == Number:
            f = 1
            print(str(str(a) + " and " + str(b)) + ' are one prime and one non prime numbers when added gives ' + str(Number))
            break
    if (a + b) == Number:
        break
    
for i in arr:
    for j in arr:
    # if condition is True Print numbers
        if i + j == Number:
            f = f + 1
            print(str(str(i) + " and " + str(j)) + ' are prime numbers when added gives ' + str(Number))
            break
    if (i + j) == Number:
        break       

if f == 2:
    print('Yes')
else:
    print('No')