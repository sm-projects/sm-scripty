# Given a url the following script finds all the links


import requests
import re

# Ask the user to enter a url
url = input("Enter a url (include 'http://): ")

# connect to the url
website = requests.get(url)

# read the page
html = website.text

# Use re.findall to grab all links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# print out all the links
for link in links:
    print(link[0])



