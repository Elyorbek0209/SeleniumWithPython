from selenium import webdriver

from selenium.webdriver.common.by import By

import time




#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "http://testautomationpractice.blogspot.com/"


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


clickMeButton = driver.find_element_by_xpath("//button[contains(text(),'Click Me')]")

clickMeButton.click()

time.sleep(3)


#--- To Work With Alert Dialog Box, we should to Switch to Alert Command ----

Alert = driver.switch_to_alert()

# To Close the Alert PopUp, we'll use "accept()" method to Click "OK" button
Alert.accept()

time.sleep(3)


clickMeButton.click()

time.sleep(3)


# if we wanna Cancel it, we'll use 'dismiss()' method

Alert.dismiss()

#-----------------------------------------------------------------------------


driver.quit()

