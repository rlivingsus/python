#!/usr/bin/python3
import sys
import io
import getpass
import hashlib
import requests
import urllib3

def main():

	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  #surpresses warnings during output
	passw = getpass.getpass("Enter your password: ")
	m = hashlib.sha1(passw.encode()).hexdigest()  #encoding and hashing the password
	up = m.upper()
	prefix = up[0:5] #obtains first 5 chars of hash
	URL = "https://api.pwnedpasswords.com/range/" + prefix
	response = requests.get(URL, verify=False)
	if response:
		res = response.text #all data goes into res
		for line in res.splitlines(): #looping through res by splitlines
			merge = prefix + line
			m = merge[0:40]	#take 1st 40 char of merge
			if (up == m):
				print("PASSWORD BREACHED")
				exit()
		print ("PASSWORD SAFE")
	else:
		print("An error has occurred")

if __name__ == '__main__':
	main()
	print ("run directly")
else:
	print ("run from import")
