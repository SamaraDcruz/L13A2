num = int(input("Enter a number: "))
is_prime = True

for i in range(2, num):  # Outer loop
    for j in range (2, i):  # Inner loop checks if i is divisible
        if i % j ==0:
            is_prime = False
            break
if num > 1 and is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")