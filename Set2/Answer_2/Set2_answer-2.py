n = int(input('Enter number of rows: '))
for i in range(0,n):
    print(i * '  ' + (2*(n-i)-1) * '* ')
