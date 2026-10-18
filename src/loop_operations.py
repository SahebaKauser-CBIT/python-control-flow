number = int(input("Enter a number for multiplication table: "))

print(f"\nMultiplication Table of {number}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

n = int(input("\nEnter N to calculate the sum: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    print(f"Sum of first {n} natural numbers = {total}")

rows = int(input("\nEnter the number of triangle rows: "))

if rows < 1:
    print("Please enter a positive number of rows.")
else:
    print("\nRight-Angled Triangle:")
    for i in range(1, rows + 1):
        print("*" * i)