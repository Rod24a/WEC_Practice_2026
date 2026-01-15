from tkinter import * 

## My idea of how this works: 
## 1. User inputs number of players
## 2. User inputs player names
## 3. Backend generates brackets and displays matches like: Match 1: Player A vs Player B
## 4. User inputs match results in the format: # Winner Name
## 5. Backend reads number of match and winner and updates brackets. 

## when your function needs to print just call: 
## output_text.insert(END, "stirng\n")

# Global variable for number of players
num_players = None

# Global variable for list of player names
player_names = []

# Global string for match results
match_results = ""

def number_of_players():
    global num_players
    try:
        num_players = int(entry.get())
        output_text.insert(END, f"Number of players set to: {num_players}\n")
    except ValueError:
        output_text.insert(END, "Please enter a valid number for players.\n")
        num_players = None

def get_player_names():
    global player_names
    text = players_text.get("1.0", END).strip()
    player_names = [line.strip() for line in text.split('\n') if line.strip()]
    output_text.insert(END, f"Player names retrieved: {player_names}\n")
    if num_players and len(player_names) != num_players:
        output_text.insert(END, f"Warning: Number of names ({len(player_names)}) doesn't match the set number of players ({num_players}).\n")

def submit_match_results():
    global match_results
    match_results = match_result_text.get("1.0", END).strip()
    output_text.insert(END, f"Match results submitted:\n{match_results}\n")

#create the main window
window = Tk()
window.title("Tournament Bracket Generator")
window.geometry("1000x900")

# Create left frame for inputs
left_frame = Frame(window)
left_frame.pack(side='left', padx=40, pady=20)

# Create right frame for output text box
right_frame = Frame(window)
right_frame.pack(side='right', padx=100, pady=20)

label = Label(left_frame, text="Welcome to the Tournament Bracket Generator!", font=("Arial", 12))
label.pack(pady=20)

##### Number of Players input section #####

#label for instructions
instruction_label = Label(left_frame, text="Enter the number of players:", font=("Arial", 10))
instruction_label.pack(pady=5, anchor='w')

#entry widget for number of players
entry = Entry(left_frame, font=("Arial", 10))
entry.pack(pady=10, anchor='w')

number_of_players_button = Button(left_frame, text="Submit", font=("Arial", 10))
number_of_players_button.pack(pady=10, anchor='w')
number_of_players_button.config(command=number_of_players)
number_of_players_button.config(bg="lightblue", fg="black")

##### Players Input Section #####

players_label = Label(left_frame, text="Enter the names of the players (one per line):", font=("Arial", 10))
players_label.pack(pady=5, anchor='w')
players_text = Text(left_frame, height=10, width=40, font=("Arial", 10))
players_text.pack(pady=10, anchor='w')

generate_bracket_button = Button(left_frame, text="Generate Bracket", font=("Arial", 10))
generate_bracket_button.pack(pady=10, anchor='w')
generate_bracket_button.config(command=get_player_names)
generate_bracket_button.config(bg="lightblue", fg="black")

# Output text box on the right
output_label = Label(right_frame, text="Output Information:", font=("Arial", 12))
output_label.pack(pady=5)
output_text = Text(right_frame, height=30, width=60, font=("Arial", 10))
output_text.pack(pady=10)


#### Match result input Section ####
match_result_label = Label(left_frame, text="Enter match results (format: # Winner Name)", font=("Arial", 10))
match_result_label.pack(pady=5, anchor='w')
match_result_text = Text(left_frame, height=10, width=40, font=("Arial", 10))
match_result_text.pack(pady=10, anchor='w') 
submit_results_button = Button(left_frame, text="Submit Match Results", font=("Arial", 10))
submit_results_button.pack(pady=10, anchor='w')
submit_results_button.config(bg="lightblue", fg="black")
submit_results_button.config(command=submit_match_results)


window.mainloop()