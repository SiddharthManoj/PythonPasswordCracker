#For testing purposes only passwords that have one letter/number will be cracked
import os
import hashlib
import md5
allPossibleChars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@')
def convert(i, key) :
	testpass = ""
	if(i == 0):
		testpass = 'a'
	else:
		while i % 63 > 0 :
			testpass = testpass + allPossibleChars[(int)(i % 63)];
			i /= 63;
	m = hashlib.md5()													# Gets the md5 hash
	m.update(testpass)
	print testpass
	if(m.hexdigest() == key):											# Checks the md5 hash with the key from the text file
		print "This is the password: " + testpass + "\nAnd this was the md5 hash cross-referenced: " + m.hexdigest()
		return True
	return False
	
	
def bruteForce(key):
	limit = 8
	i = 0
	while True:
		if(convert(i,key) == True):
			print "Password Found: Success"
			break
		i+=1
		if (i == 63 ** limit):
			print "Password Found: Failure"
			break
			
			
passwordfile = open("cracks.txt", "r")
passwords = []
for line in passwordfile.readlines():
	line = line.strip('\n')
	passwords.append(line)
    
passwordfile.close()
bruteForce(passwords[2])					#Change the number indexed to pick which password to search for (e.g. 2 will try to find "God"'s md5 hash)



