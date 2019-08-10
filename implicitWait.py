from selenium import webdriver


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.linkedin.com/in/elyorbek-soliev-77a148122/"

EXPECTED_TITLE = "Elyorbek Soliev - Automation Test Lead/SDET - Synchrony | LinkedIn"


driver = webdriver.Chrome(executable_path=chromePath)

driver.delete_all_cookies()

#---IMPLICIT WAIT--> Applicable for all the Element of the page & only 1 Time we'll Specify this code at the beggining of the Code
driver.implicitly_wait(10)

driver.maximize_window()

driver.get(URL)

titleOfPage = driver.title

assert EXPECTED_TITLE in titleOfPage

driver.find_element_by_xpath("//a[@class='nav-header__link']").click()


userName = driver.find_element_by_id("username")

passName = driver.find_element_by_id("password")

signIn = driver.find_element_by_xpath("//button[@aria-label='Sign in']")



userName.send_keys("elyorbeksoliev@gmail.com")

passName.send_keys("Sadaf2015$")

signIn.click()


dropDownMe = driver.find_element_by_xpath("//li[@id='profile-nav-item']")

dropDownMe.click()

logOut = driver.find_element_by_xpath("//a[@data-control-name='nav.settings_signout']")

logOut.click()

driver.quit()










