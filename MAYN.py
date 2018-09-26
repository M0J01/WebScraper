from bs4 import BeautifulSoup
import requests
import time

print("Herr otto")


STEM = "https://indeed.com"

"""
Takes in  : a URL
Spits out : a beautiful soup object
"""
def kitchen(address):
    r = requests.get(address)
    data = r.text
    soup = BeautifulSoup(data)
    return soup

# -------- Baby Garden (Seeds) -------
url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l="
#url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l=Lower+Earth+Orbit" # Suggested for you challenge

food = kitchen(url)

goodLinks = []
badLinks = []
resultsList = []


# ------- Grab all of the links
for link in food.find_all('a'):
    name = link.get('href')
    try:
        if "/pagead" in name:
            #print(name)
            goodLinks.append(name)
        else :
            badLinks.append(name)
    except:
        None

#print(goodLinks)
#print(badLinks)



# -------- Grab Data from Results
print("We found " + str(len(goodLinks)) + " good links, and " + str(len(badLinks)) + " bad links on this page")  #How many links did we pars for text vs how many were labelled as non-positions

for links in goodLinks:     # For each Link
    tryTimes = 10           # num of times to try to fetch data
    tryMeter = 0            # num of times to tried
    tryMore = True          # continue trying bool

    while tryMore:          # Fetch Data from Webpage in list
        try:
            fullLink = (STEM + str(links))
            food = kitchen(fullLink)
            resultsList.append(food)
            dividers = food.find_all('div', 'jobsearch-JobComponent-description')       # Fetch Job Description Content
            info = dividers[0].get_text(" ")
            #print(fullLink)
            #print(info, "\n")
            resultsList.append([fullLink, info])
            break
        except:             # Error Handling
            time.sleep(2)
            tryMeter += 1
            if tryMeter > tryTimes:
                tryMore = False
            pass

[print(item) for item in resultsList]