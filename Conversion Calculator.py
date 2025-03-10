from DCGUI import CalculatorGUI as gui
from PySide6 import QtWidgets
import sys

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        widget = gui()
        widget.show()
        sys.exit(app.exec())
        