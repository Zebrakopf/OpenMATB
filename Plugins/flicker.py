from PySide2 import QtWidgets, QtCore, QtGui
from Helpers import WFlicker
from Helpers.Translator import translate as _
import numpy as np

class Task(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Task, self).__init__(parent)
        self.my_joystick = None
        self.frameNumber = 0
        self.height = self.parent().height()
        self.width = self.parent().width()
        #self.refresh_rate = self.parent().screen_refreshrate
        # TRACK PARAMETERS ###
        self.parameters = {
            'taskplacement': 'fullscreen',
            'frequency': 10,
            'taskupdatetime': 1,
            'title': 'flicker',
            'amplitude': 100,
            'amp_reduction': 10,
            'task_duration_min':1
        }

        n_seconds = self.parameters['task_duration_min'] * 60 + 100 
        self.opac_vals = (1 + np.sin(2 * np.pi * self.parameters['frequency']  * np.arange(0,n_seconds,1/1000))) * (self.parameters['amplitude'] / 2)  
       # self.opac_vals = np.sin(2 * np.pi *  self.parameters['frequency'] * np.arange(0,n_seconds,1/1000)) * (self.parameters['amplitude'] / 2)  + self.parameters['amplitude'] / 2
        self.opac_vals = self.opac_vals * (self.parameters['amp_reduction'] / 100)

    def onStart(self):
        # Set a WTrack Qt object
        self.widget = WFlicker.WFlicker(self, self.parameters['frequency'], self.parameters['amplitude'])

        # Create a layout for the widget
        layout = QtWidgets.QGridLayout()

        # Add the WTrack object to the layout
        layout.addWidget(self.widget)
        self.setLayout(layout)


    def onUpdate(self):
        # Refresh the display
        #print('refresh',self.parent().totalElapsedTime_ms, self.opac_vals[round(self.parent().totalElapsedTime_ms)])
        self.frameNumber += 1
        self.widget.refreshState(self.opac_vals[round(self.parent().totalElapsedTime_ms )])
        self.widget.repaint()
        #self.widget.refreshState(self.opac_vals[self.frameNumber])

