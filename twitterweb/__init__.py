import os
import requests
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
from datetime import datetime

twitter = "https://www.twitter.com/"

# this will scrape the twitter handle for users
# and returns a list with the names
def getUsersFromUser(tHandle):
	# starts timer for timing purposes
	start_time = datetime.now()
	handle = tHandle
	url = twitter + handle
	handle = handle.lower()

	# makes a requet baswd on the url with the handle to check if exists or not
	request = requests.get(url)

	# checks to see if the user exists
	if(request.status_code != 200):
	    print("Invalid twitter handle, Please try again")
	    return

	# open the url and reads the html
	soup = BeautifulSoup(urlopen(url).read())

	arr = []
	count = 0

	# gets the users and cleans them up and appends them to array arr
	for element in soup.findAll('a'):
	    dataScreenName = element.get('href')
	    if dataScreenName is not None:
	        if dataScreenName.count('/') == 1 and dataScreenName.count('?') < 1:
	            temp = dataScreenName.split("/")[1]
	            if (temp.lower() != handle.lower() and temp != "" and temp != "tos" and temp != "privacy" and temp != "login" and temp != "about" and temp != "signup"):
	                # print temp
	                arr.append(temp.lower())
	                count = count + 1

	# removes duplicates from the list of users
	usersFromHtml = list(set(arr))
	#print usersFromHtml
	return usersFromHtml
