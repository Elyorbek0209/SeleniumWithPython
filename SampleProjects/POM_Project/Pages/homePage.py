class HomePage():


    def __init__(self, driver):

        self.driver = driver


        self.welcomeLinkXPATH = "//a[@id='welcome']"

        self.logOutXPATH = "//a[contains(text(),'Logout')]"






    # Click Welcome Link
    def click_WelcomeLink(self):

        welcomeLink = self.driver.find_element_by_xpath(self.welcomeLinkXPATH)

        welcomeLink.click()



    # Click LogOut Button
    def click_LogOut(self):

        logOut = self.driver.find_element_by_xpath(self.logOutXPATH)

        logOut.click()



