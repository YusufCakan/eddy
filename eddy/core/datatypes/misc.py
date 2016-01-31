# -*- coding: utf-8 -*-

##########################################################################
#                                                                        #
#  Eddy: a graphical editor for the construction of Graphol ontologies.  #
#  Copyright (C) 2015 Daniele Pantaleone <danielepantaleone@me.com>      #
#                                                                        #
#  This program is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
#  #####################                          #####################  #
#                                                                        #
#  Graphol is developed by members of the DASI-lab group of the          #
#  Dipartimento di Ingegneria Informatica, Automatica e Gestionale       #
#  A.Ruberti at Sapienza University of Rome: http://www.dis.uniroma1.it/ #
#                                                                        #
#     - Domenico Lembo <lembo@dis.uniroma1.it>                           #
#     - Valerio Santarelli <santarelli@dis.uniroma1.it>                  #
#     - Domenico Fabio Savo <savo@dis.uniroma1.it>                       #
#     - Marco Console <console@dis.uniroma1.it>                          #
#                                                                        #
##########################################################################


from enum import Enum, unique, IntEnum


@unique
class Color(Enum):
    """
    This class defines predicate nodes available colors.
    """
    __order__ = 'White Yellow Orange Red Purple Blue Teal Green Lime'

    White = '#fcfcfc'
    Yellow = '#f0e50c'
    Orange = '#f29210'
    Red = '#e41b20'
    Purple = '#724e9d'
    Blue = '#1760ab'
    Teal = '#16ccef'
    Green = '#2da735'
    Lime = '#86f42e'

    @classmethod
    def forValue(cls, value):
        """
        Returns the color matching the given HEX code.
        :type value: str
        :rtype: Color
        """
        for x in cls:
            if x.value == value.lower():
                return x
        return None


@unique
class DiagramMode(IntEnum):
    """
    This class defines the diagram scene operational modes.
    """
    Idle = 0 # idle mode
    NodeInsert = 1 # node insertion
    NodeMove = 2 # node movement
    NodeResize = 3 # node interactive resize
    EdgeInsert = 4 # edge insertion
    EdgeAnchorPointMove = 5 # edge anchor point movement
    EdgeBreakPointMove = 6 # edge breakpoint movement
    LabelMove = 7 # text label edit
    LabelEdit = 8 # text label movement
    RubberBandDrag = 9 # multi selection
    SceneDrag = 10 # scene being dragged by the mouse