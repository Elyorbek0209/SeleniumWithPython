from selenium import webdriver

import XLUtils

import time

#---------DECLARING VARIABLES -------------

ExcelPath = "//home//elyor//Selenium//EXCEL.xlsx"

chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://en-gb.facebook.com/login/"


#---------END OF THE DECLARING VARIABLES -------------


#---DECLARING WEBDRIVER CHROME or IE...---
driver = webdriver.Chrome(executable_path= chromePath)


#--- DELETE ALL THE COOKIES BEFORE START ---
driver.delete_all_cookies()

#---DECLARE IMPLICIT WAIT FOR ALL OBJECT---
driver.implicitly_wait(5)

#---MAXIMIZE THE WINDOW ---
driver.maximize_window()


driver.get(URL)
