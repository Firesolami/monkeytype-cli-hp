A simple Monkeytype terminal-based clone that utilizes text from the first book of the Harry Potter series.

## Requirements

- Python 3.x
- `curses` library (included with Python on Linux and macOS, use `windows-curses` on Windows)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/firesolami/monkeytype-cli-hp.git
    cd monkeytype-cli-hp
    ```

2. **Install dependencies:**

   - On Linux/macOS:
     ```bash
     sudo apt-get install python3
     ```
   - On Windows, install `windows-curses`:
     ```bash
     pip install windows-curses
     ```

3. **Prepare the text file:**

   Ensure the text file (`harryPotter.txt`) containing lines from the first Harry Potter book is in the same directory as the script. You can also replace it with any other text file of your choice.

## Usage

1. **Run the application:**
    ```bash
    python3 typing_test.py
    ```

2. **Type the displayed text:**
   - The application will display a random line from the first Harry Potter book.
   - Type the text as quickly and accurately as possible.

3. **After completing a test:**
   - Press 'y' to start another test, or press any other key to exit the application.



