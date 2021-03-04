import os

from .base import BASE_DIR

# static config
STATIC_ROOT = os.path.join(
    BASE_DIR,
    "static"
)

# media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
