import serial
import sys
import time
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

ser = serial.Serial('/dev/ttyACM1',baudrate=112500)
# constants
WINDOW_SIZE = 30
MAX_DATA_SIZE = 1024

# declare the Window
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Arduino Analog Plotter")
win.resize(1000,600)


# initialize plots
raw_plot = win.addPlot(title="Raw Pin Data")
raw_curve = raw_plot.plot(pen = 'y')
raw_plot.addLegend()
raw_plot.showGrid(True, True)

# disable auto size of the x-y axis
raw_plot.enableAutoRange('xy', False)
raw_data = np.zeros(1024)

def update():

    global raw_data, ser
    # open serial port
    raw_val = float(ser.readline())
    temp = (raw_val * 5 * 100) / 8192
    raw_data = np.append(raw_data, temp)

    # plot data
    raw_curve.setData(raw_data)

def savecounter():
    ser.close()

import atexit
atexit.register(savecounter)
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
