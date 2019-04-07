#!python

import os
import shutil

os.system('pyside2-uic ui_mainwindow.ui -o ui_mainwindow.py')
shutil.copyfile('./ui_mainwindow.py', '../project/view/ui/ui_mainwindow.py')

os.system('pyside2-uic ui_filterdialog.ui -o ui_filterdialog.py')
shutil.copyfile('./ui_filterdialog.py', '../project/view/ui/ui_filterdialog.py')

os.system('pyside2-uic ui_analysisdialog.ui -o ui_analysisdialog.py')
shutil.copyfile('./ui_analysisdialog.py', '../project/view/ui/ui_analysisdialog.py')

os.system('pyside2-uic ui_resultswindow.ui -o ui_resultswindow.py')
shutil.copyfile('./ui_resultswindow.py', '../project/view/ui/ui_resultswindow.py')