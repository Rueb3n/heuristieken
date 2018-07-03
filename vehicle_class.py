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
import board_class

board = board_class.board
mycar = 'R'


class vehicle:

	# checks if vehicle is horizontal or vertical
	@staticmethod
	def check_adjecent(vehicle, coordinates, vehicle_dict):
		first_x = 0
		first_y = 0
		for coordinate in coordinates:
			first_x = coordinate[0]
			first_y = coordinate[1]
			break
		for coordinate in coordinates[1:2]:
			if first_x == coordinate[0]:
				vehicle_dict[vehicle].append('horizontal')
			if first_y == coordinate[1]:
				vehicle_dict[vehicle].append('vertical')
		return vehicle_dict

	@staticmethod			
	def check_goal_9x9(vehicle, vehicle_dict, archive, df_grid, child_df_grid, find_path, grid, start_time):
		goal = [4,8]
		if vehicle == mycar:
			if vehicle_dict[vehicle][1] == goal:
				print "\n Goal Reached. \n"
				archive.append(copy.deepcopy(df_grid))
				archive.append(copy.deepcopy(child_df_grid))
				end_time = time.time()

				parent = (('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'),
		        	('.', '.', '.', '.', '.', '.', '.', '.', '.'))

				total_moves = 0
				while [list(x) for x in parent] != grid:
					parent = find_path[tuple(tuple(x) for x in child_df_grid)]
					print pd.DataFrame([list(x) for x in parent])
					child_df_grid = parent
					total_moves += 1
				print "\n Goal Reached. \n"
				print '\n time: ', end_time- start_time
				print 'total moves: ', total_moves
				return True

	@staticmethod
	def check_goal_6x6(vehicle, vehicle_dict, archive, df_grid, child_df_grid, find_path, grid, start_time):
			goal = [2,5]
			if vehicle == mycar:
				if vehicle_dict[vehicle][1] == goal:
					print "\n Goal Reached. \n"
					archive.append(copy.deepcopy(df_grid))
					archive.append(copy.deepcopy(child_df_grid))
					end_time = time.time()			

					parent = [['.', '.', '.', '.', '.', '.'],
					        	['.', '.', '.', '.', '.', '.'],
					        	['.', '.', '.', '.', '.', '.'],
					        	['.', '.', '.', '.', '.', '.'],
					        	['.', '.', '.', '.', '.', '.'],
					        	['.', '.', '.', '.', '.', '.']]

					total_moves = 0
					while [list(x) for x in parent] != grid:
						parent = find_path[tuple(tuple(x) for x in child_df_grid)]
						print pd.DataFrame([list(x) for x in parent])
						child_df_grid = parent
						total_moves += 1
					print "\n Goal Reached. \n"
					print '\n time: ', end_time- start_time
					print 'total moves: ', total_moves
					return True

	@staticmethod
	def move(vehicle, vehicle_dict, df_grid):
		vehicle_loc = vehicle[-1]
		vehicle = vehicle[1]
		coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2 = board.is_blocked(vehicle_dict[vehicle], df_grid)
		if vehicle_loc == object_location and coordinate_object == '.':
			if(len(vehicle_dict[vehicle])) == 3:
				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
				vehicle_dict[vehicle][0] = object_location
			if(len(vehicle_dict[vehicle])) == 4:
				vehicle_dict[vehicle][2] = vehicle_dict[vehicle][1]
				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
				vehicle_dict[vehicle][0] = object_location
		if vehicle_loc == object_location2 and coordinate_object2 == '.':
			if(len(vehicle_dict[vehicle])) == 3:
				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
				vehicle_dict[vehicle][1] = object_location2
			if(len(vehicle_dict[vehicle])) == 4:
				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][2]
				vehicle_dict[vehicle][2] = object_location2
		return vehicle_dict

