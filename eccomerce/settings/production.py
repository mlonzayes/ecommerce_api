from .base import *
from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers


ALLOWED_HOSTS = ['*']

#CORS methods and headers
CORS_ALLOW_METHODS = (
    *default_methods,
)
CORS_ALLOW_HEADERS = (
    *default_headers,
)