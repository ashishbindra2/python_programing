import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='w')

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
