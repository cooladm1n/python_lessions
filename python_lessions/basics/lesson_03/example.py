"""
Lesson 03: Loops and Patterns
"""

# Accumulation: sum 1..10
total = 0
for number in range(1, 11):
    total += number
print("sum 1..10:", total)

# Multiplication table 1..5
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    print(row)

# Count evens and sum them
values = [1, 2, 3, 4, 5, 6, 7, 8]
even_count = 0
even_sum = 0
for v in values:
    if v % 2 != 0:
        continue
    even_count += 1
    even_sum += v
print("even_count:", even_count, "even_sum:", even_sum)

# Prime check with for-else
n = 29
is_prime = True
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        is_prime = False
        break
else:
    # if no break occurred
    pass
print(n, "prime?", is_prime)

# Enumerate and zip
lines = ["alpha", "beta", "gamma"]
for idx, line in enumerate(lines, start=1):
    print(f"{idx}: {line}")

xs = [1, 2, 3]
ys = [4, 5, 6]
dot = 0
for x, y in zip(xs, ys):
    dot += x * y
print("dot:", dot)

# Factorial with while
k = 5
fact = 1
while k > 1:
    fact *= k
    k -= 1
print("5! =", fact)
