from selenium import webdriver

from selenium.webdriver import ActionChains

import time



#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://opensource-demo.orangehrmlive.com/"


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

Username = driver.find_element_by_xpath("//input[@id='txtUsername']")

#1st set Username
Username.send_keys("Admin")


Password = driver.find_element_by_xpath("//input[@id='txtPassword']")

#2nd set Password
Password.send_keys("admin123")


loginButton = driver.find_element_by_xpath("//input[@id='btnLogin']")

#3rd Click Login Button
loginButton.click()


# Now we should Click "Admin" Link & drop down appears then click chikd Links

#1st parent link
adminLink = driver.find_element_by_xpath("//a/b[contains(text(), 'Admin')]")

#2nd child link
userManagement = driver.find_element_by_xpath("//a[contains(text(), 'User Management')]")

#3rd subchild link
users = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")


#After identifying the above parent & child links XPATH, we'll create 'actions' Class
#Here 1st we should import 'ActionChains'

actions = ActionChains(driver)

actions.move_to_element(adminLink).move_to_element(userManagement).move_to_element(users).click().perform()










#driver.quit()



































