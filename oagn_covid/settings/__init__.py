# import os
from decouple import config
from .base import *


if config("ENVIRONMENT") == 'development':
    from .development import *
else:
    from .production import *