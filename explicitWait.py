from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC  # EC here Expected Condition


#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.expedia.com"


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


#2. Declaring Flight button Object with XPATH
flightButton = driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")

#3. Clicking Flight Button
flightButton.click()


time.sleep(2) # from python wait


#4. Declaring Flight From Set Box Object with XPATH
flyingFromInput = driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")

#5. Set the From Object Value
flyingFromInput.send_keys("JFK")


time.sleep(3)


#6. Declaring Flight To Set Box Object with XPATH
flyingToInput = driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")

#7. Set the Flight To Object Value
flyingToInput.send_keys("MOSCOW")


time.sleep(3)

#8. Declaring Departing Set Box Object with XPATH
departingInput = driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")

#9. Set the Departure Date Value
departingInput.send_keys("09/02/2019")


time.sleep(3)

#10. Declaring Returning Set Box Object with XPATH
returningInput = driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")

#11. Deleting Autopopulated value of Returning set box
returningInput.send_keys(Keys.CONTROL + "a", Keys.DELETE)

#12. Set the retirning Date Value
returningInput.send_keys("12/02/2019")


#13. Declaring Close Button of Calendar Drop Down Object with XPATH
closeCalendarButton = driver.find_element_by_xpath("//*[@id='flight-returning-wrapper-hp-flight']/div/div[2]/div[1]/button")

#14. Click Close Button
closeCalendarButton.click()


time.sleep(3)

#14. Declaring Search Button Object with XPATH
searchFlightButton = driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div/label/button")

#15. Click Search Button
searchFlightButton.click()



#16. Declare --- EXPLICIT WAIT ---
wait = WebDriverWait(driver, 20)

#17. Waiting the particular object to be clickable with EXPLICIT WAIT TIME
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='intentMediaAdPlacement']/div/div/div[2]/a[1]/div[1]")))


#18. Declaring 1st Checkbox Obect with XPATH
checkBox = driver.find_element_by_xpath("//*[@id='intentMediaAdPlacement']/div/div/div/a[1]/div[1]")

#19. Check the checkbox
checkBox.click()


time.sleep(3)


#20. Close all opened Browsers
driver.quit()