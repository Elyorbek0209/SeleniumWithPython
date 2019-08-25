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
datefmt='%m/%d/%Y %I:%M:%S %p')


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


logger.error("This is Error Message")

logger.warn("This is Warning Message")

logger.critical("This is Critical message")


print("Login Created")

# DEBUG & INFO will not print it here
logger.debug("This is Debug Message")

logger.info("This is Info Message")















