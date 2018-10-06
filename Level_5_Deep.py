from bs4 import BeautifulSoup
import requests
import time
import re

localTime = time.asctime( time.localtime(time.time()) )

print("Herr otto")
saveFileName = str('Third_Pull_ResultsPull' + localTime + '.txt')
print(saveFileName)

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



# Grab Number of Search Results in a page
'''
print(numResults)
pattern = 'Page[^.]* of (.+?) jobs'
patternz = re.compile(pattern)
data = re.findall(patternz, numResults)[0]
'''
numResults = food.find_all('div', {'id':'searchCount'})[0].get_text()
numSearchResults = int(str(re.findall(re.compile('Page[^.]* of (.+?) jobs'), numResults)[0]).replace(',',''))
print("Number of Search Results :", numSearchResults)

#numResults = food.find_all('div', 'resultsTop')

#numResults = "Page XX of {} jobs"
#print('num results:', numResults)
#print(food.prettify())




nextPageExists = True
tryMeter = 0
nextPageAddress = "/jobs?q=Robotics+Engineer&l="

# ------- Itterate through results

while nextPageExists:
    food = kitchen(STEM+str(nextPageAddress))
    print("Next Page Address is :" + nextPageAddress)

    # ------- Grab all of the links on a Results Page

    for link in food.find_all('a'):
        name = link.get('href')
        try:
            if ("/pagead" in name) or ("/rc/" in name):
                #print(name)
                if name not in goodLinks:
                    goodLinks.append(name)
            elif name not in goodLinks:
                badLinks.append(name)
        except:
            None


    print("Total Links so far", str(len(goodLinks)))

    # ------- See if there is a next page
    try:
        nextPageInfo = food.find_all('span', {'pn'})[-1].parent
        thereIsNextPage = nextPageInfo.get_text()
        if thereIsNextPage[0:4] =="Next":
            nextPageAddress = nextPageInfo.get('href')
            tryMeter = 0
        else:
            nextPageExists = False
            print("Last List Page Reached -read-")
            tryMeter = 0

    except:
        print("Was not able to pull page info on page : " + str(nextPageAddress))
        time.sleep(5)
        tryMeter+=1
        if tryMeter > 10:
            nextPageExists = False
            tryMeter = 0


numGoodLinksTot = len(goodLinks)
numBadLinksTot = len(badLinks)

### Print the bad links to a file here, then destroy the bad links to free up memory?



# -------- Grab Data from Results
print("We found " + str(len(goodLinks)) + " good links, and " + str(len(badLinks)) + " bad links Total")  #How many links did we pars for text vs how many were labelled as non-positions

searchedLinksTot = 0

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

            #print(resultsList[0:4])

            print("Company info Extraction Successful")
            resultsList.append([title, location, companyName, fullLink, info, food])      # Append the link, the relevant info, and the full info
            for i in range(len(resultsList)):       # This can be written much more eliquintly, the popping and looping is deprecated
                item = resultsList.pop()
                if item not in savedResults:
                    savedResults.append(item)
                    saveFile = open(saveFileName, 'a')
                    saveFile.write(str(item))
                    saveFile.write("\n\n!@#$%^&*()_+\n\n")
                    saveFile.close()
                    searchedLinksTot += 1

            print("Page Write Successful," + str(searchedLinksTot) + "Total Links Searched so far")

            break           # Fetch successfull, go to the next link
        except:             # Fetch Unsuccessfull, continue? i.e. Error 'Handling'
            time.sleep(2)
            tryMeter += 1
            print("Problem with page :" + fullLink)
            if tryMeter > tryTimes:
                tryMore = False
                errorfile = open("Errorz.txt", "a")
                errorfile.write(str(food))
                errorfile.write("\n\nNext Errorz\n\n")
                errorfile.close()
            pass


print("Wow... The whole ting was finished... Wow...")

print("Total number of Good Links :", numGoodLinksTot)
print("Total number of Links Searched :", searchedLinksTot)
print("Total number of Bad Links :", numBadLinksTot)
#[[saveFile.write(str(item)), saveFile.write("\n\n!@#$%^&*()_+\n\n")] for item in savedResults]

#[print(item[:-1]) for item in resultsList]
