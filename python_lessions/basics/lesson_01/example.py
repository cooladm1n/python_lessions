"""
Lesson 01: Getting Started with Python
- Variables and basic types
- Arithmetic and formatting
- Type conversions and quick debugging
"""

# Naming and basic values
PROJECT_NAME = "Python Lessons"
lesson_number = 1
width = 5
height = 2
pi = 3.14159

# Arithmetic
area_rect = width * height
perimeter_rect = 2 * (width + height)

radius = 4
area_circle = pi * (radius ** 2)

# Division differences
seven_over_two = 7 / 2     # float division -> 3.5
seven_div_two = 7 // 2     # floor division -> 3
neg_div = -7 // 2          # floor division with negatives -> -4
mod_example = 17 % 5       # remainder -> 2
power_example = 2 ** 10    # 1024

# Strings and formatting
first_name = "Alice"
age = 20

print(f"Welcome to {PROJECT_NAME}!")
print("Lesson:", lesson_number)
print(f"Rectangle area={area_rect}, perimeter={perimeter_rect}")
print(f"Circle area (r={radius}) = {area_circle:.3f}")
print(f"7/2={seven_over_two}, 7//2={seven_div_two}, -7//2={neg_div}")
print(f"17%5={mod_example}, 2**10={power_example}")
print(f"Hello, {first_name}. You are {age} years old.")
print("format(): Hello, {}. You are {} years old.".format(first_name, age))

# Type conversions
as_int = int("42")
as_float = float("42.5")
as_str = str(999)
as_bool_1 = bool(0)      # False
as_bool_2 = bool("0")    # True (non-empty string is truthy)

print("int('42'):", as_int, type(as_int))
print("float('42.5'):", as_float, type(as_float))
print("str(999):", as_str, type(as_str))
print("bool(0):", as_bool_1, "bool('0'):", as_bool_2)

# Quick sanity checks with type()
print("type examples:", type(1), type(3.14), type("hi"), type(True), type(None))

# Mini challenge (non-interactive): compute subtotal and tax
price = 19.99
qty = 3
subtotal = price * qty
TAX_RATE = 0.2
with_tax = subtotal * (1 + TAX_RATE)
print(f"subtotal=${subtotal:.2f}, with tax=${with_tax:.2f}")
