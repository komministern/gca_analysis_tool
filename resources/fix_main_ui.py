#!python

import os
import shutil

os.system('pyside2-uic ui_mainwindow.ui -o ui_mainwindow.py')
shutil.copyfile('./ui_mainwindow.py', '../source/view/ui/ui_mainwindow.py')