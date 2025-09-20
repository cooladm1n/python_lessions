"""
Lesson 07: Exceptions
"""

class NegativeAmountError(ValueError):
    pass

def safe_div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

# EAFP example: try then handle
for denom in [2, 0, 5]:
    try:
        print("10/", denom, "=", safe_div(10, denom))
    except ZeroDivisionError as e:
        print("error:", e)

# LBYL example: check before acting
nums = ["12", "x", "34"]
for s in nums:
    if s.isdigit():
        print(int(s))
    else:
        print("not a number:", s)

# Custom exception usage
balance = 100.0
amount = -5
try:
    if amount < 0:
        raise NegativeAmountError("amount cannot be negative")
    balance += amount
except NegativeAmountError as e:
    print("deposit failed:", e)
finally:
    print("final balance:", balance)
