import geopandas as gpd

from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Load:

    def __init__(self, pathBarr, pathElem):
        self.__dataBarr = gpd.read_file(pathBarr)
        self.__dataElem = gpd.read_file(pathElem)

        self.polyBarr = []
        self.polyElem = []

    def readPolyline(self):
        gBarr = [i for i in self.__dataBarr.geometry]
        gElem = [i for i in self.__dataElem.geometry]
        max_x = -10000000
        min_x = 10000000
        max_y = -10000000
        min_y = 10000000
        for p in range(self.__dataBarr.shape[0]):
            pol0 = list(gBarr[p].coords.xy)
            for i in range(len(pol0[0]) - 1):
                if pol0[0][i] < min_x:
                    min_x = pol0[0][i]
                if pol0[0][i] > max_x:
                    max_x = pol0[0][i]
                if pol0[1][i] < min_y:
                    min_y = pol0[1][i]
                if pol0[1][i] > max_y:
                    max_y = pol0[1][i]
        a = -(max_x + min_x) / 2
        c = -(max_y + min_y) / 2
        if abs(max_x - min_x) >= abs(max_y - min_y):
            b = d = 800 / abs(max_x - min_x)
        else:
            b = d = 550 / abs(max_y - min_y)
        for p in range(self.__dataBarr.shape[0]):
            # get x and y coordinates
            pol = list(gBarr[p].coords.xy)

            polyBarr = []
            for i in range(len(pol[0])):
                polyBarr.append(QPointF((pol[0][i] + a) * b + 450, (-pol[1][i] - c) * d + 320))

            self.polyBarr.append(polyBarr)

        for p in range(self.__dataBarr.shape[0]):
            # get x and y coordinates
            pol = list(gElem[p].coords.xy)

            polyElem = []
            for i in range(len(pol[0])):
                polyElem.append(QPointF((pol[0][i] + a) * b + 450, (-pol[1][i] - c) * d + 320))

            self.polyElem.append(polyElem)

    def getPolyBarr(self, p):
        return QPolygonF(self.polyBarr[p])

    def getPolyElem(self, p):
        return QPolygonF(self.polyElem[p])

    def numberBarr(self):
        n = range(self.__dataBarr.shape[0])
        return n

    def numberElem(self):
        n = range(self.__dataElem.shape[0])
        return n

    def clear(self):
        self.polyBarr.clear()
        self.polyElem.clear()