from bs4 import BeautifulSoup
import requests

print("Herr Shotto")

def kitchen(address):
    r = requests.get(address)
    data = r.text
    soup = BeautifulSoup(data)
    return soup

# ---- MingHua Robotics Engineer - Greer, SC
#page = "/Users/m0j01/Projects/WebScarpez/Practice_Sites/Robotics Engineer - Greer, SC - Indeed.com.htm"

# ---- Wing or Fuselage
page = "/Users/m0j01/Projects/WebScarpez/Practice_Sites/Structural Design Engineer (Wing or Fuselage) - Executive Aircraft - United States - Indeed.com.htm"


# Q3 robotics
page = "/Users/m0j01/Projects/WebScarpez/Practice_Sites/Robotics Engineer - Miami Beach, FL - Indeed.com.html"


# Astrobotic Technology Inc.
page = "/Users/m0j01/Projects/WebScarpez/Practice_Sites/Robotics Research Engineer - Simulation Focus - Pittsburgh, PA - Indeed.com.html"
#print(page)


# Ram Robotics, difficulty reading in the live fetch
page = "/Users/m0j01/Projects/WebScarpez/Practice_Sites/Robotics Engineer - Webster, NY 14580 - Indeed.com.html"

can = open(page, 'r')
text = can.read()

soup = BeautifulSoup(text, features="html.parser")



# ----------- Grabs Quals

#allLi = soup.find_all('li')
#for li in allLi:
#    print(li)




# ---- Works for 3+ pages
# Grabs most relevant text on page
dividers = soup.find_all('div', 'jobsearch-JobComponent-description')
#[print(text) for text in dividers[0].stripped_strings]

text = dividers[0].get_text(" ")
print(len(text))

'''
diver = dividers[0].find_all('p')
for dive in diver:
    print(dive)
    
for divider in dividers:
    print(divider)

'''

#print(dividers[0].get_text(" "))




#print(dividers[0].prettify())
#for line in dividers[0].get_text():
    #print(line)


#print(soup.prettify())


'''

#print(soup.prettify())
#allLinks = soup.find_all()

#print(soup.prettify())

#mainBody = soup.find_all('div class="jobsearch-JobComponent-description icl-u-xs-mt--md"')
#mainBody = soup.find_all('p')
#mainBody = soup.find_('jobsearch-DesiredExperience-item')



#print(len(list(soup.descendants)))
#print(len(list(soup.children)))

<span class="jobsearch-DesiredExperience-header">Desired: </span>
for child in soup.children:
    print("Child")
    print(child)
'''
'''
for descendant in soup.descendants:
    print("Descendant")
    print(descendant)
'''


'''
allP = soup.find_all('p')
print(len(allP))

print(allP[4].descendants)

for parent in allP[4].parents:
    print(parent)

for descendant in allP[4].descendants:
    print(descendant)
'''

#for p in allP:
#    print(p)


#textBody = soup.find_all('div')
#print(textBody)

'''
titles = soup.find_all('title')

for title in titles:
    print(title)

'''