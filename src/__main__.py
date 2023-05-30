
import sys

from PyQt5 import QtWidgets

from application import RealTimeDashboard

def main():
    # Create an instance of the QApplication class
    system = QtWidgets.QApplication(sys.argv)

    # Create your main window here
    app = RealTimeDashboard()

    # Show the main window
    app.show()

    # Start the event loop
    system.exec()


if __name__ == '__main__':
    main()
    