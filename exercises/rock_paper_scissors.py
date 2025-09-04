import PySimpleGUI as sg
import random

# List of valid options
options = ["rock", "paper", "scissors"]

# Dict with winning cases
winning_cases = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

layout = [
    [sg.Text("Choose Rock, Paper or Scissors:")],
    [sg.Button("Rock"), sg.Button("Paper"), sg.Button("Scissors")],
    [sg.Text("", key="-RESULT-", size=(40,1))],
    [sg.Button("Restart"), sg.Button("Quit")]
]

window = sg.Window("Rock Paper Scissors", layout)

while True:
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, "Quit"):
        break
    
    if event.lower() in options:
        user_choice = event.lower()
        computer_choice = random.choice(options)
        
        if user_choice == computer_choice:
            result = f"Draw! Computer chose {computer_choice}."
        elif winning_cases[user_choice] == computer_choice:
            result = f"You win! Computer chose {computer_choice}."
        else:
            result = f"You lose! Computer chose {computer_choice}."
        
        window["-RESULT-"].update(result)
    
    if event == "Restart":
        window["-RESULT-"].update("")

window.close()
