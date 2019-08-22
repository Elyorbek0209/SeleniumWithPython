from selenium import webdriver

#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "http://demo.automationtesting.in/Windows.html"


#---------END OF THE DECLARING VARIABLES -------------


driver = webdriver.Chrome(executable_path = chromePath)


driver.get("https://www.w3schools.com/html/html_tables.asp")


#---------HOW TO WORK WITH WEBTABLES -------------

#To Read the every row and column of WebTable we'll use For Loop.

#1st we should find out how many Rows & Columns we have?

#'th' - representece header
#'tr' - representece rows
#'td' - representense columns

#So how we'll find the count of rows? - we'll find the 1st ROW XPATH &
#with the help of ".findElements()" Method. we'll find "Rows"



#//*[@id="customers"]/tbody/tr[1] -->this is 1st Row Xpath
#& to find the rest of the row, I should remove "[1]" after "tr"

rowsXpath = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")


#To find the count of the rows, we'll use "len" Method Here

RowCount = len(rowsXpath)

print(RowCount)  # output 7

#-------------------------------------------

#The same way We Should Find the COLUMNS Count

#NOTE: we'll get the inside 1st "th"(Header) XPATH which is located inside our 1st ROW
#//*[@id="customers"]/tbody/tr[1]/th[1] & we'll remove "[]" square bracket to handle the rest of the column

ColumnsXpath = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th")



#To find the count of the COLUMNS, we'll use "len" Method Here

ColumnCount = len(ColumnsXpath)


print(ColumnCount)  # output 3

#---------------------------------


#After that we should read all the  rows & columns & how we do that?
#For that we'll use 2 different FOR LOOPS, 1st one will Increment the number of Rows
#2nd one will Increment the number of Columns

#We should create one Dynamic XPATH here 1st


for row in range(2, RowCount+1):

    for col in range(1, ColumnCount+1):

        Text = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[" + str(row) + "]/td[" + str(col) + "]").text

        print(Text, end='   ')

    print()



#driver.quit()



















