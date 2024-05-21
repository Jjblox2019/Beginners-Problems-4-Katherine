1. 
for attempt in range(3):
    password = input("Enter Password: ")
    if password == "Kobus":
        print("Correct Password")
        break
else:
    print("Locked")
2. 
number = int(input("Choose a number = "))
name = input("What is your name = ")

for _ in range(number):
    print(name)

3.
while True:
    number = int(input("Enter a positive interger"))
    if number <= 0:
        print("Not a positve integer")
    else:
        break

print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
4.
number = int(input("Enter an integer: "))

if number <= 1 :
    print("Not a prime number")
    exit()

is_prime = True
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

my last work that I have done
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
