from PySide2 import QtWidgets, QtCore, QtGui
import pygame

class WFlicker(QtWidgets.QWidget):

    def __init__(self, parent):
        super(WFlicker, self).__init__(parent)



        self.flickerWidth = self.parent().width
        self.flickerHeight = self.parent().height
        self.opac = 100 # default full opacity

    def paintEvent(self, e):
        self.painter = QtGui.QPainter()
        self.painter.begin(self)
        self.painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        self.painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 0, self.opac), QtCore.Qt.SolidPattern))
 
        self.painter.drawRect(0, 0, self.flickerWidth, self.flickerHeight)
        self.painter.end()
    def refreshState(self, opac):
        print('refresh', opac)
        self.opac = opac

