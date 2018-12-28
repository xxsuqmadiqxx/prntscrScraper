import sys
import os
import string
import random
import httplib2
import threading 


if len(sys.argv) < 2:sys.exit("\033[37mUsage: python " + sys.argv[0] + " (Number of threads)")

noneWorking = [0, 503, 4939, 4940, 4941, 12003, 5556]
threadAmount = int(sys.argv[1])
alph = string.ascii_uppercase + string.digits + string.ascii_lowercase
diglow = string.digits + string.ascii_lowercase

def createDir():
	if 'images' not in os.listdir():os.mkdir('images')


def scrapePictures():
	while 1:
		h = httplib2.Http('.cache')
		a = random.randint(0,1)
		if a:
			part1 = ''.join([random.choice(alph) for _ in range(3)])
			part2 = ''.join([random.choice(diglow) for _ in range(3)])
			name = part1 + part2
		else:name = ''.join([random.choice(alph) for _ in range(5)])
		url = "http://i.imgur.com/" + name + ".jpg"
		response, content = h.request(url)
		if content[0] == 60 or len(content) in noneWorking: continue#Invalid
		if content[:3] == b'GIF':ex='gif'
		elif content[1:4] == b'PNG':ex='png'
		else:ex='jpg'
		with open('images/{0}.{1}'.format(name,ex), 'wb') as f:
			f.write(content)
		print("[+] Valid: {0}".format(url))

def main():
	createDir()

	for i in range(threadAmount):
		th = threading.Thread(target=scrapePictures,)
		th.start()

if __name__ == '__main__':
	main()
