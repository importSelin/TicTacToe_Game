"""
Tic Tac Toe Game 

"""
import random


class TicTacToe():
    
    def __init__(self):
        
        # constructor
        
        self.matrix = []
        self.player_xo = ""
        self.pc_xo = ""
        self.place = None
    
    
    def create_new_game(self):
        
        # create an empty matrix for new game
        
        for i in range(1):
            for j in range(3):
                self.matrix.append(["*", "*", "*"])
    
    def displaying_matrix(self):
        
        # to show the matrix during game
        
        for i in range(3):
            for j in range(1):
                print("{}   {}   {}".format(self.matrix[i][j], self.matrix[i][j+1], self.matrix[i][j+2]))
        
      
    def pc_turn(self):
        
        # when it is pc's turn to play
        
        while True:
            rowpc = random.randint(0,2)
            colpc = random.randint(0,2)
            
            if self.matrix[rowpc][colpc] == "*":
                self.matrix[rowpc][colpc] = self.pc_xo
                break
    
    def player_turn(self):
        
        # choosing the place by player  
        
        while True:
            input_place = input("Enter row and column number (ex. 11): ")
            input_place = int(input_place)
            row = (input_place//10) - 1
            col = (input_place - ((row + 1) * 10)) - 1
            
            if (0 <= row and row <= 2) and (0 <= col and col <= 2):
                if self.matrix[row][col] == "*":
                    place = [row, col]
                    self.place = place
                    self.matrix[row][col] = self.player_xo
                    break
                else:
                    print("This place is already full!")
            else: 
                print("You should enter numbers between 1 and 3!")
            
        
    def select_player_xo(self):
        
        # choosing X or O by player
        
        while True:
            player_xo = input("Select your item X or O: ")
            if player_xo == "X" or player_xo == "x":
                self.player_xo = "X"
                self.pc_xo = "O"
                break
            elif player_xo == "O" or player_xo == "o":
                self.player_xo = "O"
                self.pc_xo = "X"
                break
            else:
                print("Invalid select. Try Again.")

    def checking_place(self):
        
        # checks situation of win 
    
        row1 = [self.matrix[0][0], self.matrix[0][1], self.matrix[0][2]]
        row2 = [self.matrix[1][0], self.matrix[1][1], self.matrix[1][2]]
        row3 = [self.matrix[2][0], self.matrix[2][1], self.matrix[2][2]]
        
        col1 = [self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]]
        col2 = [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]]
        col3 = [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]]
        
        if all(element == "X" for element in row1) or all(element == "O" for element in row1):
            return True
        elif all(element == "X" for element in row2) or all(element == "O" for element in row2):
            return True
        elif all(element == "X" for element in row3) or all(element == "O" for element in row3):
            return True
        elif all(element == "X" for element in col1) or all(element == "O" for element in col1):
            return True
        elif all(element == "X" for element in col2) or all(element == "O" for element in col2):
            return True
        elif all(element == "X" for element in col3 or all(element == "O" for element in col3)):
            return True
        elif (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == "X") or (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == "O"):
            return True
        elif (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == "X") or (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == "O"):
            return True
        else:
            return False
            
            
def result_play(n):
    if n == 1:
        print("Congrats! You are the Winner! Let's play again!")
        n = 0
        play()
    elif n == 2:
        print("Sorry! You Lose! Let's play again!")
        n = 0
        play()
    elif n == 3:
        print("The Game ended in a draw! Let's play again!")
        n = 0
        play()
    else:
        n = 0
        exit()
        

def play():
    while True:
    
        print("""
            ****** TIC TAC TOE GAME *****  
            
            Welcome to Tic Tac Toe Game 
            
            Please select choice
            
            1. PLAY
            2. QUIT
            
            """)
    
        choice = input(">>>")
        choice = int(choice)
    
        if choice == 1:
            
            player = TicTacToe()
            player.create_new_game()
            player.displaying_matrix()
            print("The Game is Ready!!!")
            player.select_player_xo()
            if player.player_xo == "X":
                for i in range(5):
                    print("It is your turn to play!")
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(1)
                    player.player_turn()
                    player.displaying_matrix()
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(1)  
                    print("It is PC's turn to play!")
                    check_result = player.checking_place()                       
                    if check_result == 1:
                        result_play(2)
                    if i == 4:
                        result_play(3)
                    player.pc_turn()
                    player.displaying_matrix()
                    check_result = player.checking_place()                       
                    if check_result == 1:
                        result_play(2)
                result_play(3)
            
            elif player.player_xo == "O":
                for i in range(5):
                    print("It is PC's turn to play!")
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(2)
                    player.pc_turn()
                    player.displaying_matrix()
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(2)
                    print("It is your turn to play!")
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(1)   
                    player.player_turn()
                    player.displaying_matrix()
                    check_result = player.checking_place()
                    if check_result == 1:
                        result_play(1)                    
                result_play(3)
          
        elif choice == 2:
            print("THANK YOU, HAVE A GOOD DAY..")
            result_play(4)
        else:
            print("Invalid number! Please select valid number.")
            print("Starting Again...")
            
        
play()

            
        

