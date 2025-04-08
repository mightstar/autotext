# AutoText

A Windows application that automatically replaces predefined shortcuts with longer text phrases.

## Features

- Monitor keyboard input for predefined shortcuts
- Replace shortcuts with corresponding text from an Excel file
- Works system-wide on Windows 11
- Easy to configure shortcuts through Excel file

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure your shortcuts in the `shortcuts.xlsx` file:
   - Column A: key (the shortcut you want to type)
   - Column B: text (the text that will replace the shortcut)

2. Run the application:
   ```
   python autotext.py
   ```

3. The application will run in the background and monitor your keyboard input
4. Type any configured shortcut (e.g., "/linkedin") and it will be automatically replaced with the corresponding text
5. Press ESC to exit the application

## Example

If you type "/linkedin" anywhere in your system, it will be automatically replaced with "https://linkedin.com/in/james" (or whatever text you've configured in the Excel file).

## Notes

- The application needs to be running for the shortcuts to work
- Make sure the `shortcuts.xlsx` file is in the same directory as the script
- The Excel file must have columns named "key" and "text" 