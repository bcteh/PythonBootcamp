#functions with parameters
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Alice")
# greet("Bob")

# #function with multiple parameters
# def add(a, b):
#     return a + b
# result = add(5, 3)
# print(f"The sum of 5 and 3 is: {result}")

# #function with default parameter
# def greet(name="Guest"):
#     print(f"Hello, {name}!")    
# greet()
# greet("Alice")
# greet("Bob")

#args and kwargs
# def print_args(*args):
#     print("Positional arguments:", args)
# def print_kwargs(**kwargs):
#     print("Keyword arguments:", kwargs)
# def print_all(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# print_args(1, 2, 3)
# print_kwargs(name="Alice", age=30)  
# print_all(1, 2, 3, name="Alice", age=30)

#complex function with args and kwargs
# def complex_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# complex_function(1, 2, 3, name="Alice", age=30)


#Exercise
#prime number check function
def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def list_primes(up_to):
    primes = [] 
    for count in range(2, up_to + 1):
        if is_prime(count):
            primes.append(count)
    return primes   
   

#prime number check using function
num = int(input("Enter a number : "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:    print(f"{num} is not a prime number.")

#prime number up to which number using function
num = int(input("Find a prime number up to which number: "))
primes = list_primes(num)
print(f"Prime numbers up to {num}: {primes}")



def print_all(*args):
    print("Positional arguments:", {args})
print_all(list_primes(num))
