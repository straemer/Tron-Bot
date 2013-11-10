#!/usr/bin/python

# Copyright 2013 Stephen Kraemer.
# This file is part of TronBot.

# TronBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TronBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TronBot.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt4 import QtGui

from TronWindow import *

def main():
    app = QtGui.QApplication(sys.argv)

    mainWindow = TronWindow()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
