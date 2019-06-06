import bs4 as bs
import urllib.request
from selenium import webdriver
import time
import pandas as pd

### Using this method returns None
### By right clicking on the webpage and clicking on View Page Source,
### we can see that no results are returned when we search for the 'listings products ...'
### This is because it is loaded DYNAMICALLY

urlPage = 'https://groceries.asda.com/search/yogurt'

# try:
#     source = urllib.request.urlopen(urlPage)
# except urllib.request.URLError:
#     print('Invalid URL')
#     exit(-1)

# soup = bs.BeautifulSoup(source, 'lxml')
# yogurt_listings = soup.find('div', class_ = 'listings products-list clearfix')
# print(yogurt_listings)

# Instead, we do the following:
# Make sure to have geckodriver installed in your $PATH for Mac
driver = webdriver.Firefox()
driver.get(urlPage)
# This code scrolls the webpage to the bottom of the screen
# This helps because the browser may not load until we scroll to the bottom
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# We also wait 30s in order to make sure the whole website is loaded
time.sleep(30)