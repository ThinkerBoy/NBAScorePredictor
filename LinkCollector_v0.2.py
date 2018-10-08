import requests
from bs4 import BeautifulSoup
import re

def checkCopy(toBeChecked, uniqueLinks):
    for i in uniqueLinks:
        if(toBeChecked == i):
            return True
        else:
            return False
    

# Make it so this method parses the <a> tags after finding them
def getLinks(contents):
    soup = BeautifulSoup(contents, 'html.parser')
    # Gets all tages containing the word 'game'
    tempList = soup.find_all(href=re.compile("game"))
    retList = []

    # Adds the important piece of each tag into a list to be returned at the
    # end of the function
    for i in tempList:
        retList.append(str(i)[9:25])
    return retList


# The starting year of the files you are parsing
year = 2000

while year < 2019:
    # All the contents from the file from a given year are put into contents
    file = open("..\DataSets\Regular Season Only\\" + str(year) + ".html", "r")
    contents = file.read()
    file.close()

    # Calls getLinks method to hold the unique ends of each url
    linkEnds = getLinks(contents)
    fullLinks = []
    
    # Creates full links to each box score
    for i in linkEnds:
        fullLinks.append("https://stats.nba.com" + str(i) + "\n")

    # Creates a new file for the box scores called year in the BoxScoreLinks folder
    bsFile = open("..\DataSets\Regular Season Only\BoxScoreLinks\\" + str(year) + ".txt", "w+")

    for i in fullLinks:
        bsFile.write(i)

    bsFile.close()

    year += 1
