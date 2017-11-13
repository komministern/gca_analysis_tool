#!/usr/bin/env python

import os
import shutil

os.system('pyside-uic ui_mainwindow.ui -o ui_mainwindow.py')
os.system('pyside-uic ui_filterdialog.ui -o ui_filterdialog.py')

#os.system('cp ui_mainwindow.py ../project/view/.')
#os.system('cp ui_filterdialog.py ../project/view/.')

shutil.copyfile('./ui_mainwindow.py', '../project/view/ui_mainwindow.py')
shutil.copyfile('./ui_filterdialog.py', '../project/view/ui_filterdialog.py')
