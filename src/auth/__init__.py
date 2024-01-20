import logging


# passlib bug
logging.getLogger('passlib').setLevel(logging.ERROR)
