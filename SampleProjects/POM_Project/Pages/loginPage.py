class LoginPage():

    def __init__(self, driver):

        self.driver = driver


        self.userNameXPATH="//input[@id='txtUsername']"

        self.passwordXPATH = "//input[@id='txtPassword']"

        self.logIn_ButtonXPATH = "//input[@id='btnLogin']"




    # Set Username
    def enter_username(self,username):

        userName = self.driver.find_element_by_xpath(self.userNameXPATH)

        userName.clear()

        userName.send_keys(username)



    # Set password
    def enter_password(self, password):

        passWord = self.driver.find_element_by_xpath(self.passwordXPATH)

        passWord.clear()

        passWord.send_keys(password)





    # Click LOGIN Button
    def click_login_button(self):

        login = self.driver.find_element_by_xpath(self.logIn_ButtonXPATH)

        login.click()



