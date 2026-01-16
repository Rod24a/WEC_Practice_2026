from tkinter import * 
from tournament import Tournament
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

# MAIN TOURNAMENT
myTournament = None

# def number_of_players():
#     global num_players
#     try:
#         num_players = int(entry.get())
#         output_text.insert(END, f"Number of players set to: {num_players}\n")
#     except ValueError:
#         output_text.insert(END, "Please enter a valid number for players.\n")
#         num_players = None

def get_player_names():
    global player_names, num_players, myTournament
    text = players_text.get("1.0", END).strip()
    player_names = [line.strip() for line in text.split('\n') if line.strip()]
    num_players = len(player_names)

    if num_players == 0:
        output_text.insert(END, f"Please enter names\n")    
        return

    # output_text.insert(END, f"Player names retrieved: {player_names}\n")
    # check if there are duplicate names - there shouldnt be!
    if len(player_names) != len(set(player_names)):
        output_text.insert(END, f"ERROR: Name list contains duplicate names. Please make all names unique.\n")
        return


    if myTournament == None:
        myTournament = Tournament()
        myTournament.add_players(player_names)
        myTournament.start_single_elimination()
        output_text.insert(END, myTournament.get_output_buffer())
    

    draw_dummy_9_player_bracket()

def submit_match_results():
    global match_results, myTournament
    match_results = match_result_text.get("1.0", END).strip()
    # output_text.insert(END, f"Match results submitted: {match_results}\n")
    match_result_text.delete("1.0", END)    # clear textbox

    if " " not in match_results: # invalid format, no space
        output_text.insert(END, f"Invalid format!: (<match #> <winner name>)\n")
        return
    # assume first space is the delimiater
    index = match_results.index(" ")
    match_num = match_results[:index]
    winner_name = match_results[index+1:]

    if not match_num.isnumeric():   #invalid format, match number not number
        output_text.insert(END, f"Invalid format!: (<match #> <winner name>)\n")
        return

    if myTournament:
        myTournament.declare_matchup_winner(int(match_num), winner_name)
        output_text.insert(END, myTournament.get_output_buffer())
    

#create the main window
window = Tk()
window.title("Tournament Bracket Generator")
window.geometry("1440x720")

top_frame = Frame(window)
top_frame.pack(side='top', padx=40, pady=0)

# Create left frame for inputs
left_frame = Frame(window)
left_frame.pack(side='left', padx=40, pady=20)

# Create right frame for output text box
right_frame = Frame(window)
right_frame.pack(side='right', padx=20, pady=20)


label = Label(top_frame, text="Welcome to 🚗URNAMENT", font=("Arial", 12))
label.pack(pady=10)

##### Number of Players input section #####

#label for instructions
# instruction_label = Label(left_frame, text="Enter the number of players:", font=("Arial", 10))
# instruction_label.pack(pady=5, anchor='w')

#entry widget for number of players
# entry = Entry(left_frame, font=("Arial", 10))
# entry.pack(pady=10, anchor='w')

# number_of_players_button = Button(left_frame, text="Submit", font=("Arial", 10))
# number_of_players_button.pack(pady=10, anchor='w')
# number_of_players_button.config(command=number_of_players)
# number_of_players_button.config(bg="lightblue", fg="black")

##### Players Input Section #####

players_label = Label(left_frame, text="Enter the names of the player (one per line):", font=("Arial", 10))
players_label.pack(pady=2, anchor='w')
players_text = Text(left_frame, height=6, width=40, font=("Arial", 10))
players_text.pack(pady=2, anchor='w')

generate_bracket_button = Button(left_frame, text="Generate Bracket", font=("Arial", 10))
generate_bracket_button.pack(pady=2, anchor='w')
generate_bracket_button.config(command=get_player_names)



generate_bracket_button.config(bg="lightblue", fg="black")


###added for the 9 player bracket display


canvas = Canvas(right_frame, width=950, height=520, bg="white")
canvas.pack(pady=10)


#### Match result input Section ####
match_result_label = Label(left_frame, text="Enter match results (format: <match #> <winner name>)", font=("Arial", 10))
match_result_label.pack(pady=2, anchor='w')
match_result_text = Text(left_frame, height=2, width=40, font=("Arial", 10))
match_result_text.pack(pady=2, anchor='w') 
submit_results_button = Button(left_frame, text="Submit Match Results", font=("Arial", 10))
submit_results_button.pack(pady=2, anchor='w')
submit_results_button.config(bg="lightblue", fg="black")
submit_results_button.config(command=submit_match_results)


# Output text box on the left!
output_label = Label(left_frame, text="Output Information:", font=("Arial", 12))
output_label.pack(pady=2)
output_text = Text(left_frame, height=8, width=40, font=("Arial", 10))
output_text.pack(pady=2)

####### Make function to hard_code the player brackets all below is changed code

def draw_dummy_9_player_bracket():
    canvas.delete("all")

    def match_box(x, y, top_text, bot_text):
        w, h = 100, 44
        canvas.create_rectangle(x, y, x+w, y+h, outline="black")
        canvas.create_text(x+8, y+14, anchor="w", text=top_text)
        canvas.create_text(x+8, y+32, anchor="w", text=bot_text)
        return x+w, y+(h//2)

    def line(x1, y1, x2, y2):
        canvas.create_line(x1, y1, x2, y2, width=2)
    
    X_PLAYIN = 30
    X_QF     = 250
    X_SF     = 510
    X_F      = 770

    Y0, Y1, Y2, Y3, Y4 = 60, 150, 240, 330, 420

    # --- Play-in ---
    p = match_box(X_PLAYIN, Y4, "Player 8", "Player 9")  # P1

    # --- Quarterfinals ---
    q1 = match_box(X_QF, Y0, "Player 1", "Player 2")  # Q1
    q2 = match_box(X_QF, Y1, "Player 3", "Player 4")     # Q2
    q3 = match_box(X_QF, Y3, "Player 5", "Player 6")     # Q3
    q4 = match_box(X_QF, Y4, "Player 7", "Winner (P1)")     # Q4

    # Connect play-in to Q1
    line(p[0], p[1], X_QF, q4[1])

    # --- Semifinals ---
    s1 = match_box(X_SF, Y1, "Winner (Q1)", "Winner (Q4)")  # S1
    s2 = match_box(X_SF, Y3, "Winner (Q2)", "Winner (Q3)")  # S2

    # Connect quarters to semis
    line(q1[0], q1[1], X_SF, s1[1])
    line(q2[0], q2[1], X_SF, s1[1])

    line(q3[0], q3[1], X_SF, s2[1])
    line(q4[0], q4[1], X_SF, s2[1])

    # --- Final ---
    f = match_box(X_F, Y2, "Winner (S1)", "Winner (S2)")  # F1

    line(s1[0], s1[1], X_F, f[1])
    line(s2[0], s2[1], X_F, f[1])

    # output_text.insert(END, "Dummy 9-player bracket drawn.\n")
    # output_text.see(END)

#Moved from line 84, to hardcode 9 players
# generate_bracket_button.config(command=draw_dummy_9_player_bracket)


window.mainloop()