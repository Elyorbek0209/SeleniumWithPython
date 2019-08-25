from selenium import webdriver

#---------DECLARING VARIABLES -------------

ExcelPath = "//home//elyor//Selenium//EXCEL.xlsx"

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


#---------------- COOKIES ------------------------

# Cookie is a piece of information from website & saved by our webBrowser

# Cookies are a way of remembering users & their interaction with the site by stroing information in the cookie file as key value pairs.

# It stores the login Information like UserName/Email & Password

# HTTP cookie is also known as a web cookie, a browser cookie or Internet cookie.


# --------Operations on COOKIES-----

# Capture All cookies from browser

# Count number of cookies

# Read Cookie pairs

# Adding new cookies

# Deleting specific cookie by using name of cookie

# Deleting all the cookie

#------------------------------------


# Capture all the Cookies created by Browser
cookies = driver.get_cookies()


#Print Number of cookies have ben Created
print(len(cookies))


#Print All the COOKIE PAIRS
print(cookies)

#How to Add New Cookes to the Browser through Automation?

# create new Cookie OBJECT
cookie = {'name': 'MyNewcookie', 'value': '123456789'}

#add new cookie
driver.add_cookie(cookie)



#-----------------We'll find NUMBER of cookies after adding new Cookie----

# Capture all the Cookies created by Browser
cookies = driver.get_cookies()


#Print Number of cookies have ben Created
print(len(cookies))


#Print All the COOKIE PAIRS
print(cookies)
#---------------------------------------------------------------------------




#Deleting Cookies
driver.delete_cookie('MyNewcookie')



#-----------------We'll find NUMBER of cookies after DELETING new Cookie----

# Capture all the Cookies created by Browser
cookies = driver.get_cookies()


#Print Number of cookies have ben Created
print(len(cookies))


#Print All the COOKIE PAIRS
print(cookies)
#---------------------------------------------------------------------------




driver.quit()











































































































