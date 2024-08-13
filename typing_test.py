import curses
import random
import time

class TypingTest:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.reset_test()

        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def reset_test(self):
        self.to_type_text = self.get_line_to_type()
        self.user_typed_text = []
        self.wpm = 0
        self.start_time = time.time()

    def get_line_to_type(self):
        with open("harryPotter.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        return random.choice(lines).strip()

    def calculate_wpm(self):
        time_elapsed = max(time.time() - self.start_time, 1)
        self.wpm = round((len(self.user_typed_text) / (time_elapsed / 60)) / 5)

    def calculate_accuracy(self):
        total_characters = min(len(self.user_typed_text), len(self.to_type_text))
        if total_characters == 0:
            return 0.0
        matching_characters = sum(1 for current_char, target_char in zip(self.user_typed_text, self.to_type_text) if current_char == target_char)
        return round((matching_characters / total_characters) * 100, 2)

    def display_wpm(self):
        self.stdscr.addstr(1, 0, f"WPM: {self.wpm}", curses.color_pair(3))

    def display_accuracy(self):
        self.stdscr.addstr(2, 0, f"Accuracy: {self.calculate_accuracy():.2f}%", curses.color_pair(3))

    def display_typed_chars(self):
        for i, char in enumerate(self.user_typed_text):
            correct_character = self.to_type_text[i]
            color = 1 if char == correct_character else 2
            self.stdscr.addstr(4, i, char, curses.color_pair(color))

    def display_details(self):
        self.stdscr.addstr(0, 0, "Type the following:", curses.color_pair(3))
        self.stdscr.addstr(3, 0, self.to_type_text)
        self.display_typed_chars()

    def run_test(self):
        self.stdscr.nodelay(True)

        while True:
            self.stdscr.clear()
            self.display_details()
            self.stdscr.refresh()

            if "".join(self.user_typed_text) == self.to_type_text or len(self.user_typed_text) == len(self.to_type_text):
                self.stdscr.nodelay(False)
                break

            try:
                key = self.stdscr.getkey()
            except Exception:
                continue

            if isinstance(key, str) and len(key) == 1 and ord(key) == 27:
                break

            if not self.user_typed_text:
                self.start_time = time.time()

            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if self.user_typed_text:
                    self.user_typed_text.pop()
            elif len(self.user_typed_text) < len(self.to_type_text):
                self.user_typed_text.append(key)

        self.calculate_wpm()
        self.stdscr.clear()
        self.display_details()
        self.display_wpm()
        self.display_accuracy()
        self.stdscr.refresh()

        self.stdscr.addstr(4, 0, "\nPress 'y' to start another test, or any other key to exit.", curses.color_pair(3))
        key = self.stdscr.getkey()

        if key.lower() == 'y':
            self.reset_test()
            self.run_test()

def main(stdscr):
    typing_test = TypingTest(stdscr)
    typing_test.run_test()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except:
        print("An error occurred")
