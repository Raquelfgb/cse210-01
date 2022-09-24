
from tkinter import * 
from tkinter import messagebox
import random
import pytest

count=0

ttt_board = ["-", "-", "-", "-", "-", "-","-", "-", "-"]
player = "X"
winner = None
running_game = True

def main():
    if running_game == False:
        answer = input("Would you like to play again? ")
        if answer == "yes":
            running_game
        else:
            print("Thank you for playing Tic Tac Toe")

    while running_game:
        show_board(ttt_board)
        pl_player(ttt_board)
        winning()
        tie(ttt_board)
        change_player()
        computer(ttt_board)
        """winning()
        tie(ttt_board)"""

def show_board(ttt_board):
    print(ttt_board[0] + " | " + ttt_board[1] + " | " + ttt_board[2])
    print("----------")
    print(ttt_board[3] + " | " + ttt_board[4] + " | " + ttt_board[5])
    print("----------")
    print(ttt_board[6] + " | " + ttt_board[7] + " | " + ttt_board[8])


def pl_player(ttt_board):
    pl=int(input("Enter the position you want to play considering numbers from 1-9: "))
    # position 1 2 3
    # position 4 5 6
    # position 7 8 9 
    # I wonder if that is clear for the player
    if pl>=1 and pl<=9 and ttt_board[pl-1] == "-":
       ttt_board[pl-1] = player 
    else:
        print("Sorry, you can't put it in that spot")

def horizontal(ttt_board):
    global winner
    if ttt_board[0] == ttt_board[1] == ttt_board[2] and ttt_board[0]!= "-":
        winner = ttt_board[0]
        return True
    elif ttt_board[3] == ttt_board[4] == ttt_board[5] and ttt_board[3]!= "-":
        winner = ttt_board[3]
        return True
    elif ttt_board[6] == ttt_board[7] == ttt_board[8] and ttt_board[6]!= "-":
        winner = ttt_board[6]
        return True

def vertical(ttt_board):
    global winner
    if ttt_board[0] == ttt_board[3] == ttt_board[6] and ttt_board[0]!= "-":
        winner = ttt_board[0]
        return True
    elif ttt_board[1] == ttt_board[4] == ttt_board[7] and ttt_board[1]!= "-":
        winner = ttt_board[1]
        return True
    elif ttt_board[2] == ttt_board[5] == ttt_board[8] and ttt_board[2]!= "-":
        winner = ttt_board[2]
        return True

def diagonal(ttt_board):
    global winner
    if ttt_board[0] == ttt_board[4] == ttt_board[8] and ttt_board[0]!= "-":
        winner = ttt_board[0]
        return True
    elif ttt_board[2] == ttt_board[4] == ttt_board[6] and ttt_board[2]!= "-":
        winner = ttt_board[2]
        return True

def tie(ttt_board):
    global running_game
    if "-" not in ttt_board:
        show_board(ttt_board)
        print("It's a tie. Try it again, maybe now you will be lucky!!!")
        running_game = False

def winning():
    if horizontal(ttt_board) or vertical(ttt_board) or diagonal(ttt_board):
        print(f"***********The winner is {winner}!!!!!!! Congratulations!!! You did it!!!!*********")

def change_player():
    global player
    if player == "X": 
        player = "O"
    else: 
        player = "X"


def computer(ttt_board):
    while player == "O":
        position = random.randint(0,8)
        if ttt_board[position] == "-":
            ttt_board[position] = "O"
            change_player()



if __name__ == "__main__":
    main()

# pytest -v ttt.py

