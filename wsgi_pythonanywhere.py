# PythonAnywhere WSGI Configuration File
# 
# This file is used by PythonAnywhere to run your Django application.
# Replace /home/yourusername with your actual PythonAnywhere username
#
# Before deployment, update the path and set it as your WSGI file in PythonAnywhere web app configuration

import os
import sys
from pathlib import Path

# Add your project directory to the sys.path
path = '/home/yourusername/adirasite'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'adirasite.settings'

# Import and configure Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
