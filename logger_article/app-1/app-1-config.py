import logging
import pathlib

def filter(record):
    if "send email" in record.getMessage():
        return True
    return False

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# creating StreamHandler
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# creating FileHandler 
path = pathlib.Path(__file__).parent.resolve()
fh = logging.FileHandler(f"{path}/critical.log")
fh.setLevel(logging.CRITICAL)

# create Formatter
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p')

# set formatter to handler
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# add filter to FileHandler
fh.addFilter(filter)

# add handler to logger
logger.addHandler(sh)
logger.addHandler(fh)

# using different severity-level logging function
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message -- just log')
logger.critical('critical message -- send email')

