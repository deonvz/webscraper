from selenium import webdriver
from selenium.webdriver.common.by import By #targeting aid with xpath etc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # wait for page content to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging #Use Python Logging

#Place the Chrome Driver or chrome into the same directory as this script
#Go to the URL you wish to scrape.Now find the element, this is is done with a Right click on the page and select view source. Otherwise press F12 and then use the Inspector to target.
# Right Click this selected element in the source code window and Copy the Xpath or the element Name/ID

# configure webdriver
options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen
# configure chrome browser to not load images and javascript
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

#What URL to scrape
siteurl = "https://www.wikipedia.org/"
# chrome Driver is found here. Select the correct one and extract it to this script directory. Google Chrome webdriver or Edge webdriver or else which ever browser your may be using and then download the correct version and place the exe file into this project directory
driver = webdriver.Chrome(options=options, chrome_options=chrome_options)
driver.get(siteurl)
#====== Out link the Steps in cluding the Clicks and submits that may lead to the next one if Multiple
# Target a Element by property or Xpath
#search_box = driver.find_element(By.XPATH, '//*[@id="tw-009a7709226f7cd643e629e8a569b092"]')
search_box = driver.find_element("name","search") #Target via HTML attribute
#What Keystrokes or words do you wish to send to the element
search_box.send_keys('Python programming')
#press enter
search_box.send_keys(Keys.ENTER)
#or click
##search_box.submit()
#search_box.click()
# Add more Steps below if needed
print(driver.page_source) #Print the Result to Console/Screen
# OR Print to a File in append fashion
#print(driver.page_source, file=open('scrapeoutput.txt', 'a'))
# OR capture the output as Logging as debug,info or warning
logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='')
logging.debug(driver.page_source)
#logging.info('')
#logging.warning('')
#exit in a clean fashion
driver.quit()