#!/usr/local/bin/python3 
from misc import *
from game_map import *
class Pacman:
    def __init__ (self, location, view, map_dimension, food):
        self.location = location # a list [x,y], pacman current location
        self.food = food # an int, the total number of food
        self.view = view # an interger 5
        #Pac man has it's own map to calculate and stores the manhattan distance
        self.map = Map(map_dimension[0], map_dimension[1])
        self.legal_actions = ["up","down","left","right","still"]        

  

    def generate_successor():
        #calculate the manhattan distance of all the tiles in i's view

        pass

    def move(self):
        print("Randomly moving!")

    # with the current view, calculate the manhattan distance of tiles that packman can currently see
    def calculate_manhattan_distance(self):
        radius = int (view/2)
        total = view * view  # the maximum number of tiles that pacman can see
        
        for y in range(self.location[1] - radius, self.location[1] + radius +1 ,1):
            if (y<0 or y >= self.map.height):
                continue
            
            for x in range(self.location[0]-radius, self.location[0] +radius + 1, 1):
                if (x<0 or x >= self.map.width) :
                    continue
                self.map.data[y][x] = manhattandistance(self.location, [x,y])

        

    # Pacman will try to scan the whole map to know where all the food is
    def map_scanning():
        pass



    # the search function to find all the best move from the given successor
    def search_for_best_move():
        pass

    # the current location has food
    def eat_food():
        self.food -= 1                  
        pass

    # when pacman has gather all the foods
    def win_game():
        dub = "win"
        return dub

    # when the current location has a monster
    def lose_game():
        l = "lose"
        return l



