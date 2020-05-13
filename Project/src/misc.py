#!/usr/local/bin/python3.7

class Symbol:
    def __init__(self):
        self.pacman = "p"
        self.monster = "m"
        self.food = "."
        self.wall = "%"
        self.empty = " "

def manhattandistance(current, destination):
    return abs( current[0] - destination[0] ) + abs( current[1] - destination[1] )

