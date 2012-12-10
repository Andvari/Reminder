#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Dec 10, 2012

@author: nemo
'''

import gtk
from datetime import date
import appindicator
from dbus.mainloop.glib import DBusGMainLoop
import dbus.service

class Reminder(dbus.service.Object):
    def __init__(self):
        DBusGMainLoop(set_as_default=True)
        self.db = dbus.SessionBus()
            
        self.ind = appindicator.Indicator("hello world client", "", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        
        self.ind.set_icon_theme_path("home/nemo/workspace/Reminder/src/images")
        self.ind.set_icon("pay")
        
        self.Menu = gtk.Menu()
        self.ind.set_menu(self.Menu)        

dt = str(date.today())
day = dt[dt.rfind("-") + 1 : ]

if((int(day)>=23)and(int(day)<=26)):
    rm = Reminder()
    gtk.gdk.threads_init()
    gtk.main()

