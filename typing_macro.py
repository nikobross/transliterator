from pynput.keyboard import Key, Controller, Listener
import textwrap
import time

def type_string():
    """
    Simulates typing the given string on the keyboard.
    """
    string_to_type = (
        "Response\n"
        "When using a typewriter, going back and fixing mistakes isn’t as simple as moving\n"
        "your cursor and rewriting. This forces you to be much more conscious and\n"
        "thoughtful about the words you choose before you even start typing. I found\n"
        "myself coming up with what I wanted to write ahead of time. Only being able to\n"
        "press one key at a time also significantly slowed down my typing speed and often\n"
        "caused me to accidentally skip letters. If I had to do work on a typewriter, I\n"
        "would work much more slowly, but I might end up writing better overall, as I\n"
        "would be thinking more carefully about each word.\n"
    )

    keyboard = Controller()
    for char in string_to_type:
        if char.isupper():  # Check if the character is uppercase
            keyboard.press(Key.shift)  # Press the shift key
            keyboard.type(char.lower())  # Type the lowercase version of the character
            keyboard.release(Key.shift)  # Release the shift key
        else:
            keyboard.type(char)  # Type the character as is
        
        if char == '\n':  # If the character is a return character
            time.sleep(1.5)  # Wait 1 second
        else:
            time.sleep(0.2)  # Wait 0.2 seconds between each key press

def on_press(key):
    """
    Listens for key presses and triggers the macro when the 'Right Shift' key is pressed.
    """
    print(f"Key pressed: {key}")  # Print the key pressed
    if key == Key.shift_r:  # Check if the 'Right Shift' key is pressed
        print("Right Shift key pressed")  # Print when the 'Right Shift' key is pressed
        type_string()

def main():
    """
    Starts the key listener.
    """
    print("Listening for the 'option' key. Press 'Ctrl + C' to exit.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()