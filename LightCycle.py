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

from PyQt4 import QtGui
from PyQt4 import QtCore

import Direction
from Dot import *
from Area import *

class LightCycle(QtCore.QObject):
    def __init__(self, name, tronWindow, colour, position, initialDirection):
        QtCore.QObject.__init__(self, tronWindow)
        self.name = name
        self.tronWindow = tronWindow
        self.colour = colour
        self.direction = initialDirection

        self.occupiedSpaces = [[False for j in xrange(0, self.tronWindow.size[1])]
                               for i in xrange(0, self.tronWindow.size[1])]

        self.nodes = [Dot(self.tronWindow, position, self.colour)]
        self.occupiedSpaces[position[0]][position[1]] = True

    def __del__(self):
        for node in self.nodes:
            node.deleteLater()

    def setDirection(self, direction):
        if(direction == Direction.Up or
           direction == Direction.Down or
           direction == Direction.Left or
           direction == Direction.Right):
            self.direction = direction

    def move(self):
        self.nodes.append(Dot(self.tronWindow,
                              Direction.add(self.getHeadPosition(), self.direction),
                              self.colour))

    def getHeadPosition(self):
        return self.nodes[-1].position

    def computeNextDirection(self):
        otherPossiblePositions = []
        for lightCycle in self.tronWindow.lightCycles:
            if lightCycle != self:
                for direction in Direction.All:
                    otherPossiblePositions.append(Direction.add(lightCycle.getHeadPosition(),
                                                                direction))
        maxArea = 0
        desiredDirection = None
        desiredDirectionCollides = False
        for direction in Direction.All:
            attemptedPosition = Direction.add(self.getHeadPosition(), direction)
            if self.tronWindow.checkPosition(attemptedPosition):
                currentArea = Area(self.tronWindow, attemptedPosition)
                estimatedArea = calculateArea(currentArea.corners)
                if estimatedArea > maxArea:
                    maxArea = estimatedArea
                    desiredDirectionCollides = attemptedPosition in otherPossiblePositions
                    desiredDirection = direction
                elif estimatedArea == maxArea and (desiredDirectionCollides or
                                                   direction == self.direction):
                    desiredDirectionCollides = attemptedPosition in otherPossiblePositions
                    desiredDirection = direction

        if desiredDirection != None:
            self.direction = desiredDirection
