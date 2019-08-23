from selenium import webdriver

from selenium.webdriver import ActionChains

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://swisnl.github.io/jQuery-contextMenu/demo.html"


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


#Here is Paticular Element XPATH & we should Double Click this Element

rightClickButton = driver.find_element_by_xpath("//span[contains(text(),'right click me')]")



#Here we'll create "ActionChains" Class object

actions = ActionChains(driver)


#To Make a RIGHT CLICK, we'll use "context_click()" Method
actions.context_click(rightClickButton).perform()























