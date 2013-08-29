# Enter your answers for chapter 6 here
# Name: Alex Choi

# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# 1 of 6.6
print middle('bb')
print middle('b')
print middle('')
# When calling the middle function with two/one/zero letters, the output is blank for all three cases.

# 2 of 6.6

def is_palindrome(word):				# Returns True if word is a palindrome. I have to confess that I peeked at the solution.
	if len(word) <= 1:					# This if statement exists as a "countdown". Once it reaches 1, it means that it has successfully checked the sameness of every pair of letters starting from both ends to the center.
		return True
	if first(word) != last(word):		# If the first and last letters are not the same, then it is not a palindrome.
		return False
	return is_palindrome(middle(word))	# Eliminates the outside letters, then will check the sameness of the next letters in from both ends.

print is_palindrome('odo')
print is_palindrome('hello')
print is_palindrome('racecar')


# Ex 6.8
def gcd(a,b):							# Returns the greatest common divisor of a and b.
	if b == 0:							# This is the base case of gcd(a, 0) = a
		return a
	else:
		return gcd(b, a % b)			# Executes Euclid's algorithm of gcd(a,b) = gcd(b,r). r = a % b



print gcd(100, 80)
print gcd(80,100)


	

