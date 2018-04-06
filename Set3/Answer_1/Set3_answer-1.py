n = int(input('Enter number of rows: '))
for i in range(1,n+1):

    l = list(range(i,2*i))

    print((n-i)* 2 *' ' + ' '.join(str(x) for x in l ) + ' ' + ' '.join(str(x) for x in l[-2::-1] ))
