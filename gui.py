from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QInputDialog, QPushButton, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt, QEventLoop, pyqtSignal
from os import path
class ColorButton(QtWidgets.QPushButton):
    '''
    Custom Qt Widget to show a chosen color.

    Left-clicking the button shows the color-chooser
    '''
    colorChanged = pyqtSignal(object)

    def __init__(self, *args, color="#4C721D", **kwargs):
        super(ColorButton, self).__init__(*args, **kwargs)

        self._color = "#4C721D"
        self._default = color
        self._oldColor = color
        self.pressed.connect(self.onColorPicker)

        # Set the initial/default state.
        self.setColor(self._default)

    def setColor(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit(color)

        if self._color:
            if self._color == "#000000":
                self._color = "#3b3b3b"
            self.setStyleSheet("background-color: %s;" % self._color)
        else:
            self.setStyleSheet("")

    def color(self):
        return self._color

    def onColorPicker(self):
        '''
        Show color-picker dialog to select color.

        Qt will use the native dialog by default.

        '''
        dlg = QtWidgets.QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QtGui.QColor(self._color))
        if dlg.exec():
            self.setColor(dlg.currentColor().name())

class MainWindow(QMainWindow):
    def __init__(self, uvSimCallerIn):
        super(MainWindow, self).__init__()

        # Initialize UVSim
        self.uvSimCaller = uvSimCallerIn

        # Initialize file_path
        self.file_path = False
        self.file_name = ""

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
        self.memory_textedit = QTextEdit(readOnly = True)
        main_layout.addWidget(self.memory_textedit)

        # Set toolbar
        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        # Add the 'file' selector button to the toolbar
        self.button_file = QAction("File...", )
        self.button_file.setStatusTip("Select the file to run")
        self.button_file.setToolTip("Ctrl+O")
        self.button_file.setShortcut("Ctrl+O")
        self.button_file.triggered.connect(self.onToolBarFileButtonClick)
        toolbar.addAction(self.button_file)

        # Add the 'Save' button
        self.button_save = QAction("Save")
        self.button_save.setStatusTip("Save changes to file")
        self.button_save.setToolTip("Ctrl+S")
        self.button_save.setShortcut("Ctrl+S")
        self.button_save.triggered.connect(self.onToolbarSave)
        toolbar.addAction(self.button_save)

        # Add the 'run' button to the toolbar
        self.button_run_program = QAction("Run", self)
        self.button_run_program.setStatusTip("Run the file through UVSim")
        self.button_run_program.setToolTip("Ctrl+R")
        self.button_run_program.setShortcut("Ctrl+R")
        self.button_run_program.triggered.connect(self.onToolBarRunButtonClick)
        toolbar.addAction(self.button_run_program)

        # Add the 'main color' button to the toolbar
        self.main_color = ColorButton()
        self.main_color.setStatusTip("Select main color for UVSim")
        toolbar.addWidget(self.main_color)

        # Add the 'secondary color' button to the toolbar
        self.second_color = ColorButton()
        self.second_color.setColor("#ffffff")
        self.second_color.setStatusTip("Select secondary color for UVSim")
        toolbar.addWidget(self.second_color)

        # Button 'Checker'
        self.button_is_checked = False

        # Add the 'Theme' button to the toolbar
        self.button_set_theme = QAction("Set Theme", self)
        self.button_set_theme.setStatusTip("Save theme changes")
        self.button_set_theme.triggered.connect(self.updateColors)
        toolbar.addAction(self.button_set_theme)

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
        self.input_line.returnPressed.connect(self.onSubmit)
        main_layout.addWidget(self.input_button)
        self.input_button.setVisible(False)

    def updateColors(self):
        self.setStyleSheet("""
        MainWindow {background-color: %s;}
        QToolBar {background-color: %s;}
        QTextEdit {background-color: %s;}
        QLineEdit {background-color: %s;}
        QPushButton {background-color: %s;}
        """
         % (self.main_color._color,self.second_color._color,self.second_color._color,self.second_color._color,self.second_color._color))

    def updateConsoleDisplay(self):
        self.uvSimOut = self.uvSimCaller.output
        self.console_output.append(self.uvSimOut)  # append new output
        self.console_output.setPlainText(self.uvSimOut)
        QApplication.processEvents()

    def update_memory_display(self):
        memory_text = "\n".join(self.uvSimCaller.memory.mem)
        self.memory_textedit.setPlainText(memory_text)

    def onToolBarFileButtonClick(self):
        if self.run_button_is_checked == False:
            self.uvSimCaller.resetForNewFile()
            #Run Loader func
            self.run_button_is_checked = True
            file_dialog = QFileDialog()
            self.file_path, _ = file_dialog.getOpenFileName(
                caption="Select File",
                directory=".",
                filter="All Files (*)")
            self.file_name = path.basename(self.file_path)
            self.uvSimCaller.loader.load_file(self.file_path)
            self.uvSimCaller.runLoader(self.file_path)
            self.memory_textedit.clear()
            self.update_memory_display()
            self.memory_textedit.setReadOnly(False) # let users edit file after load
            self.updateConsoleDisplay()
            self.console_output.setPlainText(self.uvSimCaller.loader.output)
        self.run_button_is_checked = False  # reset button after system is finished

    def onToolBarRunButtonClick(self):
        if self.file_path == False:  # check if file_path exists
            self.uvSimOut += "No file selected. Please select a file\n"
            self.console_output.setPlainText(self.uvSimOut)
        else:
            if self.run_button_is_checked == False:
                self.uvSimCaller.resetForNewRun()
                self.input_line.setReadOnly(False)
                self.input_button.setVisible(True)
                self.input_line.setFocus()
                self.run_button_is_checked = True
                self.console_output.clear()
                self.console_output.setPlainText(self.uvSimOut)  # update prompt
                QApplication.processEvents()  # Force immediate update of the console output
                self.uvSimCaller.runSystem()
                self.updateConsoleDisplay()
            self.run_button_is_checked = False

    def onToolbarSave(self):
        try:
            if self.file_path:
                with open(self.file_path, 'w', encoding="utf8") as f:
                    text = self.memory_textedit.toPlainText()
                    lines = text.split("\n")
                    if len(lines) > 100:
                        lines = lines[:100]  # Truncate the text to 99 characters
                        # Display a message to notify the user
                        QMessageBox.information(self, "Memory Truncated", "The memory has been truncated to size 100.")
                    text = "\n".join(lines)
                    f.write(text)
                self.uvSimCaller.resetForNewFile()
                #Run Loader func
                self.uvSimCaller.loader.load_file(self.file_path)
                self.uvSimCaller.runLoader(self.file_path)
                self.memory_textedit.clear()
                self.update_memory_display()
                self.updateConsoleDisplay()
                self.console_output.setPlainText(self.uvSimCaller.loader.output)

        except TypeError:
            self.uvSimOut += "Invalid file name\n"
            self.console_output.setPlainText(self.uvSimOut)

    def onSubmit(self):
        self.close_event_loop()
        if self.run_button_is_checked == True:
            QApplication.processEvents()
            self.user_input = self.input_line.text()
            self.updateConsoleDisplay()

    def close_event_loop(self):
        try:
            if self.event_loop is not None:
                self.event_loop.quit()
        except AttributeError: #on incorrect file load
            self.uvSimOut += "No file selected. Please select a file\n "
            self.console_output.setPlainText(self.uvSimOut)

    def wait_for_button(self):
        self.input_line.setFocus()
        self.event_loop = QEventLoop()
        self.event_loop.exec()

    def update_displays(self):
        # self.update_memory_display()
        self.updateConsoleDisplay()