from distutils.core import setup
import py2exe

includes = ['Tkinter']

setup(windows=['picturechoice.py'], includes=includes)
