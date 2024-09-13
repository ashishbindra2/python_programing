import logging
import logging.config
# from logging import config

logging.config.fileConfig('logging-config.init')

logger = logging.getLogger('demologger')

logger.critical("it's criticle message!!")