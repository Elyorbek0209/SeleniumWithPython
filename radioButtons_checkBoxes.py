from selenium import webdriver

from selenium.webdriver.support.ui import Select

import time


import time


#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.facebook.com/"


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


#-----WORKING WITH RADIO BUTTONS -----


firstName = driver.find_element_by_xpath("//input[@name='firstname']")

firstName.send_keys("Elyor")


lastName = driver.find_element_by_xpath("//input[@name='lastname']")

lastName.send_keys("Solly")


email = driver.find_element_by_xpath("//input[@name='reg_email__']")

email.send_keys("elyorsolly@mail.ru")

time.sleep(1)


ReEnterEmail = driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']")

ReEnterEmail.send_keys("elyorsolly@mail.ru")



newRegPassword = driver.find_element_by_xpath("//input[@name='reg_passwd__']")

newRegPassword.send_keys("abcd1245@")



#----HOW TO WORK WITH DROP DOWN ? -----

#1st we'll find out the particular drop down box XPATH
monthDD = driver.find_element_by_xpath("//select[@id = 'month']")
dayDD = driver.find_element_by_xpath("//select[@id = 'day']")
yearDD = driver.find_element_by_xpath("//select[@id = 'year']")


#2nd we should create 'Select' class Element

month = Select(monthDD)

day = Select(dayDD)

year = Select(yearDD)


# Here we use ".options" method with "Select" Object & it'll return all the option from drop down list

print(len(month.options))  # 13

print(len(day.options))  # 32

print(len(year.options))  # 116


#--- HOW WE CAPTURE ALL THE OPTIONS AND PRINT THEM AS OUTPUT? ---


allMonth_options = month.options


for option in allMonth_options:

    print(option.text)


"""
Month
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
"""

#--------------------------------------------------------------------



#3rd we'll select the Element "by Visible Text", "by Index", "by Value"

month.select_by_visible_text("Sep")

day.select_by_index(1)

year.select_by_value("1992")

#--------------------------------------



genderRadioButton = driver.find_element_by_xpath("//input[@value='2']")

status = genderRadioButton.is_selected() # return true or false

print(status) # false


genderRadioButton.click()

driver.quit()






























