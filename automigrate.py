from glob import glob
from os import system
import platform
import sys

if platform.system() == 'Windows':
    for i in glob('*/models.py'):
        system(f'{sys.executable} manage.py makemigrations {i[:-10]}')
    system(f'{sys.executable} manage.py migrate')
