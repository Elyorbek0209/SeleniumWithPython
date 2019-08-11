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
driver.implicitly_wait(5)

#---MAXIMIZE THE WINDOW ---
driver.maximize_window()



#1 Launching URL
driver.get(URL)


#-----WORKING WITH LINKS -----

links = driver.find_elements(By.TAG_NAME, "a")

NumberOfLinks = len(links)

print("Number of Links present:", NumberOfLinks)  # output:  Number of Links present: 481







driver.quit()

