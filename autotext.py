import pandas as pd
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import sys
import os

class AutoText:
    def __init__(self):
        self.keyboard = Controller()
        self.buffer = ""
        self.shortcuts = self.load_shortcuts()
        self.listener = None
        self.typing_delay = 0.02  # 20ms delay between characters
        self.is_typing = False
        self.current_text = ""
        self.current_position = 0

    def load_shortcuts(self):
        try:
            df = pd.read_excel('shortcuts.xlsx')
            return dict(zip(df['key'], df['text']))
        except Exception as e:
            print(f"Error loading shortcuts: {e}")
            return {}

    def on_press(self, key):
        try:
            if key == Key.esc and self.is_typing:
                # Stop current typing progress
                self.is_typing = False
                print("Typing interrupted. Press ESC again to exit.")
                return True
            elif key == Key.esc and not self.is_typing:
                # Exit the application
                print("Exiting AutoText...")
                return False
            elif hasattr(key, 'char') and not self.is_typing:
                self.buffer += key.char
                # Check if buffer matches any shortcut
                for shortcut, text in self.shortcuts.items():
                    if self.buffer.endswith(shortcut):
                        # Delete the shortcut text
                        for _ in range(len(shortcut)):
                            self.keyboard.press(Key.backspace)
                            self.keyboard.release(Key.backspace)
                            time.sleep(0.02)  # Small delay when deleting
                        
                        # Start typing the replacement text
                        self.is_typing = True
                        self.current_text = text
                        self.current_position = 0
                        self.type_next_character()
                        self.buffer = ""
                        break
        except Exception as e:
            print(f"Error in on_press: {e}")
            self.is_typing = False
            return True

    def type_next_character(self):
        if not self.is_typing or self.current_position >= len(self.current_text):
            self.is_typing = False
            return
        
        # Type the next character
        self.keyboard.type(self.current_text[self.current_position])
        self.current_position += 1
        
        # Schedule the next character
        if self.current_position < len(self.current_text):
            time.sleep(self.typing_delay)
            self.type_next_character()

    def on_release(self, key):
        pass

    def start(self):
        print("AutoText is running... Press ESC once to stop current typing, twice to exit.")
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

if __name__ == "__main__":
    auto_text = AutoText()
    auto_text.start() 