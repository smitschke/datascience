# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:33:48 2020

Entwicklungsumgebung: Sypder 4.1.2
ESA3

@author: Susanne Mitschke
"""

from tkinter import *
import random

class TicTacToe(object):
    
    """Spielelogik"""
    def __init__(self):
        #define player sets 0 = user, 1 = computer
        self.player_dict = {0: {0}, 1: {0}}

        self.game_board = [1,2,3,4,5,6,7,8,9]

        #define winning condition sets
        row1 = {1,2,3}
        row2 = {4,5,6}
        row3 = {7,8,9}
        
        col1 = {1,4,7}
        col2 = {2,5,8}
        col3 = {3,6,9}
        
        dia1 = {1,5,9}
        dia2 = {3,5,7}

        self.winning_conditions = (row1, row2, row3, col1, col2, col3, dia1, dia2)

    def check_winning_conditions(self, player):
        """Prüft ob das Spiel gewonnen werden kann und gibt ggf. den Wert des Feldes zurück mit dem gewonnen werden kann"""
        winning_possibility = 0
        
        for winning_condition in self.winning_conditions:
            
            if len(winning_condition-self.player_dict[player]) == 1 and winning_possibility != -1:
                
                wp = list(winning_condition-self.player_dict[player])
                if wp[0] in self.game_board:
                    winning_possibility = wp[0]
            elif len(winning_condition-self.player_dict[player]) == 0:
                winning_possibility = -1
            
        return winning_possibility        

    def make_a_move(self, player, user_input = 0):
        """Ergänzt einen Wert zum Spielerset bzw. entfernt ihn vom Spielbrett"""
        if  player == 0:
            self.player_dict[0].add(int(user_input))
            self.game_board.remove(int(user_input))
            if self.check_winning_conditions(player) == -1:
                return "Gewonnen! Hurray! :)"
            else:
                return 0
        else:
            winning_possibility = self.check_winning_conditions(player)
            
            if winning_possibility == 0:
                if len(self.game_board) > 0:
                    chance_of_winning_player = self.check_winning_conditions(0)
                    
                    if chance_of_winning_player > 0: 
                        comp_value = chance_of_winning_player
                    else:
                        comp_value = random.choice(self.game_board)
       
                    self.player_dict[player].add(comp_value)
                    self.game_board.remove(comp_value)

                    return [comp_value]
                else:
                    return [0, "Unentschieden"]
            else:                
                self.player_dict[player] = self.player_dict[player].add(winning_possibility)
                return [winning_possibility, "Leider verloren :("]


class Application(Frame):
    """GUI"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.main_frame = Frame(master).pack(fill=BOTH)
        self.master.title("Tic - tac - toe")
        
    def game_finished(self, proceed):
        """Ergebnishandling der Checkbox nach Spielende"""
        if proceed == True:
            self.content_frame.destroy()
            self.load_mainframe()                   
        else:
            self.master.destroy()
        
    def make_a_move(self, btn, value, game): 
        """"Setzt X oder O-Wert und ruft TicTacToe Methode make_a_move auf"""
        btn.config(text="X", state="disabled")
        user_val = game.make_a_move(0, value)
         
        if type(user_val) == str:
            self.game_finished(messagebox.askyesnocancel(title="Spielende", message=user_val))
        else:
            comp_val = game.make_a_move(1)
            
            if comp_val[0] > 0 or len(comp_val) == 2:
                self.button_list[comp_val[0]-1].config(text="O", state="disabled")
            if len(comp_val) == 2:
                self.game_finished(messagebox.askyesno(title="Spielende", message=comp_val[1]+"\nNochmal?"))
                
    def load_mainframe(self):
        """Erzeugt Anwendung"""
        self.game = TicTacToe()
        self.content_frame = Frame(self.main_frame)
        self.button_list = []
        
        counter = 0
        
        for i in range(1, 4):
            for j in range(1, 4):
                
                counter += 1
                 
                button = Button(self.content_frame, font=("Arial",35), width=3, height=1, bg="#dadada", relief=GROOVE, command=lambda index=counter: self.make_a_move(self.button_list[index-1], index, self.game))
                button.grid(row=i-1, column=j-1, sticky=W+E+N+S)
                self.button_list.append(button)
        
        self.content_frame.pack(fill=BOTH)

if __name__ == '__main__':
    root = Tk()
    root.lift()
    app = Application(master=root)
    app.load_mainframe()
    app.mainloop()
