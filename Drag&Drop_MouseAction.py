from selenium import webdriver

from selenium.webdriver import ActionChains

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://gojs.net/latest/samples/htmlDragDrop.html"


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



#---------- MOUSE ACTIONS --------

#- Mouse Hover

#- Double Click

#- Right Click

#- Drag and Drop

#--------------------------------


#1 Here is Element XPATH which we should DRAG

source_Element = driver.find_element_by_xpath("//div[contains(text(),'Water')]")


#2 Here is Element XPATH where we should DROP it

target_Element = driver.find_element_by_xpath("//*[@id='myDiagramDiv']/canvas")


#3 Now our job is DRAG "source_Element" into "target_Element"

#Creating "ActionChains" Object
actions = ActionChains(driver)



















