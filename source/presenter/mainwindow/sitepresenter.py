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

import logging

from PySide2 import QtCore, QtGui, QtWidgets

logger = logging.getLogger(__name__)

class SitePresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(SitePresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.presentation_dict = {}
        
        self.temp_site_name = u'_temp'

        site_items = [u''] + self.model.get_site_names()
        self.mainwindow.comboBox_ActiveSite.addItems(site_items)

        self.mainwindow.pushButton_FirstDate.setEnabled(False)
        self.mainwindow.pushButton_LastDate.setEnabled(False)
        self.mainwindow.pushButton_ActiveDate.setEnabled(False)
    

    @property
    def active_site_name(self):
        return self.mainwindow.comboBox_ActiveSite.currentText()
    

    def reload_active_site(self):
        self.set_active_site(self.mainwindow.comboBox_ActiveSite.currentIndex())


    def set_active_site(self, index):

        print('set_active_site: index=%d' % index)
        print('active_site_name=%s' % self.active_site_name)
        
        self.mainwindowpresenter.inhibit_mouseclicks()

        self.presentation_dict[self.active_site_name] = self.mainwindowpresenter.colored_dates(self.active_site_name)
        
        self.mainwindowpresenter.commit_string_search()     # self.update_text() is called in this procedure
        
        self.mainwindowpresenter.update_calendar()
        
        self.mainwindowpresenter.update_comment()
        
        self.mainwindowpresenter.update_menu()
        
        self.mainwindowpresenter.allow_mouseclicks()

        if self.active_site_name != '':
            self.mainwindow.pushButton_FirstDate.setEnabled(True)
            self.mainwindow.pushButton_LastDate.setEnabled(True)
            self.mainwindow.pushButton_ActiveDate.setEnabled(True)

            # if self.mainwindowpresenter.selected_date > self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name):
            #     self.mainwindowpresenter.selected_date = self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name)

        else:
            self.mainwindow.pushButton_FirstDate.setEnabled(False)
            self.mainwindow.pushButton_LastDate.setEnabled(False)
            self.mainwindow.pushButton_ActiveDate.setEnabled(False)

        #if self.mainwindowpresenter.selected_date > self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name):
        #    self.mainwindowpresenter.selected_date = self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name)

    def create_new_site(self):

        new_site_name, ok = QtWidgets.QInputDialog.getText(self.mainwindow, u'Enter a name for the new site', u'This capturesite file does not seem to be associated with any of the existing sites. Please name the new site:') 

        if ok:

            allowed_chars = u'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789-_ '
            allowed_set = set(allowed_chars)
 
            if (set(new_site_name) <= allowed_set) and (new_site_name != ''):

                if new_site_name in self.model.get_site_names():
                    self.mainwindowpresenter.message(u'Site name already exists. Aborting.')
    
                else:
                    self.mainwindowpresenter.inhibit_mouseclicks()
                    print('a')
                    self.model.create_new_site_from_temp_site(new_site_name)
                    print('b')
                    self.presentation_dict[new_site_name] = self.mainwindowpresenter.colored_dates(new_site_name)
                    print('c')
                    self.mainwindow.comboBox_ActiveSite.clear() # This will trigger the currentIndexChanged signal, causing the set_active_site method
                                                                # to be called. This will result in an Exception as index is -1
                    print('d')
                    site_items = [u''] + self.model.get_site_names()
                    print('e')
                    self.mainwindow.comboBox_ActiveSite.addItems(site_items)
                    new_index = site_items.index(new_site_name)
                    print('f')
                    print('create_new_site: new_index=%d' % new_index)
                    print('pre setCurrentIndex signal')
                    self.mainwindow.comboBox_ActiveSite.setCurrentIndex(new_index)
                    print('post setCurrentIndex signal')
                    self.mainwindowpresenter.allow_mouseclicks()

            else:
               
                self.mainwindowpresenter.message(u'Site name may only contain letters, numbers, -_ and space. Aborting.')

        


    def update_site(self, site_name):

        # self.mainwindowpresenter.inhibit_mouseclicks()
        
        self.model.update_site_from_temp_site(site_name)

        site_items = [u''] + self.model.get_site_names()

        old_index = self.mainwindow.comboBox_ActiveSite.currentIndex()
        new_index = site_items.index(site_name)

        # if self.mainwindowpresenter.selected_date > self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name):
        # self.mainwindowpresenter.selected_date = self.model.get_last_entry_date(site_name)


        # This call will change the index in the comboBox, and also
        # update all the views ONLY IF old_index differs from new_index!
        self.mainwindow.comboBox_ActiveSite.setCurrentIndex(new_index)
                            
        # So...
        if old_index == new_index:
            self.set_active_site(new_index)
        
        # self.mainwindowpresenter.allow_mouseclicks()


    # ---------- Import a capturesite file

    


    def import_capturesite(self):

        self.model.remove_temp_site()

        capturesite_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, u'Choose capturesite file to import', self.model.database.home_directory, u'Capturesite (*tar.gz *TAR.Z)')

        if capturesite_filename[-2:] == '.Z':
            
            if not self.model.database.exist_7z():
                self.mainwindowpresenter.message(u'To decompress this Capturesite file, the application 7z needs to be installed. Either this is not the case, or it is installed in a non default location. Please enter the location of the file 7z.exe.')

                path_to_7z, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, u'Path to 7z.exe', self.model.database.home_directory, u'7z console application (7z.exe)')
                self.model.database.set_path_to_7z(path_to_7z)

        if (capturesite_filename[-2:] != '.Z') or ( (capturesite_filename[-2:] == '.Z') and self.model.database.exist_7z() ):

            self.mainwindowpresenter.inhibit_mouseclicks()

            try:
                print('A')
                self.model.create_temp_site(capturesite_filename)
                print('B')
                possible_matching_sites = self.model.get_possible_matching_sites_to_temp_site()

                for each in possible_matching_sites:
                    self.model.database.read_site_to_memory(each)

                print('BB')

                # Now check the second latest date from the existing sites with the new one.

                definite_matching_sites = []

                for site_name in possible_matching_sites:
                    if len(self.model.database.site_dictionary[site_name].get_dates_list()) < len(self.model.database.site_dictionary[self.model.database.temp_site_name].get_dates_list()):
                        comparison_date = sorted(self.model.database.site_dictionary[site_name].get_dates_list())[-2] # -1 did not work for all sites
                    else:
                        comparison_date = sorted(self.model.database.site_dictionary[self.model.database.temp_site_name].get_dates_list())[-2]

                    comparison_log = self.model.database.site_dictionary[site_name].get_historylog(comparison_date)
                    print(site_name)
                    print(comparison_date)
                    if comparison_log == self.model.database.site_dictionary[self.model.database.temp_site_name].get_historylog(comparison_date):
                        definite_matching_sites.append(site_name)

                print('definite_matching_sites')
                print(definite_matching_sites)

                self.mainwindowpresenter.allow_mouseclicks()

                if len(definite_matching_sites) == 0:
                    print('C')
                    self.create_new_site()

                    print('D')

                elif len(definite_matching_sites) == 1:
                    site_to_be_updated = definite_matching_sites[0]

                    if self.model.temp_site_newer_than(site_to_be_updated):
                        clicked = self.mainwindowpresenter.message_with_cancel_choice(u'The capturesite file seems to be affiliated with the already existing ' + site_to_be_updated + ' site.', 
                                                            'Update ' + site_to_be_updated + '?', QtWidgets.QMessageBox.Ok)
                        if clicked == QtWidgets.QMessageBox.Ok:
                            self.update_site(site_to_be_updated)

                    elif self.model.temp_site_equal_to(site_to_be_updated):
                        self.mainwindowpresenter.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site. However, the number of entries in ' + 
                                     u'the capturesite file is the same as in your database. No new information will ' +
                                     u'be added. Aborting import.')

                    elif self.model.temp_site_older_than(site_to_be_updated):
                        self.mainwindowpresenter.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site, but it contains fewer history log entries and thus ' +
                                     u'probably predates it. Aborting import.')

                elif len(definite_matching_sites) > 1:
                    print('Several possibilities!!!!!!!!!!!!!! ERROR.')
                    

            except Exception as e:

                pass
                print(e)
            

            self.model.remove_temp_site()
            self.mainwindowpresenter.calendarpresenter.set_last_date()
            self.mainwindowpresenter.allow_mouseclicks()


