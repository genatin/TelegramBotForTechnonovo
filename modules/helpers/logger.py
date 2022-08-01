import sys
import logging
from logging import StreamHandler


logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
handler = StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
