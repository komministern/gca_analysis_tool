# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os 
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker




class SitePresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(SitePresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter


        self.presentation_dict = {}

        self.active_site_name = None
        
        self.temp_site_name = u'_temp'

        site_items = [u''] + self.model.get_site_names()
        self.view.comboBox_ActiveSite.addItems(site_items)
        self.active_site_name = site_items[0]
    

    def set_active_site(self, index):
        
        #self.lock_gui()
        
        #print 'setting active site'
        
        self.presenter.inhibit_mouseclicks()
        
        site_items = [u''] + self.model.get_site_names()
        self.active_site_name = site_items[index]

        self.presentation_dict[self.active_site_name] = self.presenter.colored_dates(self.active_site_name)
        
        self.presenter.commit_string_search()     # self.update_text() is called in this procedure
        
        self.presenter.update_calendar()
        
        self.presenter.update_comment()
        
        #self.allow_mouseclicks()
        
        #self.enable_gui()
        
        self.presenter.update_menu()
        
        self.presenter.allow_mouseclicks()
  

    # ---------- Import a capturesite file

    def import_capturesite(self):

        #self.lock_gui()

        capturesite_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.view, u'Choose capturesite file to import', self.model.home_directory, u'Capturesite (*tar.gz *TAR.Z)')

        #self.inhibit_mouseclicks()

        if capturesite_filename[-2:] == '.Z':
            
            if not self.model.exist_7z():
                self.presenter.message(u'To decompress this Capturesite file, the application 7z needs to be installed. Either this is not the case, or it is installed in a non default location. Please enter the location of the file 7z.exe.')

                path_to_7z, _ = QtGui.QFileDialog.getOpenFileName(self.view, u'Path to 7z.exe', self.model.home_directory, u'7z console application (7z.exe)')
                self.model.set_path_to_7z(path_to_7z)

        
        if (capturesite_filename[-2:] != '.Z') or ((capturesite_filename[-2:] == '.Z') and self.model.exist_7z()):

            temp_site_name = self.temp_site_name

            try:
                
                self.inhibit_mouseclicks()      # ------------------
                
                # Create a temporary site _TEMP
                # The self.mode.create_site decompresses and copies all historylog files to temp_site_name
                # and (!) reads all these in to memory
                
                self.model.create_new_site_from_capturesite_file(capturesite_filename, temp_site_name)
                
                # This much has to be done. Now, we cannot expect that any one of the other sites are loaded
                # into memory. So we have to decide whether this new temp_site are to update one of these
                # (not loaded) sites or if the temp_site is a completely new site, WITHOUT LOADING THE
                # EXISTING SITES.
                
                # We will compare the three oldest history logs in each site with the three oldest history
                # logs in the temp_site. If this is a match, then this ought to be a candidate for a site
                # to be updated.
                
                temp_dates = sorted(self.model.get_historylog_dictionary(temp_site_name).keys())
                
                compare_dates = temp_dates[:3]
                compare_logs = [self.model.get_historylog_dictionary(temp_site_name)[date] for date in compare_dates]
                
                possible_candidates = []
                
                for site_name in self.model.get_site_names():
                    
                    if site_name != temp_site_name:
                        
                        logs = [self.model.get_historylog_from_disc(site_name, date) for date in compare_dates]
                        
                        if logs == compare_logs:
                            possible_candidates.append(site_name)

                

                
                if len(possible_candidates) == 0:
                    
                    # No candidates. 
                    # Create a new site.
                    
                    self.allow_mouseclicks()        # ------------------
                    
                    self.create_new_site(temp_site_name)
                    
                
                elif len(possible_candidates) == 1:
                    
                    site_to_be_updated = possible_candidates[0]
                    
                    existing_number_of_historylog_files = self.model.get_number_of_historylog_files(possible_candidates[0])
                    new_number_of_historylog_files = self.model.get_number_of_historylog_files(temp_site_name)
                    
                    if new_number_of_historylog_files > existing_number_of_historylog_files:
                        
                        # One candidate, the capturesite file contains more historylogs than the present database.
                        # Update the database.
                        
                        self.allow_mouseclicks()        # ------------------
                        
                        clicked = self.message_with_cancel_choice(u'The capturesite file seems to be affiliated with the already existing ' + site_to_be_updated + ' site.', 
                                                            'Update ' + site_to_be_updated + '?', QtGui.QMessageBox.Ok)
                        if clicked == QtGui.QMessageBox.Ok:
                            
                            self.presenter.inhibit_mouseclicks()
                            
                            self.update_site(site_to_be_updated, temp_site_name)
    
                            
                            
                            
                            #self.presentation_dict[new_site_name] = self.colored_dates(new_site_name)
                        
                        # Remove all items from comboBox
                        #self.view.comboBox_ActiveSite.clear()

                        # Repopulate comboBox
                        
                            site_items = [u''] + self.model.get_site_names()
                        #self.view.comboBox_ActiveSite.addItems(site_items)

                            old_index = self.view.comboBox_ActiveSite.currentIndex()
                            new_index = site_items.index(site_to_be_updated)

                            # This call will change the index in the comboBox, and also
                            # update all the views ONLY IF old_index differs from new_index!
                            self.view.comboBox_ActiveSite.setCurrentIndex(new_index)
                            
                            # So...
                            if old_index == new_index:
                                self.set_active_site(new_index)
                            
                            
                            
                            #self.set_active_site(new_index)
                        
                        
                        
                    
                        
                        self.model.remove_site_from_disc(temp_site_name)
                        self.model.remove_site_from_memory(temp_site_name)

                    elif new_number_of_historylog_files == existing_number_of_historylog_files:

                        # One candidate, the capturesite file contains just as many historylogs than the present database.
                        # Abort.

                        self.allow_mouseclicks()        # ------------------
                        
                        self.presenter.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site. However, the number of entries in ' + 
                                     u'the capturesite file is the same as in your database. No new information will ' +
                                     u'be added. Aborting import.')
                        
                        self.presenter.inhibit_mouseclicks()        # ------------------
                        
                        self.model.remove_site_from_disc(temp_site_name)
                        self.model.remove_site_from_memory(temp_site_name)
                        
                    
                    else:
                        
                        # One candidate, the capturesite file contains a lesser number of historylogs than the present database.
                        # Abort.
                        
                        self.presenter.allow_mouseclicks()        # ------------------
                        
                        self.presenter.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site, but it contains fewer history log entries and thus ' +
                                     u'probably predates it. Aborting import.')
                        
                        self.presenter.inhibit_mouseclicks()        # ------------------
                                     
                        self.model.remove_site_from_disc(temp_site_name)
                        self.model.remove_site_from_memory(temp_site_name)
                    
                    
                    
                else:
                    
                    #print 'Two possible candidates. This is troublesome.'
                    
                    str = '('
                    for each in possible_candidates:
                        str += (each + ', ')
                    str = str[:-2] + ')'
                    
                    self.presenter.allow_mouseclicks()        # ------------------
                    
                    self.presenter.message(u'There seems to be several sites that this capturesite file affiliates with ' + str + '.' + 
                                    u'Aborting import.')
                
                    self.presenter.inhibit_mouseclicks()        # ------------------
                
                    self.model.remove_site_from_disc(temp_site_name)
                    self.model.remove_site_from_memory(temp_site_name)
                    
                        
                #self.model.remove_site_from_disc(temp_site_name)
                #self.model.remove_site_from_memory(temp_site_name)

            except Exception as e:
                
                #print e
                
                self.model.remove_site_from_disc(temp_site_name)
                self.model.remove_site_from_memory(temp_site_name)


        #self.enable_gui()
        
        self.presenter.update_menu()

        self.presenter.allow_mouseclicks()



    # Update an existing site
    def update_site(self, site_name, temp_site_name):
        
        self.presenter.inhibit_mouseclicks()  # ------------------
        
        self.model.copy_historylogs_from_site_to_site(temp_site_name, site_name)
        
        self.model.remove_site_from_memory(site_name)
        self.model.read_site_to_memory(site_name)
        
        self.presenter.allow_mouseclicks()    # ------------------



    # Create a new site from scratch
    def create_new_site(self, temp_site_name):
        new_site_name, ok = QtGui.QInputDialog.getText(self.view, u'Enter a name for the new site', u'This capturesite file does not seem to be associated with any of the existing sites. Please name the new site:') 

        if ok:

            allowed_chars = u'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789-_ '
            allowed_set = set(allowed_chars)
 
            if (set(new_site_name) <= allowed_set) and (new_site_name != ''):

                if new_site_name in self.model.get_site_names():
                    self.presenter.message(u'Site name already exists. Aborting.')
                    
                    #self.model.remove_site_from_disc(temp_site_name)
                    #self.model.remove_site_from_memory(temp_site_name)
                    
                    # Remove temp site

                else:
                    
                    try:
                        self.presenter.inhibit_mouseclicks()  # ------------------
                    
                        self.model.rename_site(temp_site_name, new_site_name)

                        self.presentation_dict[new_site_name] = self.presenter.colored_dates(new_site_name)
                        
                        # Remove all items from comboBox
                        self.view.comboBox_ActiveSite.clear()

                        # Repopulate comboBox
                        site_items = [u''] + self.model.get_site_names()
                        self.view.comboBox_ActiveSite.addItems(site_items)

                        new_index = site_items.index(new_site_name)
                        self.view.comboBox_ActiveSite.setCurrentIndex(new_index)    # This also triggers the set_active_site method and makes the new site active!!!!
                        
                        self.presenter.allow_mouseclicks()  # ------------------
                        
                    except Exception as e:
                        
                        self.presenter.allow_mouseclicks()  # ------------------
                        
                        self.presenter.message(u'An unexpected error occured during import. Aborting.')

            else:
                
                self.presenter.allow_mouseclicks()  # ------------------
                
                self.presenter.message(u'Site name may only contain letters, numbers, -_ and space. Aborting.')

        # This should keep everything clean. (Should put this in the __init__ as well though, the disc bit.)
        
        self.presenter.inhibit_mouseclicks()  # ------------------
        
        self.model.remove_site_from_disc(temp_site_name)
        self.model.remove_site_from_memory(temp_site_name)
        
        self.presenter.allow_mouseclicks()  # ------------------

