import sys
from PyQt5 import QtCore, QtWidgets, QtSerialPort, QtGui

from widgets.mainwidgets import App

class UIController():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.ex = App()

        self._newserialinput = ""
        self._newDataPacket = ""

        self._serial_connected = False

    def set_screen_size(self, option: int = 0) -> None:
        screen_pixels = {
            0: [800, 480],
            1: [1600, 960],
            2: [2400, 1440],
            }
        width = screen_pixels[option][0]
        height = screen_pixels[option][1]

        self.ex.setGeometry(0, 0, width, height)



        tab_dimensions = f"height: {int(height/6)}px; width: {int(width/len(self.ex.tab_widget.all_tabs))}px;"
        
        co = "{"
        cc = "}"
        tab_style_sheet = f'''QTabBar::tab {co}{tab_dimensions}{cc} \n QTabWidget::tab-bar {{ alignment: center;}}'''

        fontsize = 4
        if option == 1 or option == 2:
            fontsize = 10

        self.ex.tab_widget.setFont(QtGui.QFont('Arial', fontsize))
        self.ex.tab_widget.setStyleSheet(tab_style_sheet)
        print(tab_style_sheet)
        

    def showUI(self) -> None:
        self.ex.show()
        sys.exit(self.app.exec_())

    def _updategraphs(self) -> None:
        self.ex.tab_widget.diagnosticstab.hertz_graph

    def _updatenumbers(self) -> None:
        #DataPackager.get_gps(x)

        #self.ex.tab_widget.diagnosticstab.hertz_graph.
        pass


    @property
    def newSerialInput(self):
        #print("setting")
        return self._newserialinput
    
    @newSerialInput.setter
    def newSerialInput(self, newInput):
      self._newserialinput = newInput

      self.ex.tab_widget.diagnosticstab.raw_serial_monitor.append(self.newSerialInput)

    @property
    def newDataPacket(self):
        #print("setting")
        return self._newDataPacket
    
    @newDataPacket.setter
    def newDataPacket(self, newInput):
      self._newDataPacket = newInput

      self.ex.tab_widget.diagnosticstab.data_monitor.append(self.newDataPacket)

    @property
    def serialConnected(self):
        return self._serial_connected
    
