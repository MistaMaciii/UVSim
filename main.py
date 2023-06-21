import UVSim
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        #initalize UVSim
        self.uvSim = UVSim.UVSim()

        #initialize file_path
        self.file_path = False

        #Set main window
        self.setWindowTitle("UVSim")
        label = QLabel("")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        #Set toolbar
        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)
        
        #Add the 'file' selector button to the toolbar
        self.button_file = QAction("File...")
        self.button_file.setStatusTip("Select the file the run")
        self.button_file.triggered.connect(self.onToolBarFileButtonClick)
        toolbar.addAction(self.button_file)

        #Add the 'run' button to the toolbar
        self.button_run_program = QAction("Run", self)
        self.button_run_program.setStatusTip("Run the file through UVSim")
        self.button_run_program.triggered.connect(self.onToolBarRunButtonClick)
        toolbar.addAction(self.button_run_program)

        #Button 'Checker'
        self.button_is_checked = False

        self.setStatusBar(QStatusBar(self))

    def onToolBarFileButtonClick(self):
        if self.button_is_checked == False:
            self.button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.uvSim.loadFile(self.file_path)
            
            self.button_is_checked = False     #reset button after system is finished
    
    def onToolBarRunButtonClick(self):
        if self.file_path == False:             #check if file_path exists
            print("No file selected. Please select a file")
        else:
            if self.button_is_checked == False:
                self.button_is_checked = True
                self.uvSim.runSystem()
                self.button_is_checked = False     #reset button after system is finished

def main():
        
    app = QApplication(sys.argv) #Open the QApp through MainWindow class with
                                 # command line options
    w = MainWindow()    
    w.show()            #show main window          
    app.exec()          #start event loop

if __name__ == '__main__':
    main()
