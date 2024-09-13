# Generic logger template
import logging
import inspect

def get_custom_logger(level):
    function_name = inspect.stack()[1][3]
    logger_name = function_name + '_logger'
    
    logger = logging.getLogger(logger_name)
    
    logger.setLevel(level)
    
    file_handler = logging.FileHandler("genric_log.log", mode='a')
    file_handler.setLevel(level)
        
    formatter = logging.Formatter('%(asctime)s:%(name)s: %(levelname)s: %(message)s',datefmt = '%d-%m-%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger

def log_student():
    logger = get_custom_logger(logging.ERROR)
    
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

log_student()