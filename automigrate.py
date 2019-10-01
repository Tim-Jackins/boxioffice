from glob import glob
from os import system
import sys
import platform

if platform.system() == 'Windows':
    for i in glob('*/models.py'):
        system(f'{sys.executable} manage.py makemigrations {i[:-10]}')
    system(f'{sys.executable} manage.py migrate')
