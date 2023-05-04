from PyQt6.QtCore import *
from QPoint3DF import *

class Polygon:
    def __init__(self, pol, Z:float):
        # Create polygon
        self.__Z = Z
        self.__pol = pol

    def get_Z(self):
        # Get z coordinate
        return self.__Z

    def get_pol(self):
        return self.__pol
