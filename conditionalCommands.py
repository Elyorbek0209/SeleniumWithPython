from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.linkedin.com/in/elyorbek-soliev-77a148122/"



driver = webdriver.Chrome(executable_path = chromePath)

driver.get(URL)

print(driver.title)

driver.delete_all_cookies()

driver.maximize_window()

driver.find_element_by_xpath("//a[@class='nav-header__link']").click()

time.sleep(3)


#//input[@id='username']

userName = driver.find_element_by_xpath("//input[@id='username']")


#//input[@id='password']

passName = driver.find_element_by_xpath("//input[@id='password']")


#//button[@aria-label='Sign in']

signIn = driver.find_element_by_xpath("//button[@aria-label='Sign in']")


print(userName.is_displayed())

print(userName.is_enabled())

userName.send_keys("elyorbeksoliev@gmail.com")



print(passName.is_displayed())

print(passName.is_enabled())

passName.send_keys("Sadaf2015$")



print(signIn.is_displayed())

print(signIn.is_enabled())

signIn.click()

time.sleep(3)

dropDownMe = driver.find_element_by_xpath("//li[@id='profile-nav-item']")

dropDownMe.click()

logOut = driver.find_element_by_xpath("//a[@data-control-name='nav.settings_signout']")

logOut.click()


driver.quit()



# def highlight(element):
#
#     """Highlight (blinks) a Selenium Webdriver Element"""
#
#     driver1 = element._parent
#
#     def apply_style(s):
#         driver1.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
#
#
#
#     original_style = element.get_attribute('style')
#
#
#     apply_style("background: yellow; border: 2px solid red;")
#
#     time.sleep(3)
#
#     apply_style(original_style)





