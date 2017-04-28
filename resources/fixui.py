#!/usr/bin/env python

import os

os.system('pyside-uic ui_mainwindow.ui -o ui_mainwindow.py')
os.system('pyside-uic ui_filterdialog.ui -o ui_filterdialog.py')
os.system('cp ui_mainwindow.py ../project/view/.')
os.system('cp ui_filterdialog.py ../project/view/.')

