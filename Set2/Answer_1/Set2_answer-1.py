fibonacci_numbers = [0, 1]

n = int(input("Enter the number of elements:"))

for i in range(2,n):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

print(str(x) for x in fibonacci_numbers)

print(','.join(str(x) for x in fibonacci_numbers))
