from PySide2 import QtWidgets, QtCore, QtGui
import pygame

class WFlicker(QtWidgets.QWidget):

    def __init__(self, parent, frequency, amplitude):
        super(WFlicker, self).__init__(parent)



        self.flickerWidth = self.parent().width
        self.flickerHeight = self.parent().height
        self_frequency = frequency
        self_amplitude = amplitude
        self.opac = 100

        #self.light.setGeometry(
            #self.ulx, self.uly, self.lightWidth, self.lightHeight)
        #self.light.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
    def paintEvent2(self, e):
        screen = QtGui.QGuiApplication.screens()[0]
        # Initialing Color
        color = (255,0,0)
        
        # Drawing Rectangle
        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    def paintEvent(self, e):
        self.painter = QtGui.QPainter()
        self.painter.begin(self)
        self.painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        self.painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 0, self.opac), QtCore.Qt.SolidPattern))
 
        self.painter.drawRect(0, 0, self.flickerWidth, self.flickerHeight)
        #self.painter.drawRect(-100, -100, 1000, 1000)
        self.painter.end()
    def refreshState(self, opac):
        print('refresh', opac)
        self.opac = opac

    # def resizeEvent(self, e):
    #     self.light.setGeometry(0, 0, self.width(), self.height())

