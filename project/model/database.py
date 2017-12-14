#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import sys
import os
import shutil
import tarfile
import subprocess
from PySide import QtCore, QtGui
from sitecontainer import SiteContainer
import platform

import expanduser


class Database(QtCore.QObject):

    def __init__(self):

        if platform.system() == 'Windows':
            #import expanduser
            self.home_directory = expanduser.expand_user()
            
        else:
        
            self.home_directory = os.path.expanduser(u'~')
        
        #self.home_directory = os.path.expanduser(u'~')
            
        self.top_directory = os.path.join(self.home_directory, u'GCA Analyzer')
        self.sites_directory = os.path.join(self.top_directory, u'sites')
        self.filters_directory = os.path.join(self.top_directory, u'filters')
        
        #self.temp_files_directory = os.path.join(self.top_directory, u'temp')
        
        self.path_to_7z_filename = os.path.join(self.top_directory, u'location7z.txt')

        self.site_dictionary = {}
        self.filter_list = []

        self.check_or_fix_database_directory_structure()
        
        self.read_filters_to_memory()
        

        #self.read_all_sites_to_memory()
        #self.read_filters_to_memory()



    # Check filestructure

    def check_or_fix_database_directory_structure(self):
        if not os.path.isdir(self.top_directory):
            os.mkdir(self.top_directory)
        if not os.path.isdir(self.sites_directory):
            os.mkdir(self.sites_directory)    
        if not os.path.isdir(self.filters_directory):
            os.mkdir(self.filters_directory)    
  


    # Site stuff

    def get_site_names(self):
        sites = sorted(QtCore.QDir(self.sites_directory).entryList(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot))  # This gives utf-8!!!!
        return sites


    def read_site_to_memory(self, site_name):
        #print 'request reading of site ' + site_name
        if not site_name in self.site_dictionary.keys():
            #print 'actually read site ' + site_name
            site_directory = os.path.join(self.sites_directory, site_name)
            self.site_dictionary[site_name] = SiteContainer(site_directory)


    def remove_site_from_memory(self, site_name):
        del self.site_dictionary[site_name]


    def read_all_sites_to_memory(self):
        for site_name in self.get_site_names():
            self.read_site_to_memory(site_name)


    def create_new_site(self, capturesite_filename, site_name):
#        self.site_dictionary[site_name].check_or_fix_site_directory_structure()

        self.copy_historylogs_from_capturesite_file(capturesite_filename, site_name)
        self.read_site_to_memory(site_name)


    def update_site(self, capturesite_filename, site_name):
        this_site_directory = os.path.join(self.sites_directory, site_name)
        this_historylog_directory = os.path.join(this_site_directory, u'historylogs')
        previously_ignored_dates = self.site_dictionary[site_name].get_ignored_dates_list()
        shutil.rmtree(this_historylog_directory)
        self.site_dictionary[site_name].check_or_fix_site_directory_structure()

        self.copy_historylogs_from_capturesite_file(capturesite_filename, site_name)
        self.remove_site_from_memory(site_name)
        self.read_site_to_memory(site_name)


    def remove_site_from_disc(self, site_name):
        shutil.rmtree(os.path.join(self.sites_directory, site_name))


    def exist_7z(self):
        if not os.path.exists(self.path_to_7z_filename):
            # Assumed standard path
            self.set_path_to_7z(os.path.join('C:', os.sep, 'Program Files', '7-Zip', '7z.exe'))
        return os.path.exists(self.get_path_to_7z())


    def set_path_to_7z(self, path):
        f = open(self.path_to_7z_filename, 'w')
        f.write(path).encode('utf8')
        f.close()


    def get_path_to_7z(self):
        f = open(self.path_to_7z_filename, 'r')
        path = f.readline().decode('utf8')
        f.close()
        return path


    def copy_historylogs_from_capturesite_file(self, capturesite_filename, site_name):
        if capturesite_filename[-2:] == '.Z':
            self.copy_historylogs_from_older_capturesite_file(capturesite_filename, site_name)
        else:
            self.copy_historylogs_from_newer_capturesite_file(capturesite_filename, site_name)


    def copy_historylogs_from_older_capturesite_file(self, capturesite_filename, site_name):
        # This method reads all historylog files from a tar file (the .Z decompression has previously been done by 7z)
        # UGLY CODE!!!!
        this_site_directory = os.path.join(self.sites_directory, site_name)
        this_historylog_directory = os.path.join(this_site_directory, u'historylogs')

        prg_path = self.get_path_to_7z()
        dest_path = this_site_directory

        self.extractZfiles(prg_path, capturesite_filename, dest_path)
        
        with tarfile.open( os.path.join(dest_path, 'CAPTURESITE_TAR') ) as tar:
            history_members = [member for member in tar.getmembers() if '.txt' in member.name and member.name.startswith('/local/gca_history/')]
            for member in history_members:
                member.name = os.path.basename(member.name)
                tar.extract(member, this_historylog_directory)

        os.remove( os.path.join(dest_path, 'CAPTURESITE_TAR') )


    def extractZfiles(self, prg_path, archive_path, dest_path):
        
        fs_enc = sys.getfilesystemencoding()
        
        dest_switch = '-o' + dest_path
        
        system = subprocess.Popen([prg_path.encode(fs_enc), u'e'.encode(fs_enc), dest_switch.encode(fs_enc), archive_path.encode(fs_enc)], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        return(system.communicate())


    def copy_historylogs_from_newer_capturesite_file(self, capturesite_filename, site_name):
        # This method reads all historylog files from a tar.gz file (the tar module handles the zipping)
        this_site_directory = os.path.join(self.sites_directory, site_name)
        this_historylog_directory = os.path.join(this_site_directory, u'historylogs')
        with tarfile.open(capturesite_filename) as tar:
            history_members = [member for member in tar.getmembers() if '.txt' in member.name and member.name.startswith('/local/history/')]
            for member in history_members:
                member.name = os.path.basename(member.name)
                tar.extract(member, this_historylog_directory)




    # Historylog stuff

    def get_historylog(self, site_name, date):
        site_container = self.site_dictionary[site_name]
        text = site_container.get_historylog(date)
        if text == None:
            text = u'No history log exists for this date.'
        return text


    def get_historylog_dictionary(self, site_name):
        return self.site_dictionary[site_name].historylog_dictionary




    # Comment stuff

    def get_comment(self, site_name, date):
        site_container = self.site_dictionary[site_name]
        text = site_container.get_comment(date)
        if text == None:
            text = ''
        return text


    def save_comment(self, site_name, date, text):
        self.site_dictionary[site_name].save_comment(date, text)


    def delete_comment(self, site_name, date):
        self.site_dictionary[site_name].delete_comment(date)


    def get_comment_dictionary(self, site_name):
        return self.site_dictionary[site_name].comment_dictionary




    # Filter stuff

    def update_filters(self):
        self.write_filters_to_disc()
        self.read_filters_to_memory()

    def read_filters_to_memory(self, filter_file_name = u'filters'):
        filter_path = os.path.join(self.filters_directory, filter_file_name)
        import pickle
        from presenter.filtercontainer import Filter
        try:
            serialized_filters = pickle.load(open(filter_path, 'rb'))
            self.filter_list = [Filter()]
            for each in serialized_filters:
                self.filter_list.append(self.de_serialize_filter(each))
        except:
            self.filter_list = [Filter()]

    def write_filters_to_disc(self, filter_file_name = u'filters'):
        filter_path = os.path.join(self.filters_directory, filter_file_name)
        serialized_filters = []
        for each in self.filter_list:
            if each.name != u'':
                serialized_filters.append(self.serialize_filter(each))
        import pickle
        pickle.dump(serialized_filters, open(filter_path, 'wb'))

    def serialize_filter(self, filter):
        return [filter.content, filter.state, filter.name]
    
    def de_serialize_filter(self, alist):
        from presenter.filtercontainer import Filter
        filter = Filter()
        filter.content = alist[0]
        filter.state = alist[1]
        filter.name = alist[2]
        return filter







    # Date navigation stuff

    def get_first_entry_date(self, site_name):
        return self.site_dictionary[site_name].first_date


    def get_last_entry_date(self, site_name):
        return self.site_dictionary[site_name].last_date


    def get_third_last_entry_date(self, site_name):
        return self.site_dictionary[site_name].chronological_dates[-3]




    # Ignore stuff

    def add_ignored_date(self, site_name, date):
        #self.read_site_to_memory(site_name)
        self.site_dictionary[site_name].add_ignored_date(date)


    def get_ignored_dates(self, site_name):
        #self.read_site_to_memory(site_name)
        return self.site_dictionary[site_name].get_ignored_dates_list()


    def deignore_all_dates(self, site_name):
        #self.read_site_to_memory(site_name)
        self.site_dictionary[site_name].remove_all_ignored_dates()



    def quit(self):
        QtGui.QApplication.quit()
    
