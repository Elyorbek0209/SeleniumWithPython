from selenium import webdriver

#---------DECLARING VARIABLES -------------

ScreenShotFolderPath = "//home//elyor//Selenium//Screenshots//homePage.png"

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





#-----------CAPTURE SCREENSHOTS-------------

# WebDriver offers API's to take screenshot of a web page

#   - save_screenshot('filename')

#   - get_screenshot_as_file('filename')

#--------------------------------------------

#driver.save_screenshot("/home/elyor/Selenium/Screenshots/homePage.png")

driver.save_screenshot(ScreenShotFolderPath)

print("Screenshot created")

driver.get_screenshot_as_file("//home//elyor//Selenium//Screenshots//homePage1.png")

print("Second Screenshot Created")

driver.quit()
































