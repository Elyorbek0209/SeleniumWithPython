from selenium import webdriver

from selenium.webdriver.common.by import By

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "http://demo.automationtesting.in/Windows.html"


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



#-----WORKING WITH BROWSER WINDOWS---SO WE HANDLE BROWSER WINDOWS??? ----

'''
- "driver.current_window_handle" --->get the Handle of current Window Page of the Browser

- "driver.window_handles" method ---> Handle all the Open Browsers

'''

clickButton = driver.find_element_by_xpath("//a/button[@class='btn btn-info']")

clickButton.click()


# Here 1st,we'll get Handle of the CURRENT WINDOW with ".current_window_handle"

parent = driver.current_window_handle

print(parent)


#To get the Handle Values of the multiple window page of the Browser we use "window_handles"

Childs = driver.window_handles  # return all the handle values of the opened browser windows

print(Childs)

# How we close from 3 browser the 2nd one? - 1st we should get the "handle" value of each browser window
# with "driver.window_handles" method & based on the handle we'll switch from 1st window to 2nd & from 2nd to 3rd window
# & capture the title of the each & every browser window after that we'll use "if else" condition inside the for loop
# & close that particular browser


for handle in Childs:

    #".switch_to.window()" command switch to whichever open window
    driver.switch_to.window(handle)


    PageTitle = driver.title

    print(PageTitle)

    if PageTitle == "Frames & windows":

        driver.close()

        time.sleep(2)

driver.quit()
























