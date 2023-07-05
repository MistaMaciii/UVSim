from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QEventLoop
#Things to do handle file and run clicked again. Reset memory and gui views
class MainWindow(QMainWindow):
    def __init__(self, uvSimCallerIn):
        super(MainWindow, self).__init__()

        # Initialize UVSim
        self.uvSimCaller = uvSimCallerIn

        # Initialize file_path
        self.file_path = False
 #       # Initialize output string
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
        self.memory_textedit = QTextEdit(readOnly = True)
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
        self.run_button_is_checked = False
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
        main_layout.addWidget(self.input_line)
        self.input_button = QPushButton("Enter")
        self.input_button.clicked.connect(self.onSubmit)
        main_layout.addWidget(self.input_button)
        self.input_button.setVisible(False)

    def updateConsoleDisplay(self):
        self.uvSimOut = self.uvSimCaller.output
        self.console_output.append(self.uvSimOut)  # append new output
        self.console_output.setPlainText(self.uvSimOut)
        QApplication.processEvents()

    def update_memory_display(self):
        memory_text = "\n".join(self.uvSimCaller.memory.mem)
        self.memory_textedit.setPlainText(memory_text)

    def onToolBarFileButtonClick(self):
        # self.uvSim = UVSim.UVSim()  # initialize UVSim every file load
        if self.run_button_is_checked == False:
            #Run Loader func
            self.run_button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.uvSimCaller.loader.load_file(self.file_path)

            self.uvSimCaller.runLoader(self.file_path)
            
            self.memory_textedit.clear()
            self.update_memory_display()
            self.updateConsoleDisplay()
        self.run_button_is_checked = False  # reset button after system is finished

    def onToolBarRunButtonClick(self):
        # self.uvSim = UVSim.UVSim()  # initialize UVSim every file run
        if self.file_path == False:  # check if file_path exists
            self.uvSimOut += "No file selected. Please select a file\n"
            self.console_output.setPlainText(self.uvSimOut)
        else:
            if self.run_button_is_checked == False:
                self.input_line.setReadOnly(False)
                self.input_button.setVisible(True)
                self.run_button_is_checked = True
                self.console_output.clear()
                self.console_output.setPlainText(self.uvSimOut)  # update prompt
                QApplication.processEvents()  # Force immediate update of the console output
                self.input_line.clear()
                while self.uvSimCaller.runSystem() == 0:
                    # output to console "input please"
                    self.updateConsoleDisplay()
            self.run_button_is_checked = False
        # self.uvSim = UVSim.UVSim() # reset UVSim after runsys finish

    def onSubmit(self):
        self.close_event_loop()
        if self.run_button_is_checked == True:
            QApplication.processEvents()
            self.user_input = self.input_line.text()
            self.updateConsoleDisplay()

    def close_event_loop(self):
        if self.event_loop is not None:
            self.event_loop.quit()

    def wait_for_button(self):
        self.event_loop = QEventLoop()
        self.event_loop.exec()

    def update_displays(self):
        self.update_memory_display()
        self.updateConsoleDisplay()
    