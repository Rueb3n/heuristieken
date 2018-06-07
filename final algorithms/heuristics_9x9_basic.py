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

start_time = time.time()

# grid = [['.', '.', 'T', 'F', 'F', 'E'],
#         ['.', '.', 'T', '.', '.', 'E'],
#         ['.', '.', 'T', 'R', 'R', 'E'],
#         ['.', '.', '.', 'C', 'G', 'G'],
#         ['A', 'B', 'B', 'C', '.', '.'],
#         ['A', '.', '.', 'C', 'H', 'H']]


# new_grid = [['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.']]



# grid = [['.', '.', 'T', 'F', 'F', 'E'],
#         ['.', '.', 'T', '.', '.', 'E'],
#         ['.', '.', 'T', 'R', 'R', 'E'],
#         ['.', '.', '.', 'C', 'Z', 'Z'],
#         ['A', 'B', 'B', 'C', '.', '.'],
#         ['A', '.', '.', 'C', 'H', 'H']]


       # [['A', '.', '.', '.', 'F', 'F'], 
       #  ['A', '.', '.', '.', '.', '.'], 
       #  ['.', '.', '.', '.', 'R', 'R'], 
       #  ['Z', 'Z', 'T', 'C', '.', 'E'], 
       #  ['B', 'B', 'T', 'C', '.', 'E'], 
       #  ['H', 'H', 'T', 'C', '.', 'E']]


# grid = [['.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.'],
#     	['R', 'R', 'T', 'H', '.', '.'],
#     	['.', '.', 'T', 'H', '.', '.'],
#     	['.', '.', 'T', 'H', '.', '.'],
#     	['.', '.', 'C', 'C', '.', '.']]


# grid = [['.', '.', 'B', 'B', 'A', 'A'],
#     	['.', 'D', 'D', 'C', 'C', 'E'],
#     	['.', '.', 'R', 'R', 'Z', 'E'],
#     	['J', 'J', 'I', 'I', 'Z', 'E'],
#     	['K', '.', '.', 'H', 'F', 'F'],
#     	['K', '.', '.', 'H', 'G', 'G']]


# grid = [['.', 'Z', 'Z', 'Y', 'Y', 'Y'],
#     	['.', 'X', 'X', 'Q', 'P', 'P'],
#     	['R', 'R', 'O', 'Q', '.', 'S'],
#     	['J', 'J', 'O', 'M', 'M', 'S'],
#     	['I', '.', 'H', '.', 'N', 'N'],
#     	['I', '.', 'H', '.', '.', '.']]


# grid = [['.', 'Z', 'Z', 'Y', 'Y', 'Y'],
#     	['.', 'X', 'X', 'Q', 'P', 'P'],
#     	['.', 'R', 'R', 'Q', '.', 'S'],
#     	['J', 'J', '.', 'M', 'M', 'S'],
#     	['I', '.', 'H', '.', 'N', 'N'],
#     	['I', '.', 'H', '.', '.', '.']]

# grid = [['.', '.', 'T', 'F', 'F', '.'],
#         ['.', '.', 'T', '.', '.', 'B'],
#         ['R', 'R', '.', '.', '.', 'B'],
#         ['.', '.', '.', 'C', 'G', 'G'],
#         ['A', '.', '.', 'C', '.', '.'],
#         ['A', '.', '.', 'C', 'H', 'H']]





# grid = [['A', 'W', 'W', 'W', '.', 'S', '.', '.', '.'],
#     	  ['A', '.', '.', 'V', '.', 'S', 'Q', 'Q', 'Q'],
#     	  ['.', '.', '.', 'V', '.', 'S', '.', '.', 'P'],
#     	  ['B', 'B', '.', 'V', '.', 'T', 'T', 'T', 'P'],
#     	  ['C', 'R', 'R', 'I', '.', '.', '.', '.', 'P'],
#     	  ['C', '.', 'H', 'I', '.', 'U', 'U', 'U', 'O'],
#     	  ['E', 'E', 'H', 'J', 'L', 'L', '.', '.', 'O'],
#     	  ['F', '.', 'H', 'J', 'K', '.', '.', '.', 'O'],
#     	  ['F', 'G', 'G', 'G', 'K', 'M', 'M', 'N', 'N']]

grid = [['A', 'A', 'B', 'B', 'N', '.', '.', 'P', '.'],
        ['D', 'C', 'C', 'C', 'N', 'O', 'O', 'P', '.'],
        ['D', '.', 'E', 'E', 'L', 'M', '.', 'Q', 'Q'],
        ['.', '.', 'F', 'K', 'L', 'M', 'S', 'S', 'S'],
        ['R', 'R', 'F', 'K', '.', '.', '.', '.', '.'],
        ['.', 'G', '.', 'K', 'T', 'T', 'U', 'U', 'V'],
        ['H', 'G', 'J', 'J', 'Y', 'W', 'W', 'W', 'V'],
        ['H', '.', 'Z', 'Z', 'Y', 'X', 'X', '.', 'V'],
        ['H', 'I', 'I', 'I', 'Y', '.', '.', '.', '.']]


# grid =     [['A', 'A', 'A', 'B', '.', 'E', 'F', '.', '.'],
#         	['.', '.', '.', 'B', '.', 'E', 'F', 'H', 'H'],
#         	['.', '.', '.', 'B', 'C', 'C', 'G', '.', '.'],
#         	['.', '.', '.', '.', 'D', 'D', 'G', 'I', 'I'],
#         	['.', '.', 'Q', 'Q', 'Q', 'P', 'R', 'R', 'K'],
#         	['Z', '.', 'S', '.', '.', 'P', '.', '.', 'K'],
#         	['Z', '.', 'S', 'T', 'T', 'P', 'O', 'O', 'K'],
#         	['Y', 'X', 'W', 'W', 'U', 'M', 'M', 'M', 'L'],
#         	['Y', 'X', 'V', 'V', 'U', '.', '.', '.', 'L']]   

# grid = [['.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', 'H'],
#     	['R', 'R', 'T', '.', '.', 'H'],
#     	['.', '.', 'T', '.', '.', 'H'],
#     	['.', '.', 'T', '.', 'B', 'B'],
#     	['.', '.', '.', '.', '.', '.']]


new_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.', '.', '.', '.']]


# new_grid = [['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.']]



# print type(grid)

total_vehicles = []
mycar = 'R'
car = 'C'
truck = 'T'
# goal = [2,5]
goal = [4,8]
vehicles = {}


# class RushHour():

# for each letter, search for other letters in board, save letters in dictionary with coordinates

# adjecent grids for specific vehicle
def check_adjecent(vehicle, coordinates, vehicle_dict):
	# print 'vehicle: ',vehicle
	# print 'coordinates: ',coordinates
	# below = [x+1,y]
	# above = [x-1,y]
	# right = [x,y+1]
	# left = [x,y-1]
	# save adjecent vertical
	first_x = 0
	first_y = 0
	for coordinate in coordinates:
		first_x = coordinate[0]
		first_y = coordinate[1]
		break
	for coordinate in coordinates[1:2]:
		if first_x == coordinate[0]:
			vehicle_dict[vehicle].append('horizontal')
			# print 'horizontal'
			# print coordinate[0]
		if first_y == coordinate[1]:
			vehicle_dict[vehicle].append('vertical')
			# print 'vertical'
			# print coordinate[1]


def check_goal(vehicle, vehicle_dict, archive, df_grid, child_df_grid, find_path):
	# print '\n goal vehicle: ',vehicle, '\n',vehicle_dict
	if vehicle == mycar:
		# print 'My car: ',vehicle_dict[vehicle][1]
		if vehicle_dict[vehicle][1] == goal:
			print "\n Goal Reached. \n"
			archive.append(copy.deepcopy(df_grid))
			archive.append(copy.deepcopy(child_df_grid))
			# for board in archive:
			# 	for line in board:
			# 		print line
			end_time = time.time()
			# print 'length archive: ', len(archive)

		
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
			sys.exit()
	# else: print "Goal not reached."






def move(vehicle, vehicle_dict, df_grid):
	# print '\n NODE IN MOVE: \n ',vehicle
	# print 'move vehicle: \n'
	vehicle_loc = vehicle[-1]
	vehicle = vehicle[1]
	coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2 = is_blocked(vehicle_dict[vehicle], df_grid)
	# print '\n NODE IN MOVE 2: \n ',vehicle_dict[vehicle]
	# print '\n Vehicle location: \n ',vehicle_loc

	# print '\n\n\n\n', vehicle, '\n\n\n'
	# print '\n',coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2,'\n'
	# print coordinate_object2
	# if vehicle[-1] == object_location:
	# 	print "first"
	# if vehicle[-1] == object_location2:
	# 	print "last"
	# sys.exit()
	if vehicle_loc == object_location and coordinate_object == '.':
		if(len(vehicle_dict[vehicle])) == 3:
			vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
			vehicle_dict[vehicle][0] = object_location
			# print 'new coordinates: ', vehicle_dict[vehicle][:-1]
			# movelist.append()
		if(len(vehicle_dict[vehicle])) == 4:
			vehicle_dict[vehicle][2] = vehicle_dict[vehicle][1]
			vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
			vehicle_dict[vehicle][0] = object_location
			# print 'new coordinates: ', vehicle_dict[vehicle][:-1]
	if vehicle_loc == object_location2 and coordinate_object2 == '.':
		if(len(vehicle_dict[vehicle])) == 3:
			vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
			vehicle_dict[vehicle][1] = object_location2
			# print 'new coordinates: ', vehicle_dict[vehicle][:-1]
		if(len(vehicle_dict[vehicle])) == 4:
			vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
			vehicle_dict[vehicle][1] = vehicle_dict[vehicle][2]
			vehicle_dict[vehicle][2] = object_location2
			# print 'new coordinates: ', vehicle_dict[vehicle][:-1]
		# print '\n', vehicle_dict
	# print '\n NODE IN MOVE 3: \n ',vehicle_dict[vehicle]
	return vehicle_dict


#########################################################################################################
###					Create copies of children boards and put in queue, 
###      then save parent board in explored (archive), then check if children not in explored (archive),
###		if children board in explored > remove from queue, if not in explored (archive) then put  children in archive		
##########################################################################################################################

def copy_board(vehicle_dict):
	# print '\n\n NEW COPY \n\n'
	# create deepcopy to not overwrite 
	temp_vehicle_dict = copy.deepcopy(vehicle_dict)
	temp_grid = copy.deepcopy(new_grid)

	# remove last value to only obtain coordinates
	for k, v in temp_vehicle_dict.items():
		v.pop()	
	
	# print '\n', temp_vehicle_dict, '\n'

	# overwrite grid
	for x in range(0,6):
		for y in range(0,6):
			for k, v in temp_vehicle_dict.items():
				for coordinate in v:
					x, y = coordinate
					temp_grid[x][y] = k

	# for i in range(0, len(temp_grid)):
	# 	print temp_grid[i]
	# print grid
	df_grid = pd.DataFrame(temp_grid)
	return df_grid, archive


# checks for empty spaces (queue for movelist)
def get_movelist(vehicle, coordinates, vehicle_dict, df_grid):
	# print '\n\n in get_movelist movelist = ', movelist
	movelist = []
	# if vehicle == mycar:
	# 	print '\n my car: ', vehicle
	# 	print is_blocked(vehicle_dict[vehicle])
	# 	for coordinate in coordinates:
	# 		if isinstance(coordinate[0], int):
	# 			print 'yes'
	# 			print coordinate[1]
	# 			print coordinate[1] + 1
	# else:
	# print '\n vehicle: ',vehicle
	coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2 = is_blocked(vehicle_dict[vehicle], df_grid)
	# print 'coordinate objects: ',coordinate_object, coordinate_object2
	if coordinate_object == '.':
		# print '\n\n There is space object 1\n\n', coordinate_object
		# print '\n movelist object1 = ', movelist, '\n vehicle move: ',movelist, [vehicle_dict[vehicle],vehicle, object_location]
		# if [vehicle_dict[vehicle],vehicle, object_location] not in movelist:
		movelist.append([vehicle_dict[vehicle],vehicle, object_location])
	if coordinate_object2 == '.':
		# print '\n\n There is space object 2\n\n', coordinate_object2
		# print '\n movelist object2 = ', movelist, '\n vehicle move: ',[vehicle_dict[vehicle],vehicle, object_location2]
		# if [vehicle_dict[vehicle],vehicle, object_location2] not in movelist:
		movelist.append([vehicle_dict[vehicle],vehicle, object_location2])
	# print vehicle_dict[vehicle], object_location, object_location2
	# print vehicle[:-1], direction
	return movelist, object_location, direction


# update grid
def grid_update():
	df_grid
	df_grid.apply(lambda c: pd.Series(c.name, c.values)).fillna('-').T

# return specific object on coordinate
def grid_check(coordinate, df_grid):
	# print 'check coordinate: ', coordinate
	x,y = coordinate
	# print 'x , y = ',x,y
	# print 'on that coordinate is: ', df_grid[y][x]
	return df_grid[y][x]

# check adjecent coordinates and locate other vehicles or empty spots
def is_blocked(vehicle_dict, df_grid):
	if any("horizontal" in s for s in vehicle_dict):
		# print vehicle_dict
		# print 'horizontal yes'
		left_coordinate = vehicle_dict[0]
		right_coordinate = vehicle_dict[-2]
		left = [left_coordinate[0], left_coordinate[1] - 1]
		right = [right_coordinate[0], right_coordinate[1] + 1]
		# print 'left, right: \n', left, right
		left_grid = 0
		right_grid = 0
		if all(i in range (0,len(df_grid)) for i in left):
			try:
				left_grid = grid_check(left, df_grid)
				# print 'left: '
				# return left_grid, left, 'first'
			except:
				pass
		if all(i in range (0,len(df_grid)) for i in right):
			try:
				right_grid = grid_check(right, df_grid)
				# print 'right: '
				# return right_grid, right, 'last'
			except:
				pass
		return left_grid, left, 'first', right_grid, right, 'last'
	if any("vertical" in s for s in vehicle_dict):
		# print 'vertical yes'
		up_coordinate = vehicle_dict[0]
		down_coordinate = vehicle_dict[-2]
		# print down_coordinate
		up = [up_coordinate[0] - 1, up_coordinate[1]]
		down =  [down_coordinate[0] + 1, down_coordinate[1]]
		# print 'up, down: \n', up, down
		up_grid = 0
		down_grid = 0
		if all(i in range(0,len(df_grid)) for i in down):
			try:
				down_grid = grid_check(down, df_grid)
				# print 'down: ' 
				# return down_grid, down, 'last'
			except:
				pass
		if all(i in range(0,len(df_grid)) for i in up):
			try:
				up_grid = grid_check(up, df_grid)
				# print 'up: '
				# return up_grid, up, 'first'
			except:
				pass
		return up_grid, up, 'first', down_grid, down, 'last'


	
# read vehicles

print '\n\n\n\n START \n\n\n\n\n'

# get coordinates for vehicles
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
				# print vehicle_dict
	# 			total_vehicles.append(vehicle)
	# total_vehicles_dict = Counter(total_vehicles)
	return vehicle_dict



def create_board(vehicle_dict):
	# new_grid = []

	# new_grid = [['.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.']]



	new_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.', '.', '.', '.']]

	# print vehicle_dict,'\n', node
	# vehicle_dict_new = move(node, vehicle_dict, df_parent_grid)
	# print vehicle_dict_new
	# sys.exit()
	# print vehicle_dict
	for vehicle in vehicle_dict:
		# print '\n vehicle: ', vehicle, vehicle_dict[vehicle][0]
		for coordinate in enumerate(vehicle_dict[vehicle]):
			# print vehicle, coordinate[1][0]
			for coordinate_number in coordinate[1]:
				if coordinate_number in range(10):
				# try: 
					new_grid[coordinate[1][0]][coordinate[1][1]] = vehicle
	# 			except:
	# 				pass

	return new_grid





# results = breadth_first_search(rushhour, max_depth=25)
# queue paths
queue = []
# explored paths
explored = []
# movelist = []
grids = []
# archive =  []






######## heuristic formula #####
##      f(p)=cost(p)+h(p)    ###
################################
# where cost(p) is moves from space to goal and h(p) is vehicles blocking the way
# this is admissible heuristic, for it never overestimates





def calculate_costs(current_vehicle, vehicle_dict, child_df_grid):
	cost_p = 0
	h_p = 0
	cost_p = goal[1] - vehicle_dict['R'][1][1] 
	# cost_p = 1
	# print ' \n\n ---------------------------------- entered here ------------------------------------'
	# print 'current node: ', current_vehicle[-2:-1][0]


	# calculate h(p) by ranging over posision of r and checking grids right of r for any other cars
	for i in range(len(vehicle_dict['R'][:2])+vehicle_dict['R'][0][1],len(child_df_grid)):
		
		# print 'i: ', child_df_grid[i][vehicle_dict['R'][1][0]], i
		# print vehicle_dict['R'][1][1] 
		if child_df_grid[i][vehicle_dict['R'][1][0]] == '.' and (i == vehicle_dict['R'][1][1] +1):
			# print 'yes'
			h_p -= 3
		if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
			if child_df_grid[i][vehicle_dict['R'][1][0]] == current_vehicle[-2:-1][0]:
				h_p -= 2
			# 	print '-2 h_p'
			# print 'before if:',child_df_grid[i][vehicle_dict['R'][1][0]]
			# print 'before if:',child_df_grid[i][vehicle_dict['R'][0][0]]
			# print 'before if:',child_df_grid[i][vehicle_dict['R']]
			# print 'before 1:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
			if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) > 3 or (len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) == 3 and str(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]).isdigit()):
				# print i
				# print child_df_grid[i][vehicle_dict['R'][1][0]]
				# print '1a:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
				# print '1b:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]
				# print '1c:',vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]
				# print '\n car: ', child_df_grid[i][vehicle_dict['R'][1][0]]
				# print '\n SEARCHING: ',vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][1],vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]
				# print len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])-vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]
				# print 'wooh'
				for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
					# if child_df_grid[p][vehicle_dict['R'][1][0]].isalpha():
					# print 'x: ', x
					if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha(): #checks if car that blocks R is blocked by any horizontal vehicle
						# print child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x]
						# print '+1'
						h_p += 2
					else: h_p += 1
					# print 'score: ',h_p
				for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
					# if child_df_grid[p][vehicle_dict['R'][1][0]].isalpha():
					x = x-4
					# print 'y: ',x
					if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha(): #checks if car that blocks R is blocked by any horizontal vehicle
						# print child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x]
						# print '+1'
						# print 'score: ',h_p
						h_p += 2
					else: h_p += 1
					# print 'score: ',h_p

 	# print 'below truck: ', child_df_grid[p]
				# print 'before h_p: ',h_p
				# print vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]
				h_p += (1.2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1])
				# h_p += (2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1])-vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]
				# print 'after h_p: ',h_p
				# -vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]))-(cost_p)
				# print h_p



############ WRITE HEURISTIC THAT CHECK IF MIDDLE OF CAR IS BLOCK R, FRONT AND BACK OF CAR SHOULD BE LESS HIGH SCORE IN ORDER TO MOVE IT AWAY
############ IF CAR IS FREE TO MOVE BLOCKING RR IT SHOULD MOVE FIRST 

############ NEW HEURISTIC: TO THE LEFT IS LOWER SCORE!!!!
########### CARS AROUND RED CAR ALSO LOWER SCORE!!! 
				
			if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) < 3:
				# print child_df_grid[i][vehicle_dict['R'][1][0]]
				# print '2a:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
				# print '2b:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][0]
				# print '2c:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
				h_p += 1.3**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
				# -vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][0]))-(cost_p)
				# h_p += 2**cost_p-
				# if child_df_grid[i][vehicle_dict['R'][1][0]] == 'E':
				# print 'h_p cars: ', h_p
			# 	h_p += 2*h_p

	# for i in range(len(vehicle_dict['R'])+vehicle_dict['R'][0][1],len(child_df_grid)):
	# 	if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
	# 		h_p += 1
	# print '\n', child_df_grid
	print '\n cost(p):',cost_p, ' h(p):', h_p,
	f_p = cost_p + h_p
	# print '\n total: ', (cost_p + h_p)
	# print '\n total: ', (cost_p + h_p)*cost_p
	# sys.exit()
	return (cost_p + h_p)*cost_p


# grid =[['A', 'W', 'W', 'W', '.', '.', '.', '.', '.'],
# 	   ['A', '.', '.', 'V', '.', '.', 'Q', 'Q', 'Q'],
# 	   ['.', '.', '.', 'V', '.', '.', '.', '.', 'P'],
# 	   ['B', 'B', '.', 'V', '.', 'T', 'T', 'T', 'P'],
# 	   ['C', 'R', 'R', '.', '.', '.', '.', '.', 'P'],
# 	   ['C', '.', 'H', '.', '.', 'U', 'U', 'U', 'O'],
# 	   ['E', 'E', 'H', 'J', 'L', 'L', '.', '.', 'O'],
# 	   ['F', '.', 'H', 'J', 'K', '.', '.', '.', 'O'],
# 	   ['F', 'G', 'G', 'G', 'K', 'M', 'M', 'N', 'N']]


# grid =[['A', 'W', 'W', 'W', '.', '.', '.', '.', '.'],
# 	   ['A', '.', '.', 'V', '.', '.', 'Q', 'Q', 'Q'],
# 	   ['.', '.', '.', 'V', '.', '.', '.', '.', 'P'],
# 	   ['B', 'B', '.', 'V', '.', 'T', 'T', 'T', 'P'],
# 	   ['C', 'R', 'R', '.', '.', '.', '.', '.', 'P'],
# 	   ['C', '.', 'H', '.', '.', 'U', 'U', 'U', 'O'],
# 	   ['E', 'E', 'H', 'J', 'L', 'L', '.', '.', 'O'],
# 	   ['F', '.', 'H', 'J', 'K', '.', '.', '.', 'O'],
# 	   ['F', 'G', 'G', 'G', 'K', 'M', 'M', 'N', 'N']]


# grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     	['.', '.', 'G', 'G', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     	['R', 'R', '.', '.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     	['.', '.', 'P', 'P', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.', '.', '.', '.']]

grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    	['.', '.', 'G', 'G', '.', '.', '.', '.', '.'],
    	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    	['.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    	['R', 'R', '.', '.', '.', '.', '.', '.', 'B'],
    	['.', '.', '.', '.', '.', '.', '.', 'C', 'C'],
    	['.', '.', 'P', 'P', '.', '.', '.', '.', '.'],
    	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    	['.', '.', '.', '.', '.', '.', '.', '.', '.']]

# order queue by value of f(p) - low value is best
def start_bfs(start_grid):
	z = 0
	find_path = dict()
	vehicle_dict = dict()
	archive = deque()
	queue = PriorityQueue()
	temp_vehicle_dict = set_up(vehicle_dict,pd.DataFrame(start_grid))
	# temp_cost_child = calculate_costs(temp_vehicle_dict, pd.DataFrame(start_grid))
	# print temp_cost_child
	# sys.exit()
	queue.put((goal[1] - temp_vehicle_dict['R'][1][1],start_grid))
	find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
	while queue:
		vehicle_dict.clear()
		# print 'queue: ',queue.queue
		df_grid = queue.get()
		# print '\n\n\n value: '
		# print df_grid[0]
		# df_grid = df_grid[1]
		# print '\n\n\n value: '
		# print df_grid[0]
		df_grid = df_grid[1]
		# print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
		archive.append(df_grid)
		vehicle_dict = set_up(vehicle_dict,pd.DataFrame(df_grid))
		# z += 1
		# if z == 10:
		# 	sys.exit()

		for key, value in vehicle_dict.iteritems():
			# print key, value
			check_adjecent(key, value, vehicle_dict)
			movelist, object_location, direction = get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
			if not movelist:
				continue
			while movelist:
					node = movelist.pop(0)
					new_vehicle_dict = move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
					child_df_grid = create_board(new_vehicle_dict)
					# print "\n",pd.DataFrame(child_df_grid),"\n"
					# sys.exit()
					# print child_df_grid
					if not child_df_grid in archive:
						# print ' --------------------\n child grid: \n', pd.DataFrame(child_df_grid),'\n ------------------- \n \n '

						# cost for first heuristic function commented
						# cost_child = calculate_costs(new_vehicle_dict, pd.DataFrame(child_df_grid))
						# cost for second heuristic function
						cost_child = calculate_costs(node, new_vehicle_dict, pd.DataFrame(child_df_grid))

						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						check_goal(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path) #key error: 'r'
						queue.put((cost_child, child_df_grid))
						archive.append(child_df_grid)

	



def start_dfs(start_grid):
	# for key, value in vehicle_dict.iteritems():
	movelist = []
	vehicle_dict = dict()
	stack = deque()
	stack.append(pd.DataFrame(start_grid))
	while stack:
		vehicle_dict.clear()
		df_grid = stack.popleft()
		vehicle_dict = set_up(vehicle_dict,df_grid)
		if not True in [df_grid.equals(x) for x in archive]:
	
			movelist = []

			for key, value in vehicle_dict.iteritems():
				check_adjecent(key, value, vehicle_dict)
				movelist, object_location, direction = get_movelist(key, value, vehicle_dict, df_grid)
			new_movelist = movelist

			while new_movelist:	
	
				node = new_movelist.pop(0)

				# print 'parent grid: \n', df_grid
				new_vehicle_dict = move(node, copy.deepcopy(vehicle_dict), df_grid)
				child_df_grid = create_board(new_vehicle_dict)
				check_goal(node[1], new_vehicle_dict, archive, df_grid, child_df_grid) #key error: 'r'
				stack.append(child_df_grid)


			# if df_grid not in archive:
			archive.append(copy.deepcopy(df_grid))
			movelist, object_location, direction = get_movelist(key, value, vehicle_dict, df_grid)
	

		# print '\n queue: \n'
		# for board in queue: 
		# 	print board
		# 	dict_child = set_up(dict(),board)
		# 	print 'dict child: ',dict_child
		# 	for key, value in dict_child.iteritems():
		# 		check_adjecent(key, value, dict_child)
		# 		movelist, object_location, direction = get_movelist(key, value, dict_child, movelist, pd.DataFrame(board))
		# 		print '\n temp movelist:', movelist
		# 	new_movelist = movelist
		# print '\n new movelist:', new_movelist
		# 	# break

			###############
			#### MOVELIST IS MANIUPLATED DURING MOVE (REWRITE MOVE?)
			#############

			# print '\n last movelist 2: \n', movelist
			# print 'vehicle dict: ', vehicle_dict
			# sys.exit()



	# sys.exit()


		# print '\n *********************** \n *********************** \n archive: \n *********************** \n ********************** \n', archive,'\n'

	# if vehicle_dict not in archive:
	# 		archive.append(vehicle_dict) #copy deepcopy?





start_bfs(grid)
# start_dfs(grid)


