import PySimpleGUI as sg
import random

# Function to start a new game
def new_game():
    return random.randint(1, 100), 0  # secret_number, attempts

# Initialize the game
secret_number, attempts = new_game()

# Window layout
layout = [
    [sg.Text("Guess a number between 1 and 100", key='-HEADER-')],
    [sg.Input(key='-IN-', size=(10,1)), sg.Button("Check", bind_return_key=True)],
    [sg.Text("", key='-OUT-', size=(40,1))],
    [sg.Button("Restart"), sg.Button("Quit")]
]

# Create the window
window = sg.Window("Guess the Number", layout)

while True:
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, "Quit"):
        break

    if event == "Restart":
        secret_number, attempts = new_game()
        window['-OUT-'].update("")
        window['-IN-'].update("")
        window['-HEADER-'].update("Guess a number between 1 and 100")
        continue

    if event == "Check":
        guess = values['-IN-']
        if not guess.isdigit():
            window['-OUT-'].update("Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == secret_number:
            window['-OUT-'].update(f"Correct! The number was {secret_number} in {attempts} attempts.")
        elif guess < secret_number:
            window['-OUT-'].update("Too low! Try again.")
        else:
            window['-OUT-'].update("Too high! Try again.")

window.close()
