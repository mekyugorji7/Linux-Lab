#!/usr/bin/python3

import sys

if len(sys.argv) == 2:
	key = sys.argv[1]
	message = input()
	message = message.upper()
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	onlyAlpha = ""
	
	for i in range(len(message)):
		if message[i].isalpha():
			onlyAlpha += message[i]
	cipherWord = ""
	for i in range(len(onlyAlpha)):
		index_val = alphabets.index(onlyAlpha[i]) + int(key)
		cipherWord += alphabets[index_val]
	
	count = 0
	newLinecount = 0
	for i in range(len(message)):
		count += 1
		if count == 6:
			cipherWord = cipherWord[:i] + " " + cipherWord[i:]
			count = 0
			newLinecount += 1
			if newLinecount == 10:
				cipherWord = cipherWord[:i]+"\n"+cipherWord[i:]
				newLinecount = 0
				count -= 1
	print(cipherWord)


else:
	print("Usage: python3 mycipher.py 1")


	
