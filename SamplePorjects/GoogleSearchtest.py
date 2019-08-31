from selenium import webdriver




chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.google.com"

EXPECTED_TITLE = "Google"


driver = webdriver.Chrome(executable_path=chromePath)


#------------------------------------------

#----Sample Project with Selenium Python---


#1. Create a Test For Google Search

#2. Add Implicit wait 10 Sec

#3 Maximize Window

#4 Create Unit Test

#5 Add HTML REPORTING Library

#6 Run From Command Line

#-------------------------------------------




#2. ---IMPLICIT WAIT--> Applicable for all the Element of the page & only 1 Time we'll Specify this code at the beggining of the Code
driver.implicitly_wait(10)

#3. Maximize Window
driver.maximize_window()

# Launch the URL
driver.get(URL)



