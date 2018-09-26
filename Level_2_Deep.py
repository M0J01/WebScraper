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

'''
dividers = soup.find_all('div', 'jobsearch-JobComponent-description')
[print(text) for text in dividers[0].stripped_strings]
'''

# -------- Grab Data from Results

print("We found " + str(len(goodLinks)) + " good links, and " + str(len(badLinks)) + " bad links on this page")  #How many links did we pars for text vs how many were labelled as non-positions

for links in goodLinks:
    tryMeter = 0
    tryMore = True
    while tryMore:
        try:
            fullLink = (STEM + str(links))
            food = kitchen(fullLink)
            resultsList.append(food)
            dividers = food.find_all('div', 'jobsearch-JobComponent-description')
            #[print(text) for text in dividers[0].stripped_strings] # Stores each list item, p, b etc, as a list item
            info = dividers[0].get_text(" ")
            print(fullLink, "\n")
            print(info)
            break
        except:
            time.sleep(2)
            tryMeter += 1
            if tryMeter > 10:
                tryMore = False
            pass


    #print(food.find_all('b'))
    #print(food.find_all('Basic Qualifications'))
    #print(food.find_all('p'))
    #print(food.find_all('Basic Qualifications'))
    #for item in food.find_all('p'):
    #    print(item)

    #print(food.find_all('jobsearch-DesiredExperience'))
    #print(food.get_text())
    #print(food.body)
    #print(food.title.string)
    #print(food.get("jobsearch-DesiredExperience"))

    #break

#print(goodLinks)
#print(badLinks)