# ===========================================================================
# Author:       Max ZIMMER
# Project:      NashFlowComputation 2017
# File:         plotValuesCanvasClass.py
# ===========================================================================

from matplotlib import figure, lines
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas



# ======================================================================================================================



class PlotValuesCanvas(FigureCanvas):
    def __init__(self):
        self.figure = figure.Figure()
        super(PlotValuesCanvas, self).__init__(self.figure)  # Call parents constructor


    def update_plot(self, lowerBound, upperBound, xValues, yValues, *additional_values):

        self.figure.clf()

        axes = self.figure.add_subplot(111)
        yMin, yMax = min(yValues), max(yValues)
        axes.plot(xValues, yValues, linewidth=2, color='green')
        for xVals, yVals in additional_values:
            yMin, yMax = min(yMin, min(yVals)), max(yMax, max(yVals))
            axes.plot(xVals, yVals, linewidth=2, color='red')

        axes.set_xlim(lowerBound, upperBound)
        axes.set_ylim(yMin, yMax)


        self.draw_idle()