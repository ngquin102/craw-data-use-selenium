from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# What you enter here will be searched for in
# Google Images
query = "dogs"

# Creating a webdriver instance

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize the screen
driver.maximize_window()

# Open Google Images in the browser
driver.get('https://www.freepik.com/')

box = driver.find_element(by="id", value='search-value-fake')

# Type the search query in the search box
box.send_keys(query)

# Pressing enter
box.send_keys(Keys.ENTER)

# Loop to capture and save each image
for i in range(1, 50):

	# range(1, 50) will capture images 1 to 49 of the search results
	# You can change the range as per your need.
	try:

	# XPath of each image
		img = driver.find_element(by=By.XPATH, value='//*[@id="modal-detail"]/div/div/div/header/div/div/div[1]/img')

		# Enter the location of folder in which
		# the images will be saved
		img.screenshot('Download-Web documents' +
					query + ' (' + str(i) + ').png')
		# Each new screenshot will automatically
		# have its name updated

		# Just to avoid unwanted errors
		time.sleep(0.2)

	except:
		
		# if we can't find the XPath of an image,
		# we skip to the next image
		continue

# Finally, we close the driver
driver.close()
