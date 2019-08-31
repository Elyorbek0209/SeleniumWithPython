from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.toolsqa.com/automation-practice-form/"


#---------END OF THE DECLARING VARIABLES -------------



#---------- DOWNLOADING TEXT FILE -------------

#1st thing we'll import "Options" Class from "selenium.webdriver.chrome.options"

#2nd we'll create "Options" Class Object

chromeOptions = Options()


#3rd with "Options" Class object, we'll use ".add_experimental_option()" Method to Give Location for our Download

chromeOptions.add_experimental_option("prefs", {"download.default_directory": "//home//elyor//Selenium//CHROME_Download"})

#------------------------------------------------

print("Options Class object created")


#---DECLARING WEBDRIVER CHROME

driver = webdriver.Chrome(executable_path=chromePath, chrome_options=chromeOptions)

print("Chrome Class Driver Created")


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


download_Element = driver.find_element_by_xpath("//a[contains(text(),'Selenium Automation')]")


#SCROLLING PAGE UNTIL ELEMENT EXIST

driver.execute_script("arguments[0].scrollIntoView()", download_Element)

time.sleep(3)

print("Page Scrolled Successfully")

#Download Link
download_Element.click()

time.sleep(3)





















