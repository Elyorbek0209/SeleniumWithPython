from selenium import webdriver

from selenium.webdriver.common.by import By

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.w3schools.com/html/default.asp"


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



#-----3 WAYS of SCROLLING DOWN THE PAGES ---------

#1st --> Scroll Down the Page by PIXEL

#driver.execute_script("window.scrollBy(0,500)","")


#2nd --> Scroll Down the Page Till ELEMENT FOUND

#driver.execute_script("arguments[0].scrollIntoView()",Element)


#3rd --> Scroll to END OF THE PAGE

#driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")


#-------------------------------------------

#1st way
#driver.execute_script("window.scrollBy(0,2000)","")

#print("1st scroll executed")

#---------------------------------------



#2nd way - Scroll Down Till Element is Visible

#Here 1st we'll Identify the XPATH of the Element
quizButton = driver.find_element_by_xpath("//a[contains(text(), 'Start HTML Quiz!')]")


#driver.execute_script("arguments[0].scrollIntoView();", quizButton)

#print("2nd Scroll executed")

#-----------------------------------------

#3rd way - How to Scroll the Page till end of the page?
# - With the help of javascript command "window.scrollBy(0, document.body.scrollHeight)", we'll scroll it


driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")



driver.quit()






























