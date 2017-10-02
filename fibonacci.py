#List of Fibonacci Numbers up to N

a = [1,1]

N = input('Enter the number: ')
i = 0
while True:
    if (a[i] + a[i+1]) >= N:
        break
    a.append(a[i] + a[i+1])
    i = i + 1

print a
