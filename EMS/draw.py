from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from algorithms import *
from dialog import *


class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Query point and polygon
        self.__add_L = True
        self.__L = QPolygonF()
        self.__B = QPolygonF()
        self.__LD = QPolygonF()

        self.__LLoad = []
        self.__BLoad = []
        self.__LDLoad = []

        self.__add_vertex = True

        self.dmin = 100
        self.alpha = 0.3
        self.beta = 1000
        self.gamma = 1000
        self.lam = 20
        self.iters = 500

        #p1 = QPointF(0, 150)
        #p2 = QPointF(100, 100)
        #p3 = QPointF(200, 150)
        #self.__L.append(p1)
        #self.__L.append(p2)
        #self.__L.append(p3)

        #p4 = QPointF(0, 100)
        #p5 = QPointF(100, 90)
        #p6 = QPointF(200, 100)

        #self.__B.append(p4)
        #self.__B.append(p5)
        #self.__B.append(p6)

    def mousePressEvent(self, e:QMouseEvent):
        #Left mouse button click
        x = e.position().x()
        y = e.position().y()

        #Create new point
        p = QPointF(x, y)

        #Add point to L
        if self.__add_L:
            self.__L.append(p)

        #Add point to B
        else:
            self.__B.append(p)

        #Repaint screen
        self.repaint()

    def paintEvent(self, e:QPaintEvent):
        #Draw polygon

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes
        qp.setPen(Qt.GlobalColor.black)

        #Draw L
        qp.drawPolyline(self.__L)

        for p in range(len(self.__LLoad)):
            qp.drawPolyline(self.__LLoad[p])

        # Set attributes
        qp.setPen(Qt.GlobalColor.blue)

        # Draw B
        qp.drawPolyline(self.__B)

        for p in range(len(self.__BLoad)):
            qp.drawPolyline(self.__BLoad[p])

        # Set attributes
        qp.setPen(Qt.GlobalColor.red)

        # Draw LD
        qp.drawPolyline(self.__LD)

        for p in range(len(self.__LDLoad)):
            qp.drawPolyline(self.__LDLoad[p])

        #End draw
        qp.end()

    def switchSource(self):
        #Move point or add vertex
        self.__add_vertex = not(self.__add_vertex)

    def getL(self):
        return self.__L

    def getB(self):
        return self.__B

    def getLLoad(self):
        return self.__LLoad

    def getBLoad(self):
        return self.__BLoad

    def setLD(self, LD_):
        self.__LD = LD_

    def setLDLoad(self, LDLoad):
        self.__LDLoad = LDLoad

    def setL(self, L):
        self.__LLoad.append(L)

    def setB(self, B):
        self.__BLoad.append(B)

    def setSource(self, status):
        self.__add_L = status

    def clearAll(self):
        self.__L.clear()
        self.__B.clear()
        self.__LD.clear()

        self.__LLoad.clear()
        self.__BLoad.clear()
        self.__LDLoad.clear()

    def setSettings(self):
        a = Algorithms()
        dialog = InputDialog()
        if dialog.exec():
            dmin, alpha, beta, gamma, lam, iters = dialog.getInputs()
            try:
                dmin = int(dmin)
                alpha = float(alpha)
                beta = int(beta)
                gamma = int(gamma)
                lam = int(lam)
                iters = int(iters)
                self.dmin = dmin
                self.alpha = alpha
                self.beta = beta
                self.gamma = gamma
                self.lam = lam
                self.iters = iters
            except ValueError:
                dmin, alpha, beta, gamma, lam, iters = a.setDefaultSettings()
                self.InvalidInput()
                self.dmin = dmin
                self.alpha = alpha
                self.beta = beta
                self.gamma = gamma
                self.lam = lam
                self.iters = iters
        else:
            return

    def getSettings(self):
        return self.dmin, self.alpha, self.beta, self.gamma, self.lam, self.iters

    def InvalidInput(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Wrong Input")
        dlg.setText("Invalid input. Use integer for custom settings (except for alpha coefficient). Default settings will be applied.")
        dlg.exec()