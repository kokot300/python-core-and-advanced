import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
logging.critical("critical")
logging.error('error')
logging.warning("warning")
#logging.warn("warned") #deprecated
logging.info("uy")
logging.debug("debug")
