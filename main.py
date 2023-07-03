import sys
import gui
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    with open("style.css", "r") as file:    #opens file for css styles
        app.setStyleSheet(file.read())
    w = gui.MainWindow()
    w.show()  # show main window
    sys.exit(app.exec())  # start event loop

if __name__ == '__main__':
    main()
