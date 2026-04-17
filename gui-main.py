import tkinter as tk

root = tk.Tk()
root.title("The Cold Cave")

# --- DATA ABSTRACTION: LIST ---
scenarios = [
    "EMPTY SLOT", 
    "Scenario 1: Dark tunnel.\n1: Light match\n2: Walk in dark",
    "Scenario 2: Giant spider!\n1: Fight\n2: Sneak past",
    "Scenario 3: Mysterious lever.\n1: Pull it\n2: Ignore it",
    "Scenario 4: Ground is shaking!\n1: Run for exit\n2: Hide under rocks",
    "Scenario 5: A deep chasm!\n1: Try to jump\n2: Look for bridge"
]

scenario_number = 1
score = 0
history_log = "" # Global variable to store the 'Passed Room' text

def show_main_menu():
    global scenario_number, score, history_log
    scenario_number = 1
    score = 0
    history_log = "" # Reset history
    canvas.delete("all")
    canvas.create_rectangle(100, 50, 500, 150, fill="#B5AFA8")
    canvas.create_text(300, 100, text="Cave Escape", fill='white', font=("Helvetica", 25, "bold"))
    
    start_button = tk.Button(root, text="Start my Journey!", command=start_game)
    canvas.create_window(300, 210, window=start_button)

def start_game():
    update_display()

# --- STUDENT-DEVELOPED PROCEDURE ---
def process_move(choice_made):
    global scenario_number, score, history_log
    
    is_correct = False
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
        # Update the history log string
        history_log = history_log + "Passed Room " + str(scenario_number) + "... "
        print(history_log) # Keep console output as well
        
        scenario_number = scenario_number + 1
        update_display()
    else:
        game_over_message("You made the wrong choice and were lost!")

def update_display():
    canvas.delete("all")
    
    # Check for Win State
    if scenario_number > 5:
        win_text = "YOU ESCAPED!\nFinal Score: " + str(score)
        canvas.create_text(300, 200, text=win_text, fill="gold", font=("Arial", 20, "bold"), justify="center")
        win_button = tk.Button(root, text="Victory! Main Menu", command=show_main_menu)
        canvas.create_window(300, 300, window=win_button)
    else:
        # 1. Display Score at the top
        canvas.create_text(500, 30, text="Score: " + str(score), fill="white", font=("Arial", 12))
        
        # 2. Display Scenario Text
        msg = scenarios[scenario_number]
        canvas.create_text(300, 180, text=msg, fill="white", font=("Arial", 14), width=400, justify="center")
        
        # 3. Create Option Buttons
        btn1 = tk.Button(root, text="Option 1", command=clicked_1)
        btn2 = tk.Button(root, text="Option 2", command=clicked_2)
        canvas.create_window(200, 350, window=btn1)
        canvas.create_window(400, 350, window=btn2)

        # 4. Display "Passed Room" history BELOW options
        canvas.create_text(300, 430, text=history_log, fill="#AFAFAF", font=("Arial", 10), width=500, justify="center")

def clicked_1():
    process_move(1)

def clicked_2():
    process_move(2)

def game_over_message(reason):
    canvas.delete("all")
    full_message = reason + "\n\nFinal Score: " + str(score)
    canvas.create_text(300, 200, text=full_message, fill="red", font=("Arial", 14), width=400, justify="center")
    
    # Even on game over, show the progress they made
    canvas.create_text(300, 430, text="Your Progress: " + history_log, fill="gray", font=("Arial", 10))
    
    retry_button = tk.Button(root, text="Return to Start", command=show_main_menu)
    canvas.create_window(300, 320, window=retry_button)

canvas = tk.Canvas(root, width=600, height=500, bg="#664F64")
canvas.pack()

show_main_menu()
root.mainloop()
