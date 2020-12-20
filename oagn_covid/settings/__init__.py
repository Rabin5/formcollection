import os
import time
from .base import *

if os.environ.get("ENVIRONMENT") == 'development':
    from .development import *
else:
    from .production import *