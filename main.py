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
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("UVSim")
        
        self.button = QPushButton("Run Program")
        self.button.setCheckable(True)
        self.button.released.connect(self.isReleased)
        self.button.setChecked(self.button_is_checked)
        self.button.clicked.connect(self.isClicked)
        self.button.clicked.connect(self.isToggled)
        self.setFixedSize(QSize(200,100))
        self.setCentralWidget(self.button)
    
    def isClicked(self):
        print("Button Clicked")
    
    def isToggled(self, toggle):
        print("Toggle State: ", toggle)

    def isReleased(self):
        self.button_is_checked = self.button.isChecked()

def main():    
    app = QApplication([])          #create instance of the app
    window = MainWindow()           #create window
    window.show()                   #window is hidden by default -- show
    app.exec()                      #start event loop

if __name__ == '__main__':
    main()
