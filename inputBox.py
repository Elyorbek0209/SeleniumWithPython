from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


import time


#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.surveymonkey.com/"


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


#2. Declaring Sign Up button Object with XPATH
signUp = driver.find_element_by_xpath("//a[@class='sign-up static-buttons']")

#3. Clicking Sign Up Button
signUp.click()

time.sleep(3)


#----HOW TO FIND HOW MANY INPUTBOXES PRESENT IN WEB PAGE?---

#INPUTBOXES = driver.find_elements(By.CLASS_NAME,'notranslate wds-input wds-input--stretched')

#print(len(INPUTBOXES))


#----HOW TO GET THE STATUS OF THE PARTICULAR ELEMENT IS DISPLAYED OR NOT?----

#4 Declaring Username set box object with Xpath
userName = driver.find_element_by_xpath("//input[@id='username']")

status = userName.is_displayed() # status is Boolean Here

print("Element is Displayed or not" + "status")


#-----------------------------------------------


#5 Set the Username Value
userName.send_keys("python0209")


#6 Declaring Password Object
password = driver.find_element_by_xpath("//input[@id='password']")

#7 Set the password value
password.send_keys("HelloPython12345#")


#8 Declaring Email Object
email = driver.find_element_by_xpath("//input[@id='email']")

#9 Set the email value
email.send_keys("helloPython0209@gooogle.com")


#10 Declare first name object
firstName = driver.find_element_by_xpath("//input[@id='first_name']")

#11 Set the first name Value
firstName.send_keys("Donald")

#12 Declare last name object
lastname = driver.find_element_by_xpath("//input[@id='last_name']")

#13 Set the Last Name value

lastname.send_keys("Trump")

#14 Close the all browser
driver.quit()