import os

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(12))
# WTF_CSRF_CHECK_DEFAULT = False


