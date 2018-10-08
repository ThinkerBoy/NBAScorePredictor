import pyautogui
import clipboard
import time
print('Press Ctrl-C to quit.')

# Clicks through the page and copies html
def toCopy():
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.keyDown('shiftleft')
    #pyautogui.typewrite('i')
    #pyautogui.keyUp('ctrlleft')
    #pyautogui.keyUp('shiftleft')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'i')
    time.sleep(pauseTime)
    pyautogui.click(1266, 310)
    time.sleep(pauseTime)
    pyautogui.click(1281, 423)
    time.sleep(pauseTime)
    pyautogui.click(1297, 442)
    time.sleep(pauseTime)
    pyautogui.click(1310, 461)
    time.sleep(pauseTime)
    pyautogui.click(1328, 714)
    time.sleep(pauseTime)
    pyautogui.click(1378, 714)
    pyautogui.hotkey('ctrlleft', 'c')
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'i')

# Writes information from the clipboard into a file
def writeToFile(year, count, url):
    writeTo = open('..\DataSets\Regular Season Only\BoxScores\\' + year + '\\' + count + '.txt', 'w')
    writeTo.write(url + '\n')
    writeTo.write(clipboard.paste())

# Types the desired URL into the search bar
def goTo(url):
    pyautogui.click(400,59)
    clipboard.copy(url)
    pyautogui.typewrite(clipboard.paste())
    pyautogui.typewrite('enter', 0.5)

# Runs a loop checking if the page is loaded
def checkLoad():
    return True
    

# Go to page
# Ctrl + Shift + I to open up developer tools
# Click arrows + Scroll until proper area
# Right click line and copy element
# Open text file and paste html
# Save file

# Search bar at X = 202 : Y = 59
# First arrow at X = 1266 : Y = 310
# Second arrow at X = 1281 : Y = 423
# Third arrow at X = 1297 : Y = 442
# Fourth arrow at X = 1310 : Y = 461
# Fifth arrow at X = 1328 : Y = 714
# Right click at X = 1490 : Y = 752
# Copy at X = 1661 : Y = 501
year = 2000
pauseTime = 1
count = 1
try:
    # Clicks to right screen
    pyautogui.click(1266, 301, duration = 0.1)
    # Loops through each year reading from every file
    for i in range((year - 2000), 19):
        year = 2000 + i
        readFrom = open("..\DataSets\Regular Season Only\BoxScoreLinks\\" + str(year) + "v2.txt", 'r')
        links = readFrom.readlines()
        for j in range(0,len(links)):
            curLink = links[len(links) - count]
            goTo(curLink)
            toCopy()
            writeToFile(str(year), str(count), curLink)
            count += 1
        count = 1
except KeyboardInterrupt:
    print('\nDone.')
    print(str(year))
    print(str(count))


