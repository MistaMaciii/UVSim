import UVSim
import sys
import io
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QPlainTextEdit, QMessageBox, QLineEdit, QVBoxLayout, QWidget, QTextEdit
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QMetaObject
from PyQt6.QtGui import QTextCursor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize UVSim
        self.uvSim = UVSim.UVSim()

        # Initialize file_path
        self.file_path = False

        # Main Layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)
        # Set main window
        self.setWindowTitle("UVSim")
        label = QLabel("")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(800, 450)

        #label for memory contents
        mem_label = QLabel("Memory")
        main_layout.addWidget(mem_label)

        #Set textedit to display memory contents
        self.memory_textedit = QTextEdit()
        self.memory_textedit.setReadOnly(True)

        #add QTextEdit to the QVBoxLayout
        main_layout.addWidget(self.memory_textedit)

  
        # Set toolbar
        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        # Add the 'file' selector button to the toolbar
        self.button_file = QAction("File...")
        self.button_file.setStatusTip("Select the file to run")
        self.button_file.triggered.connect(self.onToolBarFileButtonClick)
        toolbar.addAction(self.button_file)

        # Add the 'run' button to the toolbar
        self.button_run_program = QAction("Run", self)
        self.button_run_program.setStatusTip("Run the file through UVSim")
        self.button_run_program.triggered.connect(self.onToolBarRunButtonClick)
        toolbar.addAction(self.button_run_program)

        # Button 'Checker'
        self.button_is_checked = False

        self.setStatusBar(QStatusBar(self))

        #Add Console Output
        console_output = QLineEdit()
        console_output.setReadOnly(True)
        main_layout.addWidget(console_output)

    def update_memory_display(self, mem):
        memory_text ="\n".join(mem)
        self.memory_textedit.setPlainText(memory_text)

    def onToolBarFileButtonClick(self):
        if self.button_is_checked == False:
            self.button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.uvSim.loadFile(self.file_path)
            mem = self.uvSim.mem #prints memory after loading file
            self.update_memory_display(mem) 
            self.button_is_checked = False  # reset button after system is finished
    
    def onToolBarRunButtonClick(self):
        if self.file_path == False:  # check if file_path exists
            print("No file selected. Please select a file")
        else:
            if self.button_is_checked == False:
                self.button_is_checked = True
                self.uvSim.runSystem()
                self.button_is_checked = False  # reset button after system is finished

def main():
    app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    uv_sim = UVSim.UVSim()
    w = MainWindow()
    w.show()  # show main window
    sys.exit(app.exec())  # start event loop

if __name__ == '__main__':
    main()