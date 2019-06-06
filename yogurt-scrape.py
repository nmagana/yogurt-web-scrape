import bs4 as bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import numpy as np

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

# Setting up headless browser with Firefox (works the same as the regular way, just uses less resources)
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)

# Set up driver using Firefox
# driver = webdriver.Firefox()

# Set up driver using PhantomJS
# driver = webdriver.PhantomJS()
# Notes: PhantomJS only gets 40 out of the 60 items from the webpage

driver.get(urlPage)

# Set up timer to allow webpage to load first
time.sleep(10)

# This code scrolls the webpage to the bottom of the screen
# This helps because the browser may not load until we scroll to the bottom
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# We also wait 30s in order to make sure the whole website is loaded
time.sleep(30)

# Using the xpath, we can grab the items from the web page
xPath = "//*[@id='componentsContainer']//div[@class='product-content']//span[contains(@class, 'productTitle')]//a"
items = driver.find_elements_by_xpath(xPath)

print("Number of results on Webpage: ", len(items))

data = []
for item in items:
    item_data = []
    title = item.get_attribute('title')
    webPage = item.get_attribute('href')
    item_data.append(title)
    item_data.append(webPage)
    data.append(item_data)

# Quit driver when finished
driver.quit()

# Create dataframe 
df = pd.DataFrame(data, columns=['Item', 'Link'], index=np.arange(1, len(data)+1))

# Write to CSV file
df.to_csv('asdaYogurtData.csv')