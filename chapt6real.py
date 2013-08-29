# Enter your answers for chapter 6 here
# Name: Alex Choi

# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

#1 of 6.6
print middle('bb')
print middle('b')
print middle('')
#When calling the middle function with two/one/zero letters, the output is blank for all three cases.
