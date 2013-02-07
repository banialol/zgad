import string
import random

print 'Range from 1 to 10.'
los = random.choice(range(1,11))
a = 1
def enka(a):
  n = int(raw_input('Number: '))
	if n > los:
		a = a + 1
		print 'Lower\n'
		return enka(a)
	elif n < los:
		a = a + 1
		print 'Higher\n'
		return enka(a)
	else:
		print 'You guessed it!', los, '\nFor',a, 'time.\n\n'
enka(a)
