from PyQt6.QtCore import *
from QPoint3DF import *

class Polygon:
    def __init__(self, pol:list[QPoint3DF], Z:float):
        self.__Z = Z
        self.__pol = pol

    def get_Z(self):
        return self.__Z

    def get_pol(self):
        return self.__pol
