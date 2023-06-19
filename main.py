"""
UVSim - Simple Virtual Machine 
Elena Mitchell, Justin Peeples, Mac Snow, Wes James
Utah Valley University
"""
# import UVSim
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QThread, pyqtSignal

# class UVSimThread(QThread):
#     finished = pyqtSignal()

#def run(self):
#     uvSim = UVSim.UVSim()
#     uvSim.loadFile()
#     uvSim.runSystem()
#     self.finished.emit()

# def main():
#     app = QApplication([])
#     window = QWidget()
#     label = QLabel("UVSim")
#     button = QPushButton("Run Program")
#     layout = QVBoxLayout()
#     layout.addWidget(label)
#     layout.addWidget(button)
#     window.setLayout(layout)
#     window.show()

#     thread = UVSimThread()
#     thread.finished.connect(app.quit)

#     button.clicked.connect(thread.start)

#     app.exec_()
import UVSim
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("UVSim")
        label = QLabel("")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)
        self.button_is_checked = False
        self.button_run_program = QAction("Run", self)
        self.button_run_program.setStatusTip("Run the file through UVSim")
        self.button_run_program.triggered.connect(self.onToolBarButtonClick)
        toolbar.addAction(self.button_run_program)

        self.setStatusBar(QStatusBar(self))

    def onToolBarButtonClick(self):
        if self.button_is_checked == False:
            self.button_is_checked = True
            uvSim = UVSim.UVSim()
            uvSim.loadFile()
            uvSim.runSystem()
            self.button_is_checked = False     #reset button after system is finished

def main():    
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()                    #start event loop

if __name__ == '__main__':
    main()
