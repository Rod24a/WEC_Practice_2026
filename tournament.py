import math

all_matchup_index = 1

# simple binary tree node class for binary tree with only leaf nodes
class Node:
    def __init__(self, parent=None):
        self.current_name = ""
        # self.index = -1
        self.left = None
        self.right = None
        self.parent = parent

        self.matchup_index = -1
    
    def create_from_leaves(self, leaf_list):
        # list given as [['7 guy', '6 guy'], ['5guys', '4man'], ['3man', '2man'], 'BEST MAN']
        # ready for binary tree 

        if len(leaf_list) > 1:
            # split it in half and pass it down
            self.left = Node(self)
            self.left.create_from_leaves(leaf_list[:len(leaf_list)//2])
            self.right = Node(self)
            self.right.create_from_leaves(leaf_list[len(leaf_list)//2:])

            # if nodes both nodes are leaf nodes, create matchup in this node!
            # if self.left.current_name != "" and self.right.current_name != "":
            #     # create matchup in this node
            #     self.matchup_index = all_matchup_index
            #     all_matchup_index += 1

            # create matchup index in this node - no matter what
            # self.matchup_index = all_matchup_index
            # all_matchup_index += 1


        elif (len(leaf_list) == 1 and type(leaf_list[0]) == list):
            
            self.left = Node(self)
            self.left.create_from_leaves([leaf_list[0][0]])
            self.right = Node(self)
            self.right.create_from_leaves([leaf_list[0][1]])

            # if nodes both nodes are leaf nodes, create matchup
            # self.matchup_index = all_matchup_index
            # all_matchup_index += 1

        else:
            # you are a leaf node, just set name
            self.current_name = leaf_list[0]
            self.parent.check_new_matchup()
            

    def __str__(self):
        # if self.left == None and self.right == None:
        #     return self.current_name
        # else:
        #     return f"[{self.left}, {self.right}]"
        if self.current_name != "":
            return self.current_name
        else:
            return f"[{self.left}, {self.right}]"
    
    def declare_matchup_winner(self, matchup_id, winner):
        # print(f"AAAA my index is {self.matchup_index}")
        if self.matchup_index == matchup_id:
            # found matchup! make winner 
            # VERIFY IF WINNER IS ONE OF THE COMPETITORS
            if winner != self.left.current_name and winner != self.right.current_name:
                print(f"Invalid name! No '{winner}' found in matchup #{matchup_id}")
                return False

            
            self.current_name = winner
            if self.parent:
                self.parent.check_new_matchup()

        else:
            # check nodes
            if self.left:
                self.left.declare_matchup_winner(matchup_id, winner)
            if self.right:
                self.right.declare_matchup_winner(matchup_id, winner)
    
    def check_new_matchup(self):
        global all_matchup_index
        # print(f"checking new matchup")
        # check and print if your two nodes have two competitiors, and print
        if not self.left or not self.right:
            # print("no1")
            return
        if self.left.current_name == "" or self.right.current_name == "":
            # print(f"My child is {self.left.current_name} and right {self.right.current_name}")
            # print("no2")
            return
        
        self.matchup_index = all_matchup_index
        all_matchup_index += 1
        print(f"New Matchup #{self.matchup_index}: {self.left.current_name} VS {self.right.current_name}!")

    # def get_leaves(self):
    #     if self.name != "":
    #         return [self.name]
    #     else:
    #         return [self.left, self.right]

class Tournament:

    def __init__(self):
        self.num_players = 0
        self.player_list = []
        self.bracket = []   # used for keeping live tournament data
        
        self.root = None
        
    
    def add_player(self, name):
        self.player_list.append(name)
        self.num_players += 1


    def add_players(self, name_list):
        for name in name_list:
            self.add_player(name)
    
    def start_single_elimination(self):
        # assume player list was added from best to worst
        # single elimination bracket is just a binary tree
        # create binary tree from list, best players get byes if needed
        # error checking first though
        if self.num_players <= 1 or len(self.player_list) <= 1:
            return
        

        # tree_depth = pow(2, self.num_players - 1 - 1)
        # create tree depth of -1 then append the players to those nodes
        # add two players to leaf until number of players left = number of leaves left
        players_left = self.num_players
        temp_player_list = self.player_list[:]
        self.bracket = [None] * int(math.pow(2, int(math.log2(self.num_players))))
        
        for i in range(len(self.bracket)):
            
            if len(temp_player_list) > len(self.bracket)-i:
                # append two
                self.bracket[i] = [temp_player_list.pop(), temp_player_list.pop()]
            else:
                # player gets a bye, add only one
                self.bracket[i] = temp_player_list.pop()
        
        # ok now converge last layer into binary tree leaves
        self.root = Node()
        self.root.create_from_leaves(self.bracket)

    def declare_matchup_winner(self, matchup_id, name):
        self.root.declare_matchup_winner(matchup_id, name)

print("\n>>Initializing and adding players...")
myTourny = Tournament()
# myTourny.add_players(["BEST MAN", "2man", "3man", "4man", "5guys", "6 guy", "7 guy", "8"])
myTourny.add_players(["BEST MAN", "2man", "3man", "4man", "5guys"])
myTourny.start_single_elimination()
print("Curent bracket:", myTourny.root)

print("\n>>Setting winner in #1: '4man'")
myTourny.declare_matchup_winner(1, "4man")
print("Curent bracket:", myTourny.root)

print("\n>>Setting winner in #2: 'somebody'")
myTourny.declare_matchup_winner(2, "somebody")
print("Curent bracket:", myTourny.root)

print("\n>>Setting winner in #2: '2man'")
myTourny.declare_matchup_winner(2, "2man")
print("Curent bracket:", myTourny.root)

print("\n>>Setting winner in #3: '3man'")
myTourny.declare_matchup_winner(3, "3man")
print("Curent bracket:", myTourny.root)

print("\n>>Setting winner in #4: '3man'")
myTourny.declare_matchup_winner(4, "3man")
print("Curent bracket:", myTourny.root)