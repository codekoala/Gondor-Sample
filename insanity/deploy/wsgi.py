from os.path import abspath, join, dirname
import os
import sys

from django.core.handlers.wsgi import WSGIHandler

sys.path.insert(0, abspath(join(abspath(dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, abspath(join(abspath(dirname(__file__)), os.pardir)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'insanity.settings'
application = WSGIHandler()
