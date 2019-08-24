from selenium import webdriver

from selenium.webdriver import ActionChains

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.toolsqa.com/automation-practice-form/"


#---------END OF THE DECLARING VARIABLES -------------



#---DECLARING WEBDRIVER CHROME or IE...---

driver = webdriver.Chrome(executable_path = chromePath)



#---------------------------------------------------------

#--- DELETE ALL THE COOKIES BEFORE START ---

driver.delete_all_cookies()

#---DECLARE IMPLICIT WAIT FOR ALL OBJECT---
driver.implicitly_wait(10)

#---MAXIMIZE THE WINDOW ---
driver.maximize_window()

#-----------------------------------------------------------


#1 Launching URL
driver.get(URL)



#---------- UPLOADING FILE --------

#Switching the Frame
#driver.switch_to_frame(0)


#Here is Paticular Element XPATH

uploadElement = driver.find_element_by_xpath("//input[@name='photo']")

print(uploadElement)

#SCROLLING PAGE UNTIL ELEMENT EXIST

driver.execute_script("arguments[0].scrollIntoView()", uploadElement)

time.sleep(3)

#Uploading FilePath
FilePath = "//home//elyor//Pictures//bike.resized.png"

#With "send_keys()" Method, we'll pass the file
uploadElement.send_keys(FilePath)

print("File Uploaded Successfully")































