"""
CS2302
Lab6
Purpose: use a disjoint set forest to build a maze.
Created on Mon Apr 8, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

# Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate 


def DisjointSetForest(size):
    r = np.zeros(size,dtype=np.int) - 1
    #print(r)
    return r
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root
        
'''def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0: # i is a root
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1: #i and S[i] are neighbors; draw straight line
                y0 = [0,0,0,0,0]
            else:      #i and S[i] are not neighbors; draw arc
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interpolate.interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)
    
plt.close("all")      
S = DisjointSetForest(8)
print(S)
draw_dsf(S) 
union(S,7,6)
print(S) 
draw_dsf(S)
union(S,0,2)
print(S)
draw_dsf(S)
union(S,6,3)
print(S)
draw_dsf(S)
union(S,5,2)
print(S)
draw_dsf(S)
union(S,4,6)
print(S)
draw_dsf(S)'''