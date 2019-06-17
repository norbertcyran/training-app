import os

from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'npng-workouts.herokuapp.com']