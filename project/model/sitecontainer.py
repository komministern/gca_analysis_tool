#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore   #, QtGui
import os
import shutil
import codecs
import logging

logger = logging.getLogger(__name__)

class SiteContainer(QtCore.QObject):
    
    # The int is the progress (0-100)
    historylog_file_progress = QtCore.Signal(int)
    
    def __init__(self, site_directory):

        super(SiteContainer, self).__init__()

        self.historylogs_directory = os.path.join(site_directory, u'historylogs')
        self.comments_directory = os.path.join(site_directory, u'comments')
        self.ignored_directory = os.path.join(site_directory, u'ignored')

        self.check_or_fix_site_directory_structure()

        self.comment_dictionary = self.read_all_comments()

        self.ignored_dates_list = self.read_all_ignored_dates()
        
        self.historylog_dictionary = None
        



    def get_dates_except_ignored_list(self):
        all_dates = self.get_historylog_dictionary().keys()
        ignored_dates = self.get_ignored_dates_list()
        return [date for date in all_dates if date not in ignored_dates]



    def get_dates_list(self):
        return self.get_historylog_dictionary().keys()
    


    def get_first_date(self):
        return sorted(self.get_dates_except_ignored_list())[0]


    
    def get_last_date(self):
        return sorted(self.get_dates_except_ignored_list())[-1]
        




    # Directory structure stuff

    def check_or_fix_site_directory_structure(self):
        if not os.path.isdir(self.historylogs_directory):
            os.mkdir(self.historylogs_directory)
        if not os.path.isdir(self.comments_directory):
            os.mkdir(self.comments_directory)
        if not os.path.isdir(self.ignored_directory):
            os.mkdir(self.ignored_directory)



    # Comments stuff

    def get_comment(self, date):
        try:
            return self.comment_dictionary[date]
        except KeyError:
            return None


    def save_comment(self, date, text):
        #u_day = unicode(date.day())
        u_day = str(date.day())
        if len(u_day) < 2:
            u_day = '0' + u_day
        u_month = str(date.month())
        if len(u_month) < 2:
            u_month = '0' + u_month
        u_year = str(date.year())
        filename = u_year + u_month + u_day + u'.txt'
        destination_path = os.path.join(self.comments_directory, filename)
        with codecs.open(destination_path, mode='w', encoding='utf-8') as f:
            f.write(text)
        if date in self.comment_dictionary:
            del self.comment_dictionary[date]
        self.comment_dictionary[date] = text


    def read_all_comments(self):
        string_dictionary = {}
        for filename in os.listdir(self.comments_directory):
            
            if set(filename) <= set('0123456789.tx'):
                try:
                    year = int(filename[:4])
                    month = int(filename[4:6])
                    day = int(filename[6:8])
                    date = QtCore.QDate(year, month, day)
                    source_path = os.path.join(self.comments_directory, filename)
                    with codecs.open(source_path, mode='r', encoding='utf-8') as f:
                        string_dictionary[date] = f.read()
                except Exception as e:
                    #print e
                    pass
        return string_dictionary


    def delete_comment(self, date):

        u_day = str(date.day())
        if len(u_day) < 2:
            u_day = u'0' + u_day
        u_month = str(date.month())
        if len(u_month) < 2:
            u_month = u'0' + u_month
        u_year = str(date.year())[:4]

        filename = u_year + u_month + u_day + u'.txt'
        path = os.path.join(self.comments_directory, filename)

        try:
            os.remove(path)
        except Exception as e:
            pass
            #print e


        if date in self.comment_dictionary:
            del self.comment_dictionary[date]

        else:
            pass
            #print 'Error deleting comment'




    # Historylog stuff

    def get_number_of_historylog_files(self):
        # Always do this in this manner to avoid unexpected trouble with non utf-8 characters.
        return len([name for name in os.listdir(self.historylogs_directory) if (os.path.isfile(os.path.join(self.historylogs_directory, name)) and self.valid_historylog_filename(name))])
        

    def get_historylog_dictionary(self):
        if not self.historylog_dictionary:
            self.historylog_dictionary = self.read_all_historylogs()
        return self.historylog_dictionary


    def get_historylog(self, date):
        if not self.historylog_dictionary:
            self.historylog_dictionary = self.read_all_historylogs()
        try:
            return self.historylog_dictionary[date]
        except KeyError:
            return None

        
    def read_historylog(self, date):
        
        #return 'read historylog'
        
        try:
            #file_path = os.path.join(self.historylogs_directory, self.historylog_filename(date))
            with codecs.open(os.path.join(self.historylogs_directory, self.historylog_filename(date)), 'r', encoding='utf-8') as f:
                str = f.read()
            return str
        
        except Exception as e:
            
            print(e)
            return ''
        

    def read_all_historylogs(self):
        string_dictionary = {}
        filenames = os.listdir(self.historylogs_directory)
        number_of_files_to_be_read = len(filenames)
        counter = 0
        for filename in filenames:
            try:
                date = self.historylog_date(filename)
                if 'A0001_' in filename and not (date in self.ignored_dates_list):
                    with codecs.open(os.path.join(self.historylogs_directory, filename), 'r', encoding='utf-8') as f:
                        string_dictionary[date] = f.read()
                        # The history log files usually only contains ASCII characters it seems. Some erroneous files
                        # does differ on this though. The utf-8 decoding prohibit errors due to this.
            except ValueError as e:                
                #print '****************'
                #print e
                pass
            counter += 1
            
            self.historylog_file_progress.emit(int(round(100.0*counter/number_of_files_to_be_read)))
            
        return string_dictionary
    
    def valid_historylog_filename(self, filename):
        try:
            date = self.historylog_date(filename)
            return True
        except ValueError as e:
            #print '******'
            return False


    def historylog_date(self, historylog_filename):
        dstr = historylog_filename[6:12]
        year = int('20' + dstr[4:6])
        month = int(dstr[0:2])
        day = int(dstr[2:4])
        return QtCore.QDate(year, month, day)


    def historylog_filename(self, date):
        year_str = str(date.year())[-2:]
        month_str = str(date.month())
        if len(month_str) == 1:
            month_str = '0' + month_str
        day_str = str(date.day())
        if len(day_str) == 1:
            day_str = '0' + day_str
        filename = 'A0001_' + month_str + day_str + year_str + '.txt'
        #print 'Filename: ' + filename
        return filename


    # Ignored dates stuff

    def get_ignored_dates_list(self):
        return self.ignored_dates_list


    def remove_all_ignored_dates(self):
        self.ignored_dates_list = []
        shutil.rmtree(self.ignored_directory)
        self.check_or_fix_site_directory_structure()


    def read_all_ignored_dates(self):
        a_list = []
        try:
            for filename in os.listdir(self.ignored_directory):
                if 'A0001_' in filename:
                    a_list.append(self.historylog_date(filename))
        except Exception as e:
            #print e
            pass
        return a_list
        

    def add_ignored_date(self, date):
        u_day = str(date.day())
        if len(u_day) < 2:
            u_day = u'0' + u_day
        u_month = str(date.month())
        if len(u_month) < 2:
            u_month = u'0' + u_month
        u_year = str(date.year())[2:4]
        if len(u_year) < 2:
            u_year = '0' + u_year
        file_name = u'A0001_' + u_month + u_day + u_year + u'.txt'
        source_path = os.path.join(self.historylogs_directory, file_name)
        destination_path = os.path.join(self.ignored_directory, file_name)
        shutil.copy(source_path, destination_path)
        self.ignored_dates_list.append(date)




