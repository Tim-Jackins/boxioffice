from glob import glob
from os import system
import platform

if platform.system() == 'Windows':
    for i in glob('*/models.py'):
        system(f'py manage.py makemigrations {i[:-10]}')
    system('py manage.py migrate')
