# Arduino GUI Controller

This project provides a graphical user interface (GUI) to control an Arduino project. It allows users to interact with the Arduino board through a user-friendly interface, sending commands and receiving data.

## Project Structure

```
arduino-gui-controller
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui
│   │   └── interface.py # GUI management
│   ├── arduino
│   │   └── controller.py # Arduino communication
│   └── utils
│       └── helpers.py   # Utility functions
├── requirements.txt     # Project dependencies
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd arduino-gui-controller
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Connect your Arduino board to your computer.

4. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Use the GUI to send commands to the Arduino and view the data received.
- Ensure that the correct COM port is selected in the application settings for proper communication with the Arduino.

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.