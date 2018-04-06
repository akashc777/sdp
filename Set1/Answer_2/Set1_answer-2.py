n = int(input('Enter a three digit integer: '))
temp = n
result = 0
while temp != 0:
    remainder = temp % 10
    result += remainder ** 3
    temp //= 10

print(result)
if n == result:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
