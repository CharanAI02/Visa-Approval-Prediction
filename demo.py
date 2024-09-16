from Visa_prediction.logger import logging
from Visa_prediction.exception import visapredException
import sys

try:
    a=1/"10"
except Exception as e:
    logging.info(e)
    raise visapredException(e,sys) from e


# logging demo
#logging.info("Welcome to our custom log")