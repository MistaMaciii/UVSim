import UVSim
import sys
import gui
from Operations.IO_Operations import IO_Operations
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QPushButton




def main():
    app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    w = gui.MainWindow()
    w.show()  # show main window
    sys.exit(app.exec())  # start event loop


if __name__ == '__main__':
    main()