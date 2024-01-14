import random
from game import Game, Move, Player
import randomAgent
from copy import copy
from collections import namedtuple
import numpy as np
from random import choice, randint
from tqdm import tqdm
from scipy.special import softmax
import pickle
import matplotlib.pyplot as plt

class GameNode:
    def __init__(self, current_game, move, available_moves, ply_id,parent = None) -> None:
        super().__init__()
        self.game = current_game
        self.state = current_game.get_board()
        #add state value
        self.available_moves = available_moves
        self.children = []
        self.move = move
        self.parent = parent
        self.ply_id = ply_id

    def __add_children__(self, childNode):
        if childNode not in self.children:
            self.children.append(childNode)
    def __get_available_moves(self, current_board):
        return [((2,3,Move.TOP))]

    def __compute_tree__(self):
        for move in self.available_moves:
            self.game.__move((move.y, move.x), move.slide,self.ply_id)
            child = self.game.get_board()
            self.__add_children__(GameNode(self.game, move, self.__get_available_moves(child),self.ply_id, self ))

    def __evaluate__(self, matrix, sign):
        # Controlla le righe 
        max_row_count = max([row.count(sign) for row in matrix]) 
    
        # Controlla le colonne 
        max_column_count = max([column.count(sign) for column in zip(*matrix)]) 
    
        # Controlla la diagonale principale 
        main_diagonal_count = sum([matrix[i][i] == sign for i in range(5)]) 
    
        # Controlla la diagonale secondaria 
        secondary_diagonal_count = sum([matrix[i][4-i] == sign for i in range(5)]) 
    
    
        return max(max_row_count, max_column_count, main_diagonal_count, secondary_diagonal_count)

class minMaxPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.id = -1

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move

