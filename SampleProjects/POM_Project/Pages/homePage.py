from SampleProjects.POM_Project.Locators.locators import Locators


class HomePage():


    def __init__(self, driver):

        self.driver = driver


        self.welcomeLinkXPATH = Locators.welcomeLinkXPATH

        self.logOutXPATH = Locators.logOutXPATH






    # Click Welcome Link
    def click_WelcomeLink(self):

        welcomeLink = self.driver.find_element_by_xpath(self.welcomeLinkXPATH)

        welcomeLink.click()



    # Click LogOut Button
    def click_LogOut(self):

        logOut = self.driver.find_element_by_xpath(self.logOutXPATH)

        logOut.click()



