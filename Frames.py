from selenium import webdriver

from selenium.webdriver.common.by import By

import time




#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "http://seleniumhq.github.io/selenium/docs/api/java/index.html"


#---------END OF THE DECLARING VARIABLES -------------


#---DECLARING WEBDRIVER CHROME or IE...---
driver = webdriver.Chrome(executable_path= chromePath)


#--- DELETE ALL THE COOKIES BEFORE START ---
driver.delete_all_cookies()

#---DECLARE IMPLICIT WAIT FOR ALL OBJECT---
driver.implicitly_wait(10)

#---MAXIMIZE THE WINDOW ---
driver.maximize_window()



#1 Launching URL
driver.get(URL)


#---While we working with frames, we should switch from one to another with "switch_to_frame()" method

driver.switch_to_frame("packageListFrame")  # 1st FRAME

link = driver.find_element_by_link_text("org.openqa.selenium")

link.click()

time.sleep(3)

driver.back()

time.sleep(3)

#Going to another Frame, 1st i should come out from current Frame to MainPage with ".switch_to_default_content()" method

driver.switch_to_default_content()  # Leaving 1st FRAME



#------------------------2nd FRAME STARTED-------------------------------

driver.switch_to_frame("packageFrame")  #2nd FRAME

secondLink = driver.find_element_by_link_text("WebDriver")

secondLink.click()

time.sleep(3)

driver.back()

time.sleep(3)

driver.switch_to_default_content()  # Leaving 2nd FRAME



#-----------------------------3rd FRAME BEGINS ---------------------------


driver.switch_to_frame("classFrame")    #3rd FRAME

thirdLink = driver.find_element_by_xpath("//div[@class='topNav']//a[contains(text(),'Deprecated')]")

thirdLink.click()

driver.switch_to_default_content() #Leaving 3rd Frame


driver.quit()






