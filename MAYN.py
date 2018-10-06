from bs4 import BeautifulSoup
import requests
import time
import re

"""
Kitchen : Bakes it up
Takes in  : a URL
Spits out : a beautiful soup object
"""
def kitchen(address):
    r = requests.get(address)
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    return soup

# -------- Baby Garden (Seeds) -------
localTime = time.asctime(time.localtime(time.time()))       # Grab time for file naming
STEM = "https://indeed.com"
print("Herr otto")      # Yes, your configuration will atleast get this far

saveFileName = str('Third_Pull_ResultsPull' + localTime + '.txt')
print(saveFileName)     # Print name of save to file

url = "https://www.indeed.com/jobs?q=Robotics+Engineer&l="
food = kitchen(url)

goodLinks = []          # Where we store good link strings
badLinks = []           # Where we store bad link strings
resultsList = []        # Where we store results DEPRECATED
savedResults = []       # Where we ... Deprecated?



# ------ Grab Number of Search Results in a page

numResults = food.find_all('div', {'id':'searchCount'})[0].get_text()   # Maybe should release this after the next line?
numSearchResults = int(str(re.findall(re.compile('Page[^.]* of (.+?) jobs'), numResults)[0]).replace(',',''))
print("Number of Search Results :", numSearchResults)




# ------- Itterate through Job Listing Pages


nextPageExists = True                               # Bool condition for loop
nextPageAddress = "/jobs?q=Robotics+Engineer&l="    # Storage Space for next address to search
tryMeter = 0                                        # Counter for retry before quit
tryMore = 10                                        # Max number of retry before quit

while nextPageExists:
    try:
        food = kitchen(STEM+str(nextPageAddress))           # Pull data from Next List Page
        print("Next Page Address is :" + nextPageAddress)
    except:
        print(" Had difficulty accessing :" + nextPageAddress)

    # ------- Grab all of the links on a Results Page

    for link in food.find_all('a'):                     # Grab all the a tags
        name = link.get('href')                         # grab all the href's
        try:
            if ("/pagead" in name) or ("/rc/" in name): # Sort out real listings vs non-listings
                #print(name)
                if name not in goodLinks:               # If Link is unique, put in toBeCrawled
                    goodLinks.append(name)
            elif name not in badLinks:                 # Sort links into non-crawler links
                badLinks.append(name)
        except:
            None


    print("Total Links so far", str(len(goodLinks)))


    # ------- See if there is a next page

    try:
        nextPageInfo = food.find_all('span', {'pn'})[-1].parent     # Find nextpage object by location
        thereIsNextPage = nextPageInfo.get_text()                   # Find nextpage object text
        if thereIsNextPage[0:4] =="Next":                           # Compare text to expected string
            nextPageAddress = nextPageInfo.get('href')              # Get next page address
            tryMeter = 0                                            # Reset TryMeter
        else:                                                       # Else, break pagelistfetch loop
            nextPageExists = False
            print("Last List Page Reached -read-")
            tryMeter = 0                                            # Reset Try Meter

    # Move this Try/Except up to the web fetch
    except:                                                         # This is probably not best here, as it will retry, but fail everytime if it failed the first time. This is set up to retry fetching a web link (aka kitchen), however, it is just reseraching a string. If this fails once, it will likely fail every time.
        print("Was not able to pull page info on page : " + str(nextPageAddress))
        time.sleep(5)
        tryMeter+=1
        if tryMeter > 10:
            nextPageExists = False
            tryMeter = 0


# Variable for the number of links
numGoodLinksTot = len(goodLinks)
numBadLinksTot = len(badLinks)

badLinksFileName = str("badLinksFile"+localTime)
badLinksFile = open(badLinksFileName, 'a')
print("We found " + str(len(goodLinks)) + " good links, and " + str(len(badLinks)) + " bad links Total")  #How many links did we pars for text vs how many were labelled as non-positions

for link in badLinks:
    badLinksFile.write(str(link))
badLinksFile.close()
print("Bad links written to :", badLinksFileName)

### Destroy the bad links name to free up memory


# -------- Grab Data from Job Posting Links

searchedLinksTot = 0        # Num of links succesfully scraped

for links in goodLinks:     # For each Job Posting Link to be scraped
    tryTimes = 10           # num of times to try to fetch data
    tryMeter = 0            # num of times to tried
    tryMore = True          # continue trying bool

    # While don't get up
    while tryMore:

        # If have not seen this link before, check it for info
        if links not in savedResults:

            # Try to fetch and then parse data
            try:
                fullLink = (STEM + str(links))      # Concatonate stem with Link appendage
                food = kitchen(fullLink)            # Grab web request and create soup object

                # Grab all job description content
                dividers = food.find_all('div', 'jobsearch-JobComponent-description')       # Fetch Job Description Content
                info = dividers[0].get_text(" ")    # Hmmm, don't quite remember this

                # Grab header information ( Job Title, Location, Job sub title
                titleList = food.title.get_text().split("- ")
                title, location = '- '.join(titleList[:-2]), titleList[-2]
                companyName = food.find_all("div", 'icl-u-lg-mr--sm')[0].get_text()

                # Save Company Profile to save page
                companyProfile = [title, location, companyName, fullLink, info, food]
                saveFile = open(saveFileName, 'a')
                saveFile.write(str(companyProfile))
                saveFile.write("\n\n!@#$%^&*()_+\n\n")      # This is the break string between companys
                saveFile.close()
                searchedLinksTot += 1
                print("Page Write Successful, " + str(searchedLinksTot) + " Total Links Searched so far")

                savedResults.append(links)
                break           # Fetch successfull, go to the next link

            # Fetch Unsuccessfull, continue? i.e. Error 'Handling'
            except:
                time.sleep(2)       # Maybe we are fetching too fast
                tryMeter += 1       # Increment move on timer
                print("Problem with page :" + fullLink)

                # Move to next if tried to many times
                if tryMeter > tryTimes:
                    tryMore = False
                    errorfile = open("Errorz.txt", "a")
                    errorfile.write(str(food))
                    errorfile.write("\n\nNext Errorz\n\n")
                    errorfile.close()
                pass    # Move to the next itteration

            else:
                break

''' 
Quick Overview of steps
1. Start at a seed page
2. Grab all links on page and add to a list
3. See if there is a next page, and visit it
4. Repeat until no more pages
5. Itterate through list and grab web data
6. Sort and store web data in text file
7. Give stats on info 
'''

# ----- Ending Stats
print("Wow... The whole ting was finished... Wow...")
print("Total number of Good Links :", numGoodLinksTot)
print("Total number of Links Searched :", searchedLinksTot)
print("Total number of Bad Links :", numBadLinksTot)
