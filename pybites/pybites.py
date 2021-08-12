from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

# print(text[1:-1])

# print(text.strip())

# no_white_space = text.strip()
# split_lines = no_white_space.splitlines()
# print(split_lines)

def slice_and_dice(text: str = text) -> list:
# #     """Get a list of words from the passed in text.
# #        See the Bite description for step by step instructions"""

	no_white_space = text.strip()
	split_lines = no_white_space.splitlines()
	# print(split_lines)

	for line in split_lines:
		no_space = line.strip()
		words = no_space.splitlines()
		print(words)

	# results = []
slice_and_dice()

