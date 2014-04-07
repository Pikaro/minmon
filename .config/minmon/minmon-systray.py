#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk
from subprocess import call
from sys import argv
from os import environ

print environ['PATH']

class SystrayIconApp:
	def __init__(self,pid,name):
		self.pid = pid
		self.name = name
		self.tray = gtk.StatusIcon()
		if gtk.icon_theme_get_default().has_icon(self.name):
			self.tray.set_from_icon_name(self.name)
		else:
			self.tray.set_from_stock(gtk.STOCK_ABOUT)
		self.tray.connect('button_press_event', self.click)
		self.tray.connect('popup-menu', self.make_menu)

	def click(self, icon, event):
		if event.button == 1:
			if call(["minmon-state-visible",str(self.pid)]):
				call(["minmon-hide-all",str(self.pid)])
			else:
				call(["minmon-restore-all",str(self.pid)])

  	def make_menu(self, icon, event_button, event_time):
		menu = gtk.Menu()

		quit = gtk.MenuItem("Quit")
		quit.connect('activate', self.quit)

		menu.append(quit)
		menu.show_all()

		menu.popup(None, None, None,
		           event_button, event_time, self.tray)

	def quit(self, event):
		call(["kill",str(self.pid)])
		gtk.main_quit(event)

if __name__ == "__main__":
	SystrayIconApp(argv[1],argv[2])
	gtk.main()
