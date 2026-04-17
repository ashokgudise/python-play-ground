import tkinter as tk

root = tk.Tk()
root.title("The Cold Cave")

# --- AP CSP REQUIREMENT: LIST (DATA ABSTRACTION) ---
# This list stores the story text for each scenario. 
# It manages complexity by allowing us to access any scenario using an index.
scenarios = [
    "EMPTY SLOT", # Index 0 (not used)
    "Scenario 1: Dark tunnel.\n1: Light match\n2: Walk in dark",
    "Scenario 2: Giant spider!\n1: Fight\n2: Sneak past",
    "Scenario 3: Mysterious lever.\n1: Pull it\n2: Ignore it",
    "Scenario 4: Ground is shaking!\n1: Run for exit\n2: Hide under rocks",
    "Scenario 5: A deep chasm!\n1: Try to jump\n2: Look for bridge"
]

scenario_number = 1

def show_main_menu():
    global scenario_number
    scenario_number = 1
    canvas.delete("all")
    canvas.create_rectangle(100, 50, 500, 150, fill="#B5AFA8")
    canvas.create_text(300, 100, text="Cave Escape", fill='white', font=("Helvetica", 25, "bold"))
    
    start_button = tk.Button(root, text="Start my Journey!", command=start_game)
    canvas.create_window(300, 210, window=start_button)

def start_game():
    update_display()

# --- AP CSP REQUIREMENT: STUDENT-DEVELOPED PROCEDURE ---
# This procedure uses a parameter (choice_made) and contains:
# 1. Sequencing (running steps in order)
# 2. Selection (if/elif statements)
# 3. Iteration (the for loop checking progress)
def process_move(choice_made):
    global scenario_number
    
    # 1. Selection: Determine if the choice was right for the current scenario
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
        scenario_number = scenario_number + 1
        
        # 2. Iteration: A loop to 'scan' through past progress (for complexity requirement)
        history_log = ""
        for i in range(1, scenario_number):
            history_log = history_log + "Passed Room " + str(i) + "... "
        print(history_log)
        
        update_display()
    else:
        game_over_message("You made the wrong choice and were lost in the cave forever!")

def update_display():
    canvas.delete("all")
    
    # Check if we won
    if scenario_number > 5:
        canvas.create_text(300, 200, text="YOU ESCAPED!", fill="gold", font=("Arial", 20, "bold"))
        win_button = tk.Button(root, text="Victory! Main Menu", command=show_main_menu)
        canvas.create_window(300, 300, window=win_button)
    else:
        # AP CSP Requirement: Accessing data from a List
        msg = scenarios[scenario_number]
        
        canvas.create_text(300, 200, text=msg, fill="white", font=("Arial", 14), width=400)
        
        # Using separate functions for clicks to keep it simple for high school level
        btn1 = tk.Button(root, text="Option 1", command=clicked_1)
        btn2 = tk.Button(root, text="Option 2", command=clicked_2)
        canvas.create_window(200, 400, window=btn1)
        canvas.create_window(400, 400, window=btn2)

# Choice functions that call our main procedure with arguments
def clicked_1():
    process_move(1)

def clicked_2():
    process_move(2)

def game_over_message(reason):
    canvas.delete("all")
    canvas.create_text(300, 200, text=reason, fill="red", font=("Arial", 14), width=400)
    retry_button = tk.Button(root, text="Return to Start", command=show_main_menu)
    canvas.create_window(300, 300, window=retry_button)

canvas = tk.Canvas(root, width=600, height=500, bg="#664F64")
canvas.pack()

show_main_menu()
root.mainloop()
