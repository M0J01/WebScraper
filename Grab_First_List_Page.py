from bs4 import BeautifulSoup
import requests
import time
import re

print("Herr otto")


STEM = "https://indeed.com"

"""
Takes in  : a URL
Spits out : a beautiful soup object
"""
def kitchen(address):
    r = requests.get(address)
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    return soup

# -------- Baby Garden (Seeds) -------
url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l="
#url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l=California&ts=1538086172806&rq=1&fromage=last" \

food = kitchen(url)

goodLinks = []
badLinks = []
resultsList = []
savedResults = []



# Grab Number of Search Results in a page
#print(food.prettify())


# ------- Grab all of the links
for link in food.find_all('a'):
    name = link.get('href')
    try:
        if ("/pagead" in name) or ("/rc/" in name):
            #print("Good Link :")
            #print(name)
            goodLinks.append(name)
        #elif "/rc/" in name:
            #print("Good Link :")
            #print(name)
        #    goodLinks.append(name)
        else :
            badLinks.append(name)
            #print("Bad Link :")
            print(name)
    except:
        None

print(goodLinks)

print(len(goodLinks))
print(len(badLinks))