from selenium import webdriver

from selenium.webdriver.common.by import By

import time





#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.expedia.com/"


#---------END OF THE DECLARING VARIABLES -------------


#---DECLARING WEBDRIVER CHROME or IE...---
driver = webdriver.Chrome(executable_path= chromePath)


#--- DELETE ALL THE COOKIES BEFORE START ---
driver.delete_all_cookies()

#---DECLARE IMPLICIT WAIT FOR ALL OBJECT---
driver.implicitly_wait(10)

#---MAXIMIZE THE WINDOW ---
driver.maximize_window()



#1 Launching URL
driver.get(URL)


#-----WORKING WITH LINKS -----

Links = driver.find_elements(By.TAG_NAME, "a")

NumberOfLinks = len(Links)

print("Number of Links present:", NumberOfLinks)  # output:  Number of Links present: 481


# ---So How we can Read the all the links? - for that we'll use For Loop Concept ---

for link in Links:

    print(link.text)


# --- How to Click Particular Link? -


driver.find_element(By.LINK_TEXT, "Flights").click()

time.sleep(3)

driver.back()

time.sleep(1)


driver.find_element(By.ID, "tab-cruise-tab-hp").click()


driver.find_element(By.PARTIAL_LINK_TEXT, "Hot").click()


driver.quit()

