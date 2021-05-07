import socket
import re
import os
#ask user for input
print("enter a website")
website = raw_input()

#parser for html web page
def parse(data):
	t = '(.+?)'
	matching = re.search(t, data)
	if matching:
		return re.findall(t, data)
#main jelly of the code
def html_get(url):
	#the site to be scraped. can be either DNS or IP address
	host = url
	#uses port 80 because it is the standard html port
	port = 80
	#create client socket connection
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((host, port))
	#creates and sends request to website for da html sushi
	request = "GET/HTTP/1.1\r\nHost: %s \n\n" %host 
	client.send(request.encode())
	#receive response from website and decode to readable format
	response = client.recv(4096)
	html = response.decode('utf-8')
	#print out the parsed data to terminal
	print(html)
	#opens file and saves the parsed html into it
	file = open("html_save.txt", "w+")
	file.write("%s \r\n" %(parse(html)))
	print("saved")

#runs the jelly
if __name__=='__main__':
	html_get(website)