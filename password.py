#For testing purposes only passwords that have one letter/number will be cracked
import os
import hashlib
import md5
import time
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
	if(m.hexdigest() == key):											# Checks the md5 hash with the key from the text file
		print "This is the password found: " + testpass + "\nAnd this was the md5 hash cross-referenced: " + m.hexdigest()
		return True
	return False
	
	
def bruteForce(key):
	limit = 8
	i = 0
	x = 0
	while True:
		start = time.clock()
		while x < len(key):
			if(convert(i,key[x]) == True):
				print "Password Found: Success"
				break
			i+=1
			if (i == 63 ** limit):
				print "Password Found: Failure"
				break
		elapsed = (time.clock() - start)
		print "{} : {} {} {} ".format("Elapsed time", elapsed, " seconds", "\n")
		x+=1
		i = 0

#main()
passwordfile = open("cracks.txt", "r")
passwords = []
for line in passwordfile.readlines():
	line = line.strip('\n')
	passwords.append(line)
    
passwordfile.close()
bruteForce(passwords)					#passes in md5 hashed passwords



