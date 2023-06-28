import UVSim
import sys
from Operations.IO_Operations import IO_Operations
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize UVSim
        self.uvSim = UVSim.UVSim()
        # Initialize file_path
        self.file_path = False
        # Initialize output string
        self.uvSimOut = ""

        # Main Layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)

        # Set main window
        self.setWindowTitle("UVSim")
        label = QLabel("")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(500, 550)

        # Label for memory contents
        mem_label = QLabel("Memory")
        main_layout.addWidget(mem_label)

        # Set textedit to display memory contents
        self.memory_textedit = QTextEdit()
        self.memory_textedit.setReadOnly(True)

        # Add QTextEdit to the QVBoxLayout
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

        # Add the Console Output View
        console_label = QLabel("Console Output")
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        main_layout.addWidget(console_label)
        main_layout.addWidget(self.console_output)

        # Add the Console Input View

        self.input_line = QLineEdit()
        self.input_line.returnPressed.connect(self.onInputButtonClick)  # Connect returnPressed signal
        main_layout.addWidget(self.input_line)
        input_button = QPushButton("Enter")
        input_button.clicked.connect(self.onInputButtonClick)
        main_layout.addWidget(input_button)

    def updateConsoleDisplay(self):
        self.uvSimOut = self.uvSim.output
        self.console_output.append(self.uvSimOut)  # append new output

    def update_memory_display(self, mem):
        memory_text = "\n".join(mem)
        self.memory_textedit.setPlainText(memory_text)

    def onToolBarFileButtonClick(self):
        self.uvSim = UVSim.UVSim()  # initialize UVSim every file load
        if self.button_is_checked == False:
            self.button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.uvSim.loadFile(self.file_path)
            self.memory_textedit.clear()
            mem = self.uvSim.mem  # prints memory after loading file
            self.update_memory_display(mem)
            self.updateConsoleDisplay()
            self.button_is_checked = False  # reset button after system is finished

    def onToolBarRunButtonClick(self):
        if self.file_path == False:  # check if file_path exists
            self.uvSimOut += "No file selected. Please select a file\n"
            self.console_output.setPlainText(self.uvSimOut)
            print("No file selected. Please select a file")
        else:
            if self.button_is_checked == False:
                self.button_is_checked = True
                self.console_output.clear()
                self.uvSimOut += "Input a word(+1234):" + "\n"
                self.console_output.setPlainText(self.uvSimOut)  # update prompt
                QApplication.processEvents()  # Force immediate update of the console output
                self.button_is_checked = False  # reset button after system is finished

                user_input = self.input_line.text()
                self.input_line.clear()
                
                if user_input:
                    self.uvSim.runSystem(user_input)
                self.updateConsoleDisplay()

    def onInputButtonClick(self):
        self.onToolBarRunButtonClick()


def main():
    app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    w = MainWindow()
    w.show()  # show main window
    sys.exit(app.exec())  # start event loop


if __name__ == '__main__':
    main()