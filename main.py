# Cave Adventure: AP CSP Performance Task Edition

# --- AP REQUIREMENT: DATA ABSTRACTION (LIST) ---
# This list stores the scenarios to manage program complexity[cite: 41, 55].
# It allows the program to handle multiple stages using a single variable[cite: 124].
scenarios = [
    "Entrance: A dark tunnel looms. 1: Light match, 2: Walk in dark.",              #0
    "The Pit: You find a narrow ledge. 1: Crawl slowly, 2: Run across.",            #1
    "The Guardian: A large bear is sleeping. 1: Sneak past, 2: Throw a rock.",      #2
    "The Choice: You see two paths. 1: Follow the breeze, 2: Go deeper down.",      #3
    "The Exit: A heavy stone door blocks the way. 1: Use lever, 2: Push door."      #4
]

scenario_index = 0

def show_main_menu():
    global scenario_index
    scenario_index = 0
    
    print("\n--- WELCOME TO THE COLD CAVE ---")
    
    # --- AP REQUIREMENT: INPUT FROM USER ---
    # Capturing the user's name for personalization[cite: 37, 94].
    user_name = input("Enter your name, Adventurer: ")
    print(f"Welcome, {user_name}! Your journey begins now.")
    
    start = input("Press 'S' to start or 'Q' to quit: ").upper()
    if start == "S":
        play_game()
    else:
        print(f"Safe travels, {user_name}.")

# --- AP REQUIREMENT: STUDENT-DEVELOPED PROCEDURE ---
# This procedure uses a parameter (user_choice)[cite: 116].
# It implements an algorithm with sequencing, selection, and iteration[cite: 117].
def check_choice(user_choice):
    global scenario_index
    is_correct = False
    
    # 1. Selection: Determining if the choice matches the 'correct' logic[cite: 280].
    # Logic: Scenarios 0, 2, 4 = '1'; Scenarios 1, 3 = '2'
    if scenario_index % 2 == 0:
        if user_choice == "1":
            is_correct = True
    else:
        if user_choice == "2":
            is_correct = True
            
    if is_correct:
        print("\nSuccess! You move deeper into the cave.")
        scenario_index = scenario_index + 1
        
        # 2. Iteration: A loop to show a progress bar[cite: 282].
        # This demonstrates a repetitive portion of an algorithm[cite: 282].
        progress_bar = ""
        for i in range(scenario_index):
            progress_bar += "█"
        print("Progress: " + progress_bar)
        
        return True
    else:
        print("\nFAILED: You made a fatal mistake!")
        return False

def play_game():
    global scenario_index
    
    # --- AP REQUIREMENT: OUTPUT BASED ON INPUT ---
    # The program provides visual/textual output as the user progresses[cite: 52, 96].
    while scenario_index < len(scenarios):
        # Accessing data from the list (Data Abstraction)[cite: 126, 267].
        print("\n" + scenarios[scenario_index])
        
        move = input("Enter your choice (1 or 2): ")
        
        # Calling the student-developed procedure[cite: 51, 118].
        result = check_choice(move)
        
        if result == False:
            print("You must return to the beginning to try again.")
            show_main_menu() # The "Redirect" requirement
            return 

    print("\nCONGRATULATIONS! You survived the Cold Cave!")
    show_main_menu()

# Start the program
show_main_menu()
