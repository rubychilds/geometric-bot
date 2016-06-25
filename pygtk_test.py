#!/usr/bin/python3

# ZetCode PyGTK tutorial
#
# This is a trivial PyGTK example
#
# author: jan bodnar
# website: zetcode.com
# last edited: February 2009

import pygtk
pygtk.require('2.0')
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        self.show()

PyApp()
gtk.main()
