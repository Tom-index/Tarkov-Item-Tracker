# Tarkov Item Tracker

Tarkov Item Tracker is a desktop application built with PySide6 that allows users to fetch and display information about items in the game Escape from Tarkov. It utilizes the Tarkov API to retrieve data and presents it in a user-friendly graphical interface.

## Features

- User can enter the name of an item from the game
- Application fetches item details from the Tarkov API
- Displays information such as item name, last low price, and tasks the item is used in
- Overlay window stays on top of other applications for easy access

## Requirements

- Python 3.x
- PySide6
- requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Tom-index/Tarkov-Item-Tracker.git
```

2. Navigate to the project directory:
```bash
cd Tarkov-Item-Tracker
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```
2. The Tarkov Item Tracker window will appear.
3. Enter the name of the item you want to look up and press Enter.
4. The application will fetch and display the item details in the window.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Escape from Tarkov](https://www.escapefromtarkov.com/) for the game and the API
- [PySide6](https://doc.qt.io/qtforpython/index.html) for the GUI framework
- [requests](https://requests.readthedocs.io/en/latest/) for making API requests