num = int(input("Enter a number: "))
divisor = 2
while divisor <= num ** 0.5:
    if num % divisor == 0:
        print(f"{num} is not a prime number.")
        break
    divisor += 1
else:
    print(f"{num} is a prime number.")