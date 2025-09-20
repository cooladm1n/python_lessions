# Lesson 05: Collections and Comprehensions

In this lesson you will learn:
- Lists, tuples, sets, dictionaries: creation, mutation, methods
- Slicing and copying lists; pitfalls with nested lists
- Comprehensions with conditions and transformations
- Sorting with `key`, multi-key sorting with tuples
- Unpacking and the splat operators `*` and `**`

Patterns:
- Use list comprehensions for clarity when transforming sequences.
- Prefer tuples for fixed-size records; sets for membership tests.
- For stable deterministic order after deduplication, use dict from keys.

Exercises:
1) Build a list of squares 1..20 using a comprehension and filter evens.
2) From a list of words, build a dict {word: len(word)} using a comprehension.
3) Remove duplicates while preserving order (dict or seen-set).
4) Sort a list of dicts by multiple keys (e.g., age asc, name asc).
5) Flatten a nested list `[[1,2],[3,4]]` into `[1,2,3,4]` using a comprehension.
6) Use tuple unpacking to swap variables and unpack nested structures.
7) Use a set to compute unique words from text, case-insensitive.
8) Demonstrate shallow vs deep copy on nested lists (`copy` vs `deepcopy`).
