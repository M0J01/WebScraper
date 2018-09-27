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
    soup = BeautifulSoup(data, features="html.parser")
    return soup

# -------- Baby Garden (Seeds) -------
url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l="
#url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l=Lower+Earth+Orbit" # Suggested for you challenge

food = kitchen(url)

goodLinks = []
badLinks = []
resultsList = []
savedResults = []

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
        try:                # Try to fetch and parse data
            fullLink = (STEM + str(links))
            food = kitchen(fullLink)

            #resultsList.append(food)
            dividers = food.find_all('div', 'jobsearch-JobComponent-description')       # Fetch Job Description Content
            info = dividers[0].get_text(" ")
            #print(fullLink)
            #print(info, "\n")

            titleList = food.title.get_text().split("- ")
            title, location = '- '.join(titleList[:-2]), titleList[-2]
            companyName = food.find_all("div", 'icl-u-lg-mr--sm')[0].get_text()

            resultsList.append([title, location, companyName, fullLink, info, food])      # Append the link, the relevant info, and the full info
            break           # Fetch successfull, go to the next link
        except:             # Fetch Unsuccessfull, continue? i.e. Error 'Handling'
            time.sleep(2)
            tryMeter += 1
            if tryMeter > tryTimes:
                tryMore = False
            pass

for i in range(len(resultsList)):
    item = resultsList.pop()
    if item not in savedResults:
        savedResults.append(item)



saveFileName = 'rawExtractedData.txt'
saveFile = open(saveFileName, 'a')
[[saveFile.write(str(item)), saveFile.write("\n\n!@#$%^&*()_+\n\n")] for item in savedResults]
saveFile.write("\n\n!@#$%^&*()_+\n\n")
saveFile.close()
#[print(item[:-1]) for item in resultsList]