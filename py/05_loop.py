
#multiplication table using while loop
count=1
while count <= 12:
    for i in range(1, 13):
        print(count * i, end=' ')
    print()  # Print a newline after each row
    count += 1
print("Done")


#prime number check using while loop
num = int(input("Find a prime number up to which number: "))
count = 2
while count <= num:
    is_prime = True
    divisor = 2
    while divisor <= count ** 0.5:
        if count % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(f"{count}", end=' ')
    count += 1