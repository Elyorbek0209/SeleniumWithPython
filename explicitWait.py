from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC  # EC here Expected Condition



chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.expedia.com"


driver = webdriver.Chrome(executable_path= chromePath)


driver.delete_all_cookies()

driver.implicitly_wait(5)

driver.maximize_window()


driver.get(URL)



flightButton = driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")

flightButton.click()

time.sleep(2) # from python wait


flyingFromInput = driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")

flyingFromInput.send_keys("JFK")


time.sleep(3)


flyingToInput = driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")

flyingToInput.send_keys("TAS")


time.sleep(3)


departingInput = driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")

departingInput.send_keys("09/02/2019")


time.sleep(3)


returningInput = driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")

returningInput.clear()
returningInput.send_keys("12/02/2019")

closeCalendarButton = driver.find_element_by_xpath("//*[@id='flight-returning-wrapper-hp-flight']/div/div[2]/div[1]/button")

closeCalendarButton.click()

time.sleep(3)

searchFlightButton = driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div/label/button")

searchFlightButton.click()


#-------EXPLICIT WAIT --------
wait = WebDriverWait(driver, 20)


checkBox = driver.find_element_by_xpath("//*[@id='intentMediaAdPlacement']/div/div/div/a[1]/div[1]")

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='intentMediaAdPlacement']/div/div/div[2]/a[1]/div[1]")))

#wait.until(EC.element_to_be_clickable(checkBox))

checkBox.click()

time.sleep(3)

driver.quit()