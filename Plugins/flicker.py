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
        #self.refresh_rate = self.parent().screen_refreshrate #not needed at the moment


        # FlickerPARAMETERS ###
        self.parameters = {
            'taskplacement': 'fullscreen',
            'frequency': 100,        # flicker frequency to be devided by 10 to yield  Hz
            'taskupdatetime': 1,   # should stay set to 1 to insure highest posible refresh rate
            'title': 'flicker',
            'amplitude': 100,
            'amp_reduction': 10, # amplitude depth in percent
            'task_duration_min':6 # needs to be initalized to calculate the sine curve in advance
        }

    def onStart(self):
        # Set a WFlicker Qt object
        frequency = self.parameters['frequency'] / 10 #needs to happen due to how original script read parameters
        n_seconds = self.parameters['task_duration_min'] * 60 + 100 # calculate the number of seconds the flicker should be presented for
        self.opac_vals = (1 + np.sin(2 * np.pi * frequency  * np.arange(0,n_seconds,1/1000))) * (self.parameters['amplitude'] / 2)  # init sine wave
        self.opac_vals = self.opac_vals * (self.parameters['amp_reduction'] / 100) # reduce amplitude of sine wave
        self.widget = WFlicker.WFlicker(self) # init the widget

        # Create a layout for the widget
        layout = QtWidgets.QGridLayout()

        # Add the WFlicker object to the layout
        layout.addWidget(self.widget)
        self.setLayout(layout)


    def onUpdate(self):
        # Refresh the opacity of the flicker widget
        #print('refresh',self.parent().totalElapsedTime_ms, self.opac_vals[round(self.parent().totalElapsedTime_ms)])
        #self.frameNumber += 1
        self.widget.refreshState(self.opac_vals[round(self.parent().totalElapsedTime_ms )])
        self.widget.repaint()

