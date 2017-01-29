#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


import sys
import os
import shutil
import tarfile
from PySide import QtCore, QtGui
from sitecontainer import SiteContainer
import expanduser


class Database(QtCore.QObject):

    def __init__(self):

        self.home_directory = expanduser.expand_user()
        #print self.home_directory
        #self.home_directory = os.path.expanduser(u'~')
        self.top_directory = os.path.join(self.home_directory, u'GCA Analyzer')
        self.sites_directory = os.path.join(self.top_directory, u'sites')

        self.site_dictionary = {}

        self.check_or_fix_database_directory_structure()
        self.read_all_sites_to_memory()



    # Check filestructure

    def check_or_fix_database_directory_structure(self):
        if not os.path.isdir(self.top_directory):
            os.mkdir(self.top_directory)
        if not os.path.isdir(self.sites_directory):
            os.mkdir(self.sites_directory)    
    


    # Site stuff

    def get_site_names(self):
        sites = sorted(QtCore.QDir(self.sites_directory).entryList(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot))  # This gives utf-8!!!!
        return sites


    def read_site_to_memory(self, site_name):
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


    def copy_historylogs_from_capturesite_file(self, capturesite_filename, site_name):
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





    # Date navigation stuff

    def get_first_entry_date(self, site_name):
        return self.site_dictionary[site_name].first_date


    def get_last_entry_date(self, site_name):
        return self.site_dictionary[site_name].last_date


    def get_third_last_entry_date(self, site_name):
        return self.site_dictionary[site_name].chronological_dates[-3]




    # Ignore stuff

    def add_ignored_date(self, site_name, date):
        self.site_dictionary[site_name].add_ignored_date(date)


    def get_ignored_dates(self, site_name):
        return self.site_dictionary[site_name].get_ignored_dates_list()


    def deignore_all_dates(self, site_name):
        self.site_dictionary[site_name].remove_all_ignored_dates()



    def quit(self):
        QtGui.QApplication.quit()
    
