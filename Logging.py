import logging



#----------LOGGING & LOG Levels----------------

# Logging is a very useful tool in a programmer's toolbox.
# It can help you develop a better understanding of the flow
# of a program & discover scenarios that you might not even
# have thought of while developing


# Log Levels

# - DEBUG

# - INFO

# - WARNING

# - ERROR

# - CRITICAL

#------------------------------------------------

LogFilePath = "//home//elyor//Selenium//seleniumLogs//test.log"

logging.basicConfig(filename=LogFilePath, format='%(asctime)s: %(levelname)s: %(message)s',
level=logging.DEBUG)


logging.error("This is Error Message")

logging.warn("This is Warning Message")

logging.critical("This is Critical message")


print("Login Created")

# DEBUG & INFO will not print it here
logging.debug("This is Debug Message")

logging.info("This is Info Message")
















