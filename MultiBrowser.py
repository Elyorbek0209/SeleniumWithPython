from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.linkedin.com/in/elyorbek-soliev-77a148122/"

URL1 = "https://www.youtube.com"


#driver = webdriver.Firefox(executable_path=geckoPath)

driver = webdriver.Chrome(executable_path = chromePath)



driver.get(URL)
d

print(driver.title) # capture the the title of the page

print(driver.current_url) #return URL of the page

print(driver.page_source)

#-----------------------

driver.get(URL1)

print(driver.title)

print(driver.current_url)



driver.back()

print(driver.title)

time.sleep(5)


driver.forward()

print(driver.title)

time.sleep(5)


driver.back()


driver.delete_all_cookies()

driver.find_element_by_xpath("//a[@class='nav-header__link']").click()

time.sleep(5)

#driver.close() #Close the Current Browser command

driver.quit() #Close all the Browser






