# Enter your answers for chapter 7 here
# Name: Alex Choi

import math
# Ex. 7.5

def fact(n):			# Calculates factorial of n
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

def estimate_pi():			# Outputs an estimate of pi based on Ramanujan's method
	k = 0
	while True:
		multiplier = 2*math.sqrt(2)/9801
		top = fact(4*k) * (1103+26390*k)
		bottom = fact(k)**4 * 396**(4*k)
		sum = multiplier * top / bottom		# This is the formula of the right-side of Ramanujan's method
	
		if abs(sum) < 1e-15:
			break
		else:
			k = k + 1

		return 1 / sum

print estimate_pi()


# How many iterations does it take to converge?
# When I added k to the return statement in line 24, I got "1". Is this the right answer?