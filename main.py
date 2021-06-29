import logging
import graypy


class LoggingFilter(logging.Filter):
    def __init__(self):
        # In an actual use case would dynamically get this
        # (e.g. from memcache)
        self.instrument = 'LARMOR'

    def filter(self, record):
        record.instrument = self.instrument
        return True


my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)
log_filter = LoggingFilter()
my_logger.addFilter(log_filter)

my_logger.debug(f"hello graylog from {log_filter.instrument}")

log_filter.instrument = "WISH"

my_logger.debug(f"hello graylog from {log_filter.instrument}")
