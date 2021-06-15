from copy import deepcopy
from tictactoe.move import Move

class Node:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.children = []
        self.value = 0

    def addChild(self, node):
        self.children.append(node)

class Tree:
    def __init__(self, root):
        self.root = root
    
    def buildTree(self, curr):
        if curr.board.isTerminalState():
            return

        player = 'x' if curr.turn == 'o' else 'o'
        for i in range(3):
            for j in range(3):
                if curr.board.isPosEmpty(i, j):
                    newboard = deepcopy(curr.board)
                    newboard.update(Move(curr.turn, i, j))
                    curr.addChild(Node(newboard, player))

        for child in curr.children:
            self.buildTree(child)


