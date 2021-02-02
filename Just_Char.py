# Just P Python Code
# By: Mitchell Russell

import sys
import readchar

def simple_just_P():
	string1 = list(input("Phrase to convert: "))
	temp = ""
	for x in range(0,len(string1)):
		if string1[x].isalpha():
			string1[x] = 'p'
		temp += string1[x]
	string1 = temp
	print(string1)
	
	
def just_P():
	while True:
		typed_key = readchar.readkey()
		if typed_key == 'q' or typed_key == 'Q':
			print("")
			break
		else:
			print('p', end='')
			sys.stdout.flush()
	
def just_char(character):
	while True:
		typed_key = readchar.readkey()
		if typed_key == 'q' or typed_key == 'Q':
			print("")
			break
		else:
			print(str(character), end='')
			sys.stdout.flush()
