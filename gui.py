from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import UVSim
import Loader
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        # Initialize UVSim
        #self.uvSim = UVSim.UVSim()
        # Initialize Loader
        self.loader = Loader.Loader()
        # Initialize file_path
        self.file_path = False
        # Initialize output string
        self.uvSimOut = ""
        self.user_input = ""


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
        self.input_label = QLabel("Console Input")
        main_layout.addWidget(self.input_label)
        self.input_line = QLineEdit()
        self.input_line.setReadOnly(True)
        self.input_line.returnPressed.connect(self.onSubmit)  # Connect returnPressed signal
        self.input_line.selectionChanged.connect(self.onSubmit)
        main_layout.addWidget(self.input_line)
        self.input_button = QPushButton("Enter")
        self.input_button.clicked.connect(self.onSubmit)
        main_layout.addWidget(self.input_button)
        self.input_button.setVisible(False)


    def updateConsoleDisplay(self):
        self.uvSimOut = "HI"#self.uvSim.output
        self.console_output.append(self.uvSimOut)  # append new output
        self.console_output.setPlainText(self.uvSimOut)
        QApplication.processEvents()


    def update_memory_display(self, mem):
        memory_text = "\n".join(mem)
        self.memory_textedit.setPlainText(memory_text)


    def onToolBarFileButtonClick(self):
        # self.uvSim = UVSim.UVSim()  # initialize UVSim every file load
        self.loader = Loader.Loader()  # initialize Loader every file load
        if self.button_is_checked == False:
            self.button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.loader.load_file(self.file_path)
            self.memory_textedit.clear()
            mem = self.loader.memory.mem  # prints memory after loading file
            self.update_memory_display(mem)
            self.updateConsoleDisplay()
        self.button_is_checked = False  # reset button after system is finished

    def onToolBarRunButtonClick(self):
        # self.uvSim = UVSim.UVSim()  # initialize UVSim every file run
        if self.file_path == False:  # check if file_path exists
            self.uvSimOut += "No file selected. Please select a file\n"
            self.console_output.setPlainText(self.uvSimOut)
        else:
            if self.button_is_checked == False:
                self.input_line.setReadOnly(False)
                self.input_button.setVisible(True)
                self.button_is_checked = True
                self.console_output.clear()
                self.console_output.setPlainText(self.uvSimOut)  # update prompt
                QApplication.processEvents()  # Force immediate update of the console output
                self.input_line.clear()
                # while self.uvSim.runSystem() == 0:
                #     # output to console "input please"
                #     self.updateConsoleDisplay()
            self.button_is_checked = False
        # self.uvSim = UVSim.UVSim() # reset UVSim after runsys finish

    def onSubmit(self):
        if self.button_is_checked == True:
            QApplication.processEvents()
            self.process_input()
            self.uvSimOut += self.user_input + "\n"
            self.updateConsoleDisplay()
            while UVSim.IO_Operations.IO_Operations.read(self.uvSim.mem_loc, self.uvSim.memory, self.user_input) == 1:
                            #in error case of incorrect length
                            self.uvSimOut += "incorrect length\nEnter new input below\n"
                            self.updateConsoleDisplay()
                            # self.input_line.clear()
                            # self.process_input
                            # self.updateConsoleDisplay()
                            # self.uvSim.ip -= 1




            self.user_input = ""
           
    def process_input(self):
        while self.input_line.hasSelectedText() and len(self.input_line) > 3:        
            self.user_input = self.input_line.text(self.input_line.textChanged)




