# MountainCar
An implementation of a standard reinforcement learning problem where an under-powered car is trying to summit a mountain.  This implementation uses semi-gradient double-q learning to learn the optimal actions (accelerate, brake or do nothing) to take at every position.
Details on both tile coding, semi-gradient reinforcement learning methods and double-q learning can be found in the Sutton and Barto textbook, Reinforcement Learning: An Introduction

TileCoder.py - This is where the input space is divided into tiles.  Each tile is offset (in this case, diagonally) so that each point in input space is only in a single tile for each tiling.  This function returns the indices corresponding to the tile that the given input is mapped to in each tile.  By returning the tile indicies we are simulating the inner product of the weight vector theta and the feature vector q-hat. 

learning.py - Utilizes Tilecoder to get the tile indices used for each stage of learning. The learning is actually conducted in the learn() method. WriteF() writes the learned values of each state, to be plotted using plot.py
