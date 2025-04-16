import sys
from PyQt5.QtWidgets import QApplication
from gui.interface import Interface
from arduino.controller import ArduinoController

def main():
    app = QApplication(sys.argv)
    
    arduino_controller = ArduinoController()
    arduino_controller.connect()
    
    interface = Interface(arduino_controller)
    interface.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()