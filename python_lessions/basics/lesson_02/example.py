"""
Lesson 02: Conditions and Boolean Logic
"""

n = 42

# Basic branching
a = n
if a > 0:
    kind = "positive"
elif a < 0:
    kind = "negative"
else:
    kind = "zero"

# Even check and boolean algebra
is_even = (a % 2 == 0)

# Chained comparison and guard clauses
x = 75
if not (0 <= x <= 100):
    print("x out of expected range [0,100]")
else:
    print("x is within range")

# Conditional expression (ternary)
age = 17
status = "adult" if age >= 18 else "minor"

print(f"n={n} is {kind}; even={is_even}; status={status}")

# De Morgan demonstration
p = True
q = False
left = not (p and q)
right = (not p) or (not q)
print("De Morgan equality:", left == right)

# Leap year check
year = 2000
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(year, "leap?", is_leap)

# Guarded division
numerator = 10
denominator = 0
if denominator == 0:
    print("Cannot divide by zero")
else:
    print("result:", numerator / denominator)
