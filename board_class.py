# -*- coding: utf-8 -*-
import sys
import numpy as np
import random
import numbers
import pandas as pd
import time
import copy
from collections import Counter
import collections
from collections import deque
from random import shuffle
from multiprocessing import Queue
from Queue import PriorityQueue
import heapq

import algorithm_class 
import grid_class
import vehicle_class

class board:

	# checks for empty spaces (queue for movelist)
	@staticmethod 
	def get_movelist(vehicle, coordinates, vehicle_dict, df_grid):
		movelist = []
		coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2 = board.is_blocked(vehicle_dict[vehicle], df_grid)
		if coordinate_object == '.':
			movelist.append([vehicle_dict[vehicle],vehicle, object_location])
		if coordinate_object2 == '.':
			movelist.append([vehicle_dict[vehicle],vehicle, object_location2])
		return movelist, object_location, direction

	# update grid
	@staticmethod 
	def grid_update():
		df_grid
		df_grid.apply(lambda c: pd.Series(c.name, c.values)).fillna('-').T

	# return specific object on coordinate
	@staticmethod 
	def grid_check(coordinate, df_grid):
		x,y = coordinate
		return df_grid[y][x]

	# check adjecent coordinates and locate other vehicles or empty spots
	@staticmethod
	def is_blocked(vehicle_dict, df_grid):
		if any("horizontal" in s for s in vehicle_dict):
			left_coordinate = vehicle_dict[0]
			right_coordinate = vehicle_dict[-2]
			left = [left_coordinate[0], left_coordinate[1] - 1]
			right = [right_coordinate[0], right_coordinate[1] + 1]
			left_grid = 0
			right_grid = 0
			if all(i in range (0,len(df_grid)) for i in left):
				try:
					left_grid = board.grid_check(left, df_grid)
				except:
					pass
			if all(i in range (0,len(df_grid)) for i in right):
				try:
					right_grid = board.grid_check(right, df_grid)
				except:
					pass
			return left_grid, left, 'first', right_grid, right, 'last'
		if any("vertical" in s for s in vehicle_dict):
			up_coordinate = vehicle_dict[0]
			down_coordinate = vehicle_dict[-2]
			up = [up_coordinate[0] - 1, up_coordinate[1]]
			down =  [down_coordinate[0] + 1, down_coordinate[1]]
			up_grid = 0
			down_grid = 0
			if all(i in range(0,len(df_grid)) for i in down):
				try:
					down_grid = board.grid_check(down, df_grid)
				except:
					pass
			if all(i in range(0,len(df_grid)) for i in up):
				try:
					up_grid = board.grid_check(up, df_grid)
				except:
					pass
			return up_grid, up, 'first', down_grid, down, 'last'



	# get coordinates for vehicles
	@staticmethod
	def set_up(vehicle_dict, current_grid):
		for x in range(len(current_grid[0])):
			for y in range(len(current_grid[0])):
				if current_grid[x][y].isalpha():
					vehicle = current_grid[x][y]
					# add coordinates to vehicle
					if vehicle in vehicle_dict:
						vehicle_dict[vehicle].append([y,x])
					else:
						vehicle_dict[vehicle] = [[y,x]]
		return vehicle_dict

	# creates 9x9 board
	@staticmethod
	def create_board_9x9(vehicle_dict):

		new_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
		        	['.', '.', '.', '.', '.', '.', '.', '.', '.']]

		for vehicle in vehicle_dict:
			for coordinate in enumerate(vehicle_dict[vehicle]):
				for coordinate_number in coordinate[1]:
					if coordinate_number in range(10):
						new_grid[coordinate[1][0]][coordinate[1][1]] = vehicle
		return new_grid

	# creates 6x6 board
	@staticmethod	
	def create_board_6x6(vehicle_dict):

			new_grid = [['.', '.', '.', '.', '.', '.'],
			        	['.', '.', '.', '.', '.', '.'],
			        	['.', '.', '.', '.', '.', '.'],
			        	['.', '.', '.', '.', '.', '.'],
			        	['.', '.', '.', '.', '.', '.'],
			        	['.', '.', '.', '.', '.', '.']]


			for vehicle in vehicle_dict:
				for coordinate in enumerate(vehicle_dict[vehicle]):
					for coordinate_number in coordinate[1]:
						if coordinate_number in range(10):
							new_grid[coordinate[1][0]][coordinate[1][1]] = vehicle
			return new_grid
