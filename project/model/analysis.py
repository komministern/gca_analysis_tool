

from PySide2 import QtCore

class Analysis(QtCore.QObject):





    def __init__(self, historylog_dictionary):

        self.historylog_dict = historylog_dictionary

    

    @property
    def dates(self):
        return self.historylog_dict.keys()

    def historylog(self, date):
        return self.historylog[date]

    
    def get_temperatures(self, date):
        

