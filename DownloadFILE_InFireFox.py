from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.toolsqa.com/automation-practice-form/"


#---------END OF THE DECLARING VARIABLES -------------



#---------- DOWNLOADING TEXT FILE IN FIREFOX -------------


#1st we should ADD some Preferences here

#Creating "FirefoxProfile()" Class Object

firefoxPro = webdriver.FirefoxProfile()


#2nd we'll use ".set_preference()" Method to add all kind of preferences

firefoxPro.set_preference("browser.helpApps.neverAsk.saveToDisk", "text/plain,application/pdf")


firefoxPro.set_preference("browser.download.manager.showWhenStarting", False)


firefoxPro.set_preference("browser.download.dir", "//home//elyor//Selenium//CHROME_Download")


firefoxPro.set_preference("browser.download.folderList", 2)


firefoxPro.set_preference("pdfjs.disabled", True)


#------------------------------------------------


print("Options Class object created")


#---DECLARING WEBDRIVER CHROME

driver = webdriver.Firefox(executable_path=geckoPath, firefox_profile=firefoxPro)

print("Firefox Class Driver Created")


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


#2 SCROLLING PAGE UNTIL ELEMENT EXIST

driver.execute_script("arguments[0].scrollIntoView()", download_Element)

time.sleep(3)

print("Page Scrolled Successfully")


#3 Click to Download File
download_Element.click()

print("File Saved")
