from .base import *

DEBUG = False

try:
    from .local import *  # noqa
except ImportError:
    pass
