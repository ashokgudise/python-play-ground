import tkinter as tk

root = tk.Tk()
root.title("The Cold Cave")

# --- AP CSP REQUIREMENT: LIST (DATA ABSTRACTION) ---
scenarios = [
    "EMPTY SLOT", 
    "Scenario 1: Dark tunnel.\n1: Light match\n2: Walk in dark",
    "Scenario 2: Giant spider!\n1: Fight\n2: Sneak past",
    "Scenario 3: Mysterious lever.\n1: Pull it\n2: Ignore it",
    "Scenario 4: Ground is shaking!\n1: Run for exit\n2: Hide under rocks",
    "Scenario 5: A deep chasm!\n1: Try to jump\n2: Look for bridge"
]

scenario_number = 1
# New variable to track the score
score = 0

def show_main_menu():
    global scenario_number, score
    scenario_number = 1
    score = 0 # Reset score when returning to menu
    
    canvas.delete("all")
    canvas.create_rectangle(100, 50, 500, 150, fill="#B5AFA8")
    canvas.create_text(300, 100, text="Cave Escape", fill='white', font=("Helvetica", 25, "bold"))
    
    start_button = tk.Button(root, text="Start my Journey!", command=start_game)
    canvas.create_window(300, 210, window=start_button)

def start_game():
    update_display()

# --- AP CSP REQUIREMENT: STUDENT-DEVELOPED PROCEDURE ---
def process_move(choice_made):
    global scenario_number, score
    
    is_correct = False
    
    # Logic to determine if the choice is correct
    if scenario_number == 1 and choice_made == 1:
        is_correct = True
    elif scenario_number == 2 and choice_made == 2:
        is_correct = True
    elif scenario_number == 3 and choice_made == 1:
        is_correct = True
    elif scenario_number == 4 and choice_made == 2:
        is_correct = True
    elif scenario_number == 5 and choice_made == 1:
        is_correct = True

    if is_correct:
        # Increase score by 5 for every correct answer
        score = score + 5
        scenario_number = scenario_number + 1
        
        # Iteration requirement
        history_log = ""
        for i in range(1, scenario_number):
            history_log = history_log + "Passed Room " + str(i) + "... "
        print(history_log)
        
        update_display()
    else:
        # If wrong, go to game over and show the final score
        game_over_message("You made the wrong choice and were lost!")

def update_display():
    canvas.delete("all")
    
    # Check if we won
    if scenario_number > 5:
        # Displaying Final Score on Win
        win_text = "YOU ESCAPED!\nFinal Score: " + str(score)
        canvas.create_text(300, 200, text=win_text, fill="gold", font=("Arial", 20, "bold"), justify="center")
        
        win_button = tk.Button(root, text="Victory! Main Menu", command=show_main_menu)
        canvas.create_window(300, 300, window=win_button)
    else:
        # Show current score while playing
        canvas.create_text(500, 30, text="Score: " + str(score), fill="white", font=("Arial", 12))
        
        msg = scenarios[scenario_number]
        canvas.create_text(300, 200, text=msg, fill="white", font=("Arial", 14), width=400)
        
        btn1 = tk.Button(root, text="Option 1", command=clicked_1)
        btn2 = tk.Button(root, text="Option 2", command=clicked_2)
        canvas.create_window(200, 400, window=btn1)
        canvas.create_window(400, 400, window=btn2)

def clicked_1():
    process_move(1)

def clicked_2():
    process_move(2)

def game_over_message(reason):
    canvas.delete("all")
    # Displaying Final Score on Loss
    full_message = reason + "\n\nFinal Score: " + str(score)
    
    canvas.create_text(300, 200, text=full_message, fill="red", font=("Arial", 14), width=400, justify="center")
    
    retry_button = tk.Button(root, text="Return to Start", command=show_main_menu)
    canvas.create_window(300, 320, window=retry_button)

canvas = tk.Canvas(root, width=600, height=500, bg="#664F64")
canvas.pack()

show_main_menu()
root.mainloop()
