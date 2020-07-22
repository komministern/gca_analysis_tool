"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

    GCA Analysis Tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GCA Analysis Tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GCA Analysis Tool. If not, see <https://www.gnu.org/licenses/>.

"""


from PySide2 import QtCore, QtGui, QtWidgets
from model.database import Database
from model.datacollector import Datacollector

#logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):

    io_progress = QtCore.Signal(int)

    def __init__(self):

        super(MyModel, self).__init__()

        self.database = Database(self)
        self.datacollector = Datacollector(self)


    def get_filter_list(self):
        return self.database.filter_list
    
    def get_filter_by_index(self, index):
        return self.database.filter_list[index]
    
    def add_filter(self, filter):
        self.database.filter_list.append(filter)
        self.database.filter_list.sort(key = lambda x: x.name)
        self.database.update_filters()
    
    def remove_filter_by_index(self, index):
        del self.database.filter_list[index]
    

    def get_site_names(self):
        return self.database.get_site_names()
    

    def get_historylog_dictionary(self, site_name):
        return self.database.get_historylog_dictionary(site_name)
    
    def get_historylog(self, site_name, date):
        return self.database.get_historylog(site_name, date)

    
    def get_comment_dictionary(self, site_name):
        return self.database.get_comment_dictionary(site_name)
    
    def get_comment(self, site_name, date):
        return self.database.get_comment(site_name, date)
    
    #def get_ignored_dates(self, site_name):
    #    return self.database.get_ignored_dates(site_name)
    
    def get_first_entry_date(self, site_name):
        return self.database.get_first_entry_date(site_name)
    
    def get_last_entry_date(self, site_name):
        return self.database.get_last_entry_date(site_name)



    def add_ignored_date(self, site_name, date):
        self.database.add_ignored_date(site_name, date)
        self.database.remove_site_from_memory(site_name)
        self.database.read_site_to_memory(site_name)

    def get_ignored_dates(self, site_name):
        return self.database.get_ignored_dates(site_name)

    def deignore_all_dates(self, site_name):
        self.database.deignore_all_dates(site_name)
        self.database.remove_site_from_memory(site_name)
        self.database.read_site_to_memory(site_name)

    def deignore_date(self, site_name, date):
        self.database.deignore_date(site_name, date)
        self.database.remove_site_from_memory(site_name)
        self.database.read_site_to_memory(site_name)





    def create_new_site_from_temp_site(self, site_name):
        self.database.rename_site(self.database.temp_site_name, site_name)
    
    def update_site_from_temp_site(self, site_name):
        self.database.copy_historylogs_from_site_to_site(self.database.temp_site_name, site_name)
    
    def create_temp_site(self, capturesite_filename):
        self.database.create_new_site_from_capturesite_file(capturesite_filename, self.database.temp_site_name)
    
    def remove_temp_site(self):
        self.database.remove_site_from_disc(self.database.temp_site_name)
        self.database.remove_site_from_memory(self.database.temp_site_name)
    
    def get_possible_matching_sites_to_temp_site(self):
        
        # This much has to be done. Now, we cannot expect that any one of the other sites are loaded
        # into memory. So we have to decide whether this new temp_site are to update one of these
        # (not loaded) sites or if the temp_site is a completely new site, WITHOUT LOADING THE
        # EXISTING SITES.
                
        # We will compare the three oldest history logs in each site with the three oldest history
        # logs in the temp_site. If this is a match, then this ought to be a candidate for a site
        # to be updated.
                
        temp_dates = sorted(self.database.get_historylog_dictionary(self.database.temp_site_name).keys())

        compare_dates = temp_dates[:3]
        compare_logs = [self.database.get_historylog_dictionary(self.database.temp_site_name)[date] for date in compare_dates]

        possible_candidates = []
                
        for site_name in self.database.get_site_names():

            if site_name != self.database.temp_site_name:
                        
                logs = [self.database.get_historylog_from_disc(site_name, date) for date in compare_dates]
                        
                if logs == compare_logs:
                    possible_candidates.append(site_name)
        
        return possible_candidates

    def temp_site_newer_than(self, site_name):
        nbr_of_historylog_files_in_temp_site = self.database.get_number_of_historylog_files(self.database.temp_site_name)
        nbr_of_historylog_files_in_site = self.database.get_number_of_historylog_files(site_name)
        return (nbr_of_historylog_files_in_temp_site > nbr_of_historylog_files_in_site)
    
    def temp_site_older_than(self, site_name):
        nbr_of_historylog_files_in_temp_site = self.database.get_number_of_historylog_files(self.database.temp_site_name)
        nbr_of_historylog_files_in_site = self.database.get_number_of_historylog_files(site_name)
        return (nbr_of_historylog_files_in_temp_site < nbr_of_historylog_files_in_site)
    
    def temp_site_equal_to(self, site_name):
        nbr_of_historylog_files_in_temp_site = self.database.get_number_of_historylog_files(self.database.temp_site_name)
        nbr_of_historylog_files_in_site = self.database.get_number_of_historylog_files(site_name)
        return (nbr_of_historylog_files_in_temp_site == nbr_of_historylog_files_in_site)


    def get_analysis(self, site_name, start_date, end_date):
        return self.datacollector.get_analysis(site_name, start_date, end_date)


    def save_comment(self, site_name, date, text):
        self.database.save_comment(site_name, date, text)

    def delete_comment(self, site_name, date):
        self.database.delete_comment(site_name, date)
        

    def quit(self):
        QtWidgets.QApplication.quit()