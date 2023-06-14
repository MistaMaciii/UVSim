"""
UVSim - Simple Virtual Machine 
Elena Mitchell, Justin Peeples, Mac Snow, Wes James
Utah Valley University
"""
import UVSim
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal

class UVSimThread(QThread):
    finished = pyqtSignal()

    def run(self):
        uvSim = UVSim.UVSim()
        uvSim.loadFile()
        uvSim.runSystem()
        self.finished.emit()

def main():
    app = QApplication([])
    window = QWidget()
    label = QLabel("UVSim")
    button = QPushButton("Run Program")
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()

    thread = UVSimThread()
    thread.finished.connect(app.quit)

    button.clicked.connect(thread.start)

    app.exec_()

if __name__ == '__main__':
    main()
