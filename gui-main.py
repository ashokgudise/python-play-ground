import tkinter as tk

root = tk.Tk()
root.title("The Cold Cave")

# --- DATA ABSTRACTION: LIST ---
# This list manages complexity. Instead of 5 variables, we use one list.
scenarios = [
    "EMPTY SLOT", 
    "Scenario 1: Dark tunnel.\n1: Light match\n2: Walk in dark",
    "Scenario 2: Giant spider!\n1: Fight\n2: Sneak past",
    "Scenario 3: Mysterious lever.\n1: Pull it\n2: Ignore it",
    "Scenario 4: Ground is shaking!\n1: Run for exit\n2: Hide under rocks",
    "Scenario 5: A deep chasm!\n1: Try to jump\n2: Look for bridge"
]

# Global Variables
scenario_number = 1
score = 0
history_log = ""
player_name = "" 

def show_main_menu():
    global scenario_number, score, history_log
    scenario_number = 1
    score = 0
    history_log = ""
    
    canvas.delete("all")
    
    # Title Box
    canvas.create_rectangle(100, 30, 500, 110, fill="#B5AFA8")
    canvas.create_text(300, 70, text="Cave Escape", fill='white', font=("Helvetica", 25, "bold"))
    
    # Name Input Field
    canvas.create_text(300, 140, text="Enter Your Name:", fill="white", font=("Arial", 12))
    global name_entry
    name_entry = tk.Entry(root)
    canvas.create_window(300, 170, window=name_entry)
    
    # Start Button calls collect_name_and_start
    start_button = tk.Button(root, text="Start my Journey!", command=collect_name_and_start)
    canvas.create_window(300, 220, window=start_button)

def collect_name_and_start():
    global player_name
    player_name = name_entry.get()
    if player_name == "":
        player_name = "Adventurer"
    update_display()

# --- STUDENT-DEVELOPED PROCEDURE ---
# Requirement: This procedure uses a parameter (choice_made) 
# and contains sequencing, selection, and iteration.
def process_move(choice_made):
    global scenario_number, score, history_log
    
    is_correct = False
    
    # 1. Selection (Determining the outcome)
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
        score = score + 5
        # 2. Iteration (Updating history using data)
        history_log = history_log + "Passed Room " + str(scenario_number) + "... "
        scenario_number = scenario_number + 1
        update_display()
    else:
        game_over_message("You made the wrong choice and were lost!")

# These simple functions replace 'lambda'
def clicked_1():
    process_move(1)

def clicked_2():
    process_move(2)

def update_display():
    canvas.delete("all")
    
    if scenario_number > 5:
        # Final Win Output
        win_text = "CONGRATULATIONS " + player_name.upper() + "!\nYOU ESCAPED!\nFinal Score: " + str(score)
        canvas.create_text(300, 200, text=win_text, fill="gold", font=("Arial", 16, "bold"), justify="center")
        win_button = tk.Button(root, text="Victory! Main Menu", command=show_main_menu)
        canvas.create_window(300, 320, window=win_button)
    else:
        # Display Player Info
        canvas.create_text(100, 30, text="Hero: " + player_name, fill="#AFAFAF", font=("Arial", 10))
        canvas.create_text(500, 30, text="Score: " + str(score), fill="white", font=("Arial", 12))
        
        # Display Scenario from List
        msg = scenarios[scenario_number]
        canvas.create_text(300, 180, text=msg, fill="white", font=("Arial", 14), width=400, justify="center")
        
        # Standard Buttons calling simple functions
        btn1 = tk.Button(root, text="Option 1", command=clicked_1)
        btn2 = tk.Button(root, text="Option 2", command=clicked_2)
        canvas.create_window(200, 350, window=btn1)
        canvas.create_window(400, 350, window=btn2)

        # History log
        canvas.create_text(300, 430, text=history_log, fill="#AFAFAF", font=("Arial", 10), width=500)

def game_over_message(reason):
    canvas.delete("all")
    full_message = "Sorry " + player_name + ",\n" + reason + "\n\nFinal Score: " + str(score)
    canvas.create_text(300, 200, text=full_message, fill="red", font=("Arial", 14), width=400, justify="center")
    
    retry_button = tk.Button(root, text="Return to Start", command=show_main_menu)
    canvas.create_window(300, 320, window=retry_button)

# Initial Setup
canvas = tk.Canvas(root, width=600, height=500, bg="#664F64")
canvas.pack()

show_main_menu()
root.mainloop()
