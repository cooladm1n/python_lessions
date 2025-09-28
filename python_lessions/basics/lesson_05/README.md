# Lesson 05: Collections and Comprehensions

Estimated time: 60-90 minutes

Learning outcomes
- Use lists, tuples, sets, and dicts, and choose correct types for tasks.
- Write comprehensions and use `key` functions for sorting.
- Understand shallow vs deep copy pitfalls.

Acceptance criteria
- Implement `deduplicate_preserve_order(seq)` returning a list without duplicates preserving order.
- Implement a comprehension that maps words to lengths.

Worked example

```py
def deduplicate_preserve_order(seq):
	seen = set()
	out = []
	for x in seq:
		if x not in seen:
			seen.add(x)
			out.append(x)
	return out

words = ["apple", "banana", "apple"]
word_lens = {w: len(w) for w in words}
```

Exercises (mandatory)
1) Implement `deduplicate_preserve_order` and test with repeated elements.
2) Sort list of dicts by multiple keys and write a small test.

Hints & testing
- Test deduplication with different element types and empty lists.
- Use `copy.deepcopy` to illustrate deep vs shallow copies in tests.
