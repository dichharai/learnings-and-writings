import logging
import logging.config

logging.config.fileConfig('logging.conf')
# logger for level DEBUG and above
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
logger.critical('critical message -- send email')
