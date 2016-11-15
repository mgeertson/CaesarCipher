#!/usr/bin/python

import sys

option = sys.argv[1]


if option == '-e':
	rot = sys.argv[2]
	message = sys.argv[3]
	#print(ord(message))

	for letter in message.lower():
		if ord(letter) == 32:
			sys.stdout.write(chr(32))
		else:
			shiftedLetter = chr(ord(letter) + int(rot))
			if ord(shiftedLetter) >= 123:
				sys.stdout.write(chr(ord(shiftedLetter) - 26))
			else:
				sys.stdout.write(chr(ord(shiftedLetter)))
	print(" ")
		
elif option == '-d':
	message = sys.argv[2]

	for counter in range(26):
		print("Shifting by: " + str(counter))
		for letter in message.lower():
			shiftedLetter = chr(ord(letter) + counter)
			if ord(shiftedLetter) < 64:
				sys.stdout.write(chr(32))
			elif ord(shiftedLetter) >= 123:
				sys.stdout.write(chr(ord(shiftedLetter) - 26))
			else:
				sys.stdout.write(chr(ord(shiftedLetter)))
		print("\n")

else:
	print("Invalid Option")
