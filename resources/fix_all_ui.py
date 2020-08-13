#!python

import os
import shutil

os.system('pyside2-uic ui_mainwindow.ui -o ui_mainwindow.py')
shutil.copyfile('./ui_mainwindow.py', '../source/view/ui/ui_mainwindow.py')

os.system('pyside2-uic ui_filterdialog.ui -o ui_filterdialog.py')
shutil.copyfile('./ui_filterdialog.py', '../source/view/ui/ui_filterdialog.py')

os.system('pyside2-uic ui_graphwindow.ui -o ui_graphwindow.py')
shutil.copyfile('./ui_graphwindow.py', '../source/view/ui/ui_graphwindow.py')