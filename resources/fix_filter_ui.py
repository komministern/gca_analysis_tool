#!python

import os
import shutil

os.system('pyside2-uic ui_filterdialog.ui -o ui_filterdialog.py')
shutil.copyfile('./ui_filterdialog.py', '../project/view/ui/ui_filterdialog.py')