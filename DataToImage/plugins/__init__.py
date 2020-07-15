from os import listdir, path
from importlib import import_module

# import all python modules from plugins folder
for f in listdir(path.dirname(__file__)):
    if f in ['__init__.py', 'abc.py'] or not f.endswith('.py'):
        continue
    import_module(f'.{f[:-3]}', 'DataToImage.plugins')
del f
