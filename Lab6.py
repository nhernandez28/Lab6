"""
CS2302
Lab6
Purpose: use a disjoint set forest to build a maze.
Created on Thu Apr 4, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import disjointSetForest
import time

#Draws graph, provided by professor
def draw_maze(walls, maze_rows, maze_cols, cell_nums = False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1] - w[0] == 1: #vertical wall
            x0 = (w[1] % maze_cols)
            x1 = x0
            y0 = (w[1] // maze_cols)
            y1 = y0 + 1
        else:#horizontal wall
            x0 = (w[0] % maze_cols)
            x1 = x0 + 1
            y0 = (w[1] // maze_cols)
            y1 = y0  
        ax.plot([x0, x1], [y0, y1], linewidth = 1, color = 'k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0, 0, sx, sx, 0], [0, sy, sy, 0, 0], linewidth = 2, color = 'k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r * maze_cols   
                ax.text((c + .5), (r + .5), str(cell), size = 10,
                        ha = "center", va = "center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w = []
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r * maze_cols
            #itterates until theres no more
            if c != maze_cols - 1:
                w.append([cell, cell + 1])
            #itterates until theres no more 
            if r != maze_rows - 1:
                w.append([cell, cell + maze_cols])
    return w
    
#Find for compression
def find_c(S, i):
    if S[i] < 0:
        return i
    r = find_c(S, S[i])
    S[i] = r
    return r

#union for compression
def union_by_size(S, i, j):
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        if S[ri] > S[rj]:
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

#checks if in same set
def inSameSet(S, a, b):
    return disjointSetForest.find(S, a) == disjointSetForest.find (S, b)

#counts number of sets
def numSets(S):
    sets = 0 
    count = np.zeros(len(S), dtype = int) 
    for i in range(len(S)): 
        if S[i] < 0: 
            sets += 1 
        count[disjointSetForest.find(S, i)] += 1
    return sets

#Without Compression
def main(S, walls):
    timeStart = time.time()
    
    while numSets(S) > 1:
        #selects random wall
        rand = random.randint(0, len(walls)- 1)
        
        if inSameSet(S, walls[rand][0], walls[rand][1]) == False:
            #this next line puts cell1 and cell2 together
            disjointSetForest.union(S, walls[rand][0], walls[rand][1])
            #removes random selected wall
            walls.pop(rand)
            
    draw_maze(walls, maze_rows, maze_cols)
    timeEnd = time.time() - timeStart
    print('Time it took for standard union: ', timeEnd)
    
#with compression
def main2(S, walls):
    timeS = time.time()
    
    while numSets(S) > 1:
        #selects random wall
        rand = random.randint(0, len(walls)- 1)
        
        if inSameSet(S, walls[rand][0], walls[rand][1]) == False:
            #this next line unites cell1 and cell2 using compression
            union_by_size(S, walls[rand][0], walls[rand][1])
            #removes random selected wall
            walls.pop(rand)
            
    draw_maze(walls, maze_rows, maze_cols)
    timeE = time.time() - timeS
    print('Time it took for union by size: ', timeE)

plt.close("all")

#maze demensions 
maze_rows = 20
maze_cols = 25

walls = wall_list(maze_rows, maze_cols)

draw_maze(walls, maze_rows, maze_cols, cell_nums = True) 
    
S = disjointSetForest.DisjointSetForest(maze_rows * maze_cols)

print()
#without compression
main(S, walls)
print()
#with compression
main2(S, walls)
