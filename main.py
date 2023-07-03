import sys
import gui
from PyQt6.QtWidgets import QApplication




def main():
    app = QApplication(sys.argv)  # Open the QApp through MainWindow class with command line options
    w = gui.MainWindow()
    w.show()  # show main window
    sys.exit(app.exec())  # start event loop


if __name__ == '__main__':
    main()