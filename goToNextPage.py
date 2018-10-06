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
url = "https://www.indeed.com/jobs?q=Robotics+Engineer&start=10"
#url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l=Richmond%2C+VA&start=10"
#url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l=Lower+Earth+Orbit" # Suggested for you challenge

food = kitchen(url)

goodLinks = []
badLinks = []
resultsList = []
savedResults = []


# Grab Number of Search Results in a page

numResults = food.find_all('div', {'id':'searchCount'})[0].get_text()
numSearchResults = int(str(re.findall(re.compile('Page[^.]* of (.+?) jobs'), numResults)[0]).replace(',',''))
print("Number of Search Results :", numSearchResults)



nextPageInfo = food.find_all('span', {'pn'})[-1].parent
thereIsNextPage = nextPageInfo.get_text()
if thereIsNextPage[0:4] =="Next":
    nextPageAddress = nextPageInfo.get('href')



#numResults = food.find_all('div', 'resultsTop')


#pageNext = food.find('div', {'pagination'})

#pageNext = food.div['np']
#pageNext2 = 10
#contents = pageNext.contents
'''
for item in pageNext:
    print(item.parent.decode(formatter=None))       # Need to set Decode = none in order to recieve & instead of &amp;
'''
#print(pageNext[-1].parent.decode(formatter=None))


nextPageInfo = food.find_all('span', {'pn'})[-1].parent
thereIsNextPage = nextPageInfo.get_text()
if thereIsNextPage[0:4] =="Next":
    nextPageAddress = nextPageInfo.get('href')
#else:
#    break



print(isThereNextPage)
print(nextPageAddress)

'''
pageNext = food.find_all('span', {'pn'})
nextResultsPageLink = pageNext[-1].parent.get_text()
#print(nextResultsPageLink)


if nextResultsPageLink[0:4] == "Next":
    print("Yes")
else:
    print("No")

nextPageLink = str(food.find_all('span', {'pn'})[-1].parent.get('href')) # Get the link to the next page, convert to string
print(nextPageLink)

'''
'''

nextPageLink = pageNext[-1].parent.decode(formatter=None)

print(nextPageLink)


#for item in contents:
#    print(item)
#print(pageNext.contents[-1])
#print(pageNext2)
'''