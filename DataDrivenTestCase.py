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


#-----------Here we'll read the data from excel and write---------


rows = XLUtils.getRowCount(ExcelPath,'Sheet1')

for r in range(2, rows+1):

    username = XLUtils.readData(ExcelPath, "Sheet1", r, 1)

    password = XLUtils.readData(ExcelPath, "Sheet1", r, 2)


    usernameInputBox = driver.find_element_by_xpath("//input[@id='email']")

    passwordInputBox = driver.find_element_by_xpath("//input[@id='pass']")

    logInButton = driver.find_element_by_xpath("//button[@id='loginbutton']")


    #Set Username
    usernameInputBox.clear()

    usernameInputBox.send_keys(username)


    #Set Password
    passwordInputBox.clear()

    passwordInputBox.send_keys(password)


    #Click Log In Button
    logInButton.click()



    time.sleep(5)

    Title = driver.title()

    print(Title)


    if Title=='Facebook':

        print("Test is Passed")

        XLUtils.writeData(ExcelPath, "Sheet1", r, 3, "test passed")

    else:

        print("test failed")

        XLUtils.writeData(ExcelPath, "Sheet1", r, 3, "test failed")




    # Log Out Facebook
    logOutDropDown = driver.find_element_by_xpath("//div[@id='userNavigationLabel']")

    logOutDropDown.click()

    time.sleep(3)

    logOutButton = driver.find_element_by_xpath("//div[@id='userNavigationLabel']")

    logOutButton.click()



























