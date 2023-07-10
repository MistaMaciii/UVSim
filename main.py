import sys
import UVSim
from PyQt6.QtWidgets import QApplication

def main():
    uvSim = UVSim.UVSim()
    uvSim.guiSetup()

if __name__ == '__main__':
    main()
