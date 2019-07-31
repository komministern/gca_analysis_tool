#!python

import os
import shutil

os.system('pyside2-uic ui_graphwindow.ui -o ui_graphwindow.py')
shutil.copyfile('./ui_graphwindow.py', '../project/view/ui/ui_graphwindow.py')