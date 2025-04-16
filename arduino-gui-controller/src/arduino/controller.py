class ArduinoController:
    def __init__(self, port):
        self.port = port
        self.connection = None

    def connect(self):
        import serial
        try:
            self.connection = serial.Serial(self.port, 9600)
            return True
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")
            return False

    def send_command(self, command):
        if self.connection and self.connection.is_open:
            self.connection.write(command.encode())

    def read_data(self):
        if self.connection and self.connection.is_open:
            return self.connection.readline().decode().strip()