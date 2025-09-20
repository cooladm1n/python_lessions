"""
Lesson 05: Collections and Comprehensions
"""

numbers = list(range(1, 21))
squares = [n * n for n in numbers]
even_squares = [n * n for n in numbers if n % 2 == 0]

words = ["apple", "Banana", "apple", "cherry", "banana"]
lengths = {w: len(w) for w in words}

# Deduplicate preserving first occurrence
seen = set()
unique_preserving = [w for w in words if not (w.lower() in seen or seen.add(w.lower()))]

# Sort by multiple keys: casefolded word then length
sorted_words = sorted(unique_preserving, key=lambda w: (w.casefold(), len(w)))

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [x for sub in nested for x in sub]

# Tuple unpacking
point = (10, 20)
x, y = point

# Copy pitfalls
nested_list = [[1, 2], [3, 4]]
shallow = list(nested_list)
shallow[0][0] = 99  # affects nested_list too

import copy
deep = copy.deepcopy(nested_list)
deep[1][1] = 77

# Sets for unique words (case-insensitive)
unique_words = {w.lower() for w in words}

print("squares:", squares[:10], "...")
print("even_squares:", even_squares[:10], "...")
print("lengths:", lengths)
print("unique_preserving:", unique_preserving)
print("sorted_words:", sorted_words)
print("flattened:", flattened)
print("unpacked:", x, y)
print("nested_list after shallow change:", nested_list)
print("deep copy:", deep)
print("unique_words:", sorted(unique_words))
