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


grid = [['.', 'Z', 'Z', 'Y', 'Y', 'Y'],
    	['.', 'X', 'X', 'Q', 'P', 'P'],
    	['R', 'R', 'O', 'Q', '.', 'S'],
    	['J', 'J', 'O', 'M', 'M', 'S'],
    	['I', '.', 'H', '.', 'N', 'N'],
    	['I', '.', 'H', '.', '.', '.']]


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


# grid = [['.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', 'H'],
#     	['R', 'R', 'T', '.', '.', 'H'],
#     	['.', '.', 'T', '.', '.', 'H'],
#     	['.', '.', 'T', '.', 'B', 'B'],
#     	['.', '.', '.', '.', '.', '.']]


# new_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         	['.', '.', '.', '.', '.', '.', '.', '.', '.']]


new_grid = [['.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.'],
        	['.', '.', '.', '.', '.', '.']]



# print type(grid)

total_vehicles = []
mycar = 'R'
car = 'C'
truck = 'T'
goal = [2,5]
# goal = [4,8]
vehicles = {}

# print grid
# for i in range(0, len(df_grid)):
# 		print df_grid[i]
# for i in range(0, len(new_grid)):
# 		print new_grid[i]



# class Queue:
#     def __init__(self):
#         self.elements = collections.deque()
    
#     def empty(self):
#         return len(self.elements) == 0
    
#     def put(self, x):
#         self.elements.append(x)
    
#     def get(self):
#         return self.elements.popleft()


# def breadth_first_search_3(graph, start, goal):
#     frontier = Queue()
#     frontier.put(start)
#     came_from = {}
#     came_from[start] = None
    
#     while not frontier.empty():
#         current = frontier.get()
        
#         if current == goal:
#             break
        
#         for next in graph.neighbors(current):
#             if next not in came_from:
#                 frontier.put(next)
#                 came_from[next] = current


# # visits all the nodes of a graph (connected component) using BFS
# def bfs_connected_component(graph, start):
# 	print graph	
# 	# queue paths
# 	queue = []
# 	# explored paths
# 	explored = []
# 	for i in range(len(start)):
# 		queue.append(start[i][1:][1:][0])
# 	print queue

# 	while queue:
# 		node = queue.pop(0)
# 		# print node
# 		if node not in explored:
# 			print node
# 			explored.append(node)
# 			check_adjecent(node)
# 			neighbours = graph[node]
# 			print neighbours


# 	sys.exit()
#     # keep track of all visited nodes
# 	explored = []
# 	# keep track of nodes to be checked
# 	queue = [start[1]]

# 	# keep looping until there are nodes still to be checked
# 	while queue:
# 	# pop shallowest node (first node) from queue
# 		node = queue.pop(0)
# 		if node not in explored:
# 	# add node to list of checked nodes
# 			explored.append(node)
# 			neighbours = graph[node]

# 	# add neighbours of node to queue
# 	for neighbour in neighbours:
# 		queue.append(neighbour)
# 	return explored
 



# def breadth_first_search(r, max_depth=25):
#     """
#     Find solutions to given RushHour board using breadth first search.
#     Returns a dictionary with named fields:
#         visited: the number of configurations visited in the search
#         solutions: paths to the goal state
#         depth_states: the number of states visited at each depth
#     Arguments:
#         r: A RushHour board.
#     Keyword Arguments:
#         max_depth: Maximum depth to traverse in search (default=25)
#     """
#     visited = set()
#     solutions = list()
#     depth_states = dict()

#     queue = deque()
#     queue.appendleft((r, tuple()))
#     while len(queue) != 0:
#         board, path = queue.pop()
#         new_path = path + tuple([board])

#         depth_states[len(new_path)] = depth_states.get(len(new_path), 0) + 1

#         if len(new_path) >= max_depth:
#             break

#         if board in visited:
#             continue
#         else:
#             visited.add(board)

#         if board.solved():
#             solutions.append(new_path)
#         else:
#             queue.extendleft((move, new_path) for move in board.moves())

#     return {'visited': visited,
#             'solutions': solutions,
#             'depth_states': depth_states}





# grid = ['..TCCT','..T..T','..TRRT','...TCC']


# read grid from text


# TO DO!!!! UPDATE GRID @ GRID_CHECK() AFTER FIRST ITERATION CHANGE TO TEMP GRID < already works with different def? might change in the future

# goal = (5,3)
# read location RR, define if horizontal or vertical to choose mobility option
# read locations oof CC and TTT to see if vertical or if horizontal to define their moving options
# check if RR can reach goal
# check amount of coordinates needed RR to move to reach goal
# if not 
	# check if CC or TTT can be moved near goal in order to clear 
	# 	else check if CC or TTT further from goal can move in order to clear path
	# 		if not check if RR can be moved to create opportunity to move any RR or TTT

# f = open('game1.txt','r')
# for line in f:
#     l = unicode(line, encoding='utf-8')# decode the input                                                                                  
#     print l.encode('utf-8') # encode the output                                                                                            
# f.close()

# with open('game1.txt') as f:
#     grid = [i.split() for i in f.readlines()]



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


def check_goal(vehicle, vehicle_dict, archive, df_grid, child_df_grid):
	# print '\n goal vehicle: ',vehicle, '\n',vehicle_dict
	if vehicle == mycar:
		# print 'My car: ',vehicle_dict[vehicle][1]
		if vehicle_dict[vehicle][1] == goal:
			print "\n Goal Reached. \n"
			archive.append(copy.deepcopy(df_grid))
			archive.append(copy.deepcopy(child_df_grid))
			for board in archive:
				for line in board:
					print line
			print "\n Goal Reached. \n"
			end_time = time.time()
			print '\n time: ', end_time- start_time
			sys.exit()
	# else: print "Goal not reached."


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
			print "\n Goal Reached. \n"
			end_time = time.time()
			print '\n time: ', end_time- start_time
			print 'length archive: ', len(archive)

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

			print 'total moves: ', total_moves + 1
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


# def move(vehicle, vehicle_dict):
# 	coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2 = is_blocked(vehicle_dict[vehicle])
# 	print '\n',coordinate_object, object_location, direction, coordinate_object2, object_location2, direction2,'\n'
# 	if coordinate_object == '.':
# 		# print '\n\n There is space \n\n'
# 		# print vehicle_dict[vehicle], object_location
# 		# movelist.append([vehicle_dict[vehicle],vehicle, object_location])
# 		# print vehicle[:-1], direction
# 		if direction == 'first':
# 			if(len(vehicle_dict[vehicle])) == 3:
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
# 				vehicle_dict[vehicle][0] = object_location
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 				# movelist.append()
# 			if(len(vehicle_dict[vehicle])) == 4:
# 				vehicle_dict[vehicle][2] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
# 				vehicle_dict[vehicle][0] = object_location
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 		if direction == 'last':
# 			if(len(vehicle_dict[vehicle])) == 3:
# 				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = object_location
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 			if(len(vehicle_dict[vehicle])) == 4:
# 				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][2]
# 				vehicle_dict[vehicle][2] = object_location
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 	if coordinate_object2 == '.':
# 		if direction2 == 'first':
# 			if(len(vehicle_dict[vehicle])) == 3:
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
# 				vehicle_dict[vehicle][0] = object_location2
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 				# movelist.append()
# 			if(len(vehicle_dict[vehicle])) == 4:
# 				vehicle_dict[vehicle][2] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][0]
# 				vehicle_dict[vehicle][0] = object_location2
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 		if direction2 == 'last':
# 			if(len(vehicle_dict[vehicle])) == 3:
# 				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = object_location2
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]
# 			if(len(vehicle_dict[vehicle])) == 4:
# 				vehicle_dict[vehicle][0] = vehicle_dict[vehicle][1]
# 				vehicle_dict[vehicle][1] = vehicle_dict[vehicle][2]
# 				vehicle_dict[vehicle][2] = object_location2
# 				print 'new coordinates: ', vehicle_dict[vehicle][:-1]

# 		print '\n', vehicle_dict
# 	return vehicle_dict



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


		# return up_grid, down_grid, up, down


		# check horizontal block
	# if position == 'vertical':
		# check vertical block
 
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
				total_vehicles.append(vehicle)
	total_vehicles_dict = Counter(total_vehicles)
	return vehicle_dict



def create_board(vehicle_dict):
	# new_grid = []

	new_grid = [['.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.'],
	        	['.', '.', '.', '.', '.', '.']]



	# new_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	#         	['.', '.', '.', '.', '.', '.', '.', '.', '.']]

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
	# # sys.exit()
	# print vehicle_dict
	# for vehicle, coordinates in vehicle_dict.iteritems():
	# 	coordinates = coordinates[:-1]
	# 	for i in range(0,len(coordinates)):
	# 		new_grid[coordinates[i][0]][coordinates[i][1]] = vehicle

	# df_new_grid = pd.DataFrame(new_grid)
	# print '\n new board: \n', df_new_grid
	return new_grid
	

	# for x in range(0,6):
	# 	for y in range(0,6):
	# 		if grid[x][y].isalpha():
	# 			vehicle = grid[x][y]
	# 			# add coordinates to vehicle
	# 			if vehicle in vehicle_dict:
	# 				vehicle_dict[vehicle].append([x,y])
	# 			else:
	# 				vehicle_dict[vehicle] = [[x,y]]
	# 			# print vehicle_dict
	# 			total_vehicles.append(vehicle)
	# total_vehicles_dict = Counter(total_vehicles)






# results = breadth_first_search(rushhour, max_depth=25)
# queue paths
queue = []
# explored paths
explored = []
# movelist = []
grids = []
# archive =  []




# def move_board(movelist, df_grid, vehicle_dict):
# 	while movelist:
# 		print '\n movelist: ', movelist
# 		node = movelist.pop(0)
# 		print 'First node: ', node
# 		print '\n GONNA MOVE THIS: ',node[1],
# 		print '\n Grid: \n', df_grid
# 		print vehicle_dict
# 		move(node, vehicle_dict, df_grid)
# 		print vehicle_dict_new
# 		new_df_grid = copy_board(vehicle_dict)
# 		print '\n New grid: \n', new_df_grid
# 		if df_grid_new not in grids:
# 			grids.append(df_grid_new)
# 	print 'grids: ',grids

	
	# 	if movelist == []:
	# 		for key, value in vehicle_dict.iteritems():
	# 			movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist)
	# 			print '\n movelist: ',movelist
	# 			move_board(movelist, df_grid,vehicle_dict)
	# print explored

# for key, value in vehicle_dict.iteritems():
# 	movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist, df_grid)
# new_movelist = movelist
# print '\n INITIAL MOVELIST: ',new_movelist
# move_board(movelist, df_grid, vehicle_dict)


#
#
############################################################################################
####					create board for each children node 							####
############################################################################################
#
# breadthfirst
#
# parent in archive
# if not goal
# children in queue
# if not goal,
# add children of first child to queue,
# if not goal
# add first child to archive, go to second child
#
#
# DFS
#
# parent to child, child in stack, not goal? 
# new child 
#
#
# board as parent 
# compare child move from movelist from parent board, different vehicle is moving vehicle, so add previous not moved vehicles
# - to create child board
# vehicle dict in queue
#
#
#
		# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist, df_grid)
		# movelist = movelist + movelist_temp
		# movelist = movelist + list(set(movelist_temp) - set(movelist))
		# vehicle_dict = move(key, vehicle_dict)
		# df_grid = copy_board(vehicle_dict)
		# print 'grid: \n', df_grid
		# shuffle(movelist)



######## heuristic formula #####
##      f(p)=cost(p)+h(p)    ###
################################
# where cost(p) is moves from space to goal and h(p) is vehicles blocking the way
# this is admissible heuristic, for it never overestimates


# for each vehicle in vehicle_dict 
#		calculate f(p):
#			cost(p) = calculate space r to goal x distance
#				h(p) = each unique block of path on x distance
#




# grid = [['.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.'],
#     	['.', 'R', 'R', '', '.', '.'],
#     	['.', '.', 'T', 'H', '.', '.'],
#     	['.', '.', 'T', 'H', '.', '.'],
#     	['.', '.', 'T', 'H', '.', '.']]

# grid = [['.', '.', '.', '.', '.', '.'],
#     	['.', '.', '.', '.', '.', '.'],
#     	['R', 'R', 'T', 'H', 'B', '.'],
#     	['.', '.', 'T', 'H', 'B', '.'],
#     	['.', '.', 'T', 'H', '.', '.'],
#     	['.', '.', 'C', 'C', '.', '.']]

# grid = [['.', '.', '.', '.', '.', 'D'],
#     	['.', '.', 'T', '.', '.', 'D'],
#     	['R', 'R', 'T', 'H', 'B', 'D'],
#     	['.', '.', 'T', 'H', 'B', '.'],
#     	['.', '.', '.', 'H', '.', '.'],
#     	['.', '.', 'C', 'C', '.', '.']]


# grid = [['.', 'Z', 'Z', 'Y', 'Y', 'Y'],
#     	['.', 'X', 'X', 'Q', 'P', 'P'],
#     	['R', 'R', 'O', 'Q', '.', 'S'],
#     	['J', 'J', 'O', 'M', 'M', 'S'],
#     	['I', '.', 'H', '.', 'N', 'N'],
#     	['I', '.', 'H', '.', '.', '.']]


# I’ve chosen to implement a voting system, where each car that blocks the lane of the red car can vote 
# for how it wants to free the lane (=”exit strategy”). The exit strategies that have the best 
# amount-of-cars-that-voted-for-this-exit-strategy/amount-of-cars-to-be-moved are going to get applied, 
# until the lane is free. The total amount of cars to be moved for sure is the heuristic value then. 
# E.g. for the picture above, the size-3 purple car is blocking the lane of the red car. It cannot move up, 
# as there is too less space for this car. It’s exit strategy will be down, for which the size-2 black car 
# and the size-3 blue car have to be moved.This will be the exit strategy the purple car votes for. 
# Calculation of the heuristic value = sum of moves to be done at least until the puzzle has been completed:




# # TO DO!!!!!
# # WRITE HEURISTIC, WHEN R CLOSE TO EXIT GIVE PRIORITY!!

# # add parent grid
# def calculate_costs(vehicle_dict, child_df_grid):
# 	cost_p = 0
# 	h_p = 0
# 	cost_p = goal[1] - vehicle_dict['R'][1][1] 
# 	# cost_p = 1
# 	print ' \n\n ---------------------------------- entered here ------------------------------------'
# 	# calculate h(p) by ranging over posision of r and checking grids right of r for any other cars
# 	for i in range(len(vehicle_dict['R'][:2])+vehicle_dict['R'][0][1],len(child_df_grid)):
# 		# print child_df_grid[i][vehicle_dict['R'][1][0]]
# 		if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
# 			# print 'before if:',child_df_grid[i][vehicle_dict['R'][1][0]]
# 			# print 'before 1:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
# 			if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) > 3 or (len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) == 3 and str(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]).isdigit()):
# 				# print i
# 				print child_df_grid[i][vehicle_dict['R'][1][0]]
# 				print '1a:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
# 				print '1b:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]
# 				print '1c:',vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]
# 				# print '\n car: ', child_df_grid[i][vehicle_dict['R'][1][0]]
# 				# print 'wooh'
# 				for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
# 					# if child_df_grid[p][vehicle_dict['R'][1][0]].isalpha():
# 					# print 'x: ', x
# 					if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha():
# 						h_p += 1
# 					# print 'below truck: ', child_df_grid[p]
				
# 				h_p += (2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1])-vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]
# 				# -vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]))-(cost_p)
# 				print h_p
# 			if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) < 3:
# 				print child_df_grid[i][vehicle_dict['R'][1][0]]
# 				print '2a:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]
# 				print '2b:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][0]
# 				print '2c:', vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
# 				h_p += 2.2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
# 				# -vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][0]))-(cost_p)
# 				# h_p += 2**cost_p-
# 				# if child_df_grid[i][vehicle_dict['R'][1][0]] == 'E':
# 			# 	# print 'yes'
# 			# 	h_p += 2*h_p

# 	# for i in range(len(vehicle_dict['R'])+vehicle_dict['R'][0][1],len(child_df_grid)):
# 	# 	if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
# 	# 		h_p += 1
# 	print '\n', child_df_grid
# 	print '\n cost(p):',cost_p, ' h(p):', h_p, 'total :', cost_p + h_p,'\n'
# 	# f_p = cost_p + h_p
# 	# sys.exit()
# 	return cost_p + h_p


# order queue by value of f(p) - low value is best
def start_bfs(start_grid):
	z = 0
	find_path = dict()
	vehicle_dict = dict()
	archive = deque()
	queue = deque()
	temp_vehicle_dict = set_up(vehicle_dict,pd.DataFrame(start_grid))
	# temp_cost_child = calculate_costs(temp_vehicle_dict, pd.DataFrame(start_grid))
	# print temp_cost_child
	# sys.exit()
	queue.append(start_grid)
	find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
	while queue:
		vehicle_dict.clear()
		# print 'queue: ',queue.queue
		df_grid = queue.popleft()
		# print '\n\n\n value: '
		# print df_grid[0]
		# df_grid = df_grid[1]
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
					# print type(child_df_grid)
					# sys.exit()
					# print child_df_grid
					if not child_df_grid in archive:
						# cost_child = calculate_costs(new_vehicle_dict, pd.DataFrame(child_df_grid))
						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						check_goal(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path) #key error: 'r'
						queue.append(child_df_grid)
						archive.append(child_df_grid)

			# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist, df_grid)
				# new_movelist = movelist
			# print '\n INITIAL MOVELIST: ',new_movelist
			# queue = []
			# print '\n MOVELIST \n', movelist, '\n'
			# for i in range(0,1):
				# print total_vehicles_dict
				# print vehicle_dict
				# for key, value in vehicle_dict.iteritems():
				# 	print 'key \n', key, value
			# # 	# 				A, [[4, 0], [5, 0], 'vertical']
			# # 	# sys.exit()
			# while new_movelist:	
			# 	# print '\n ***** start loop ***** \n'
			# 	# print '\n movelist before pop: \n', new_movelist
			# 	node = new_movelist.pop(0)
			# 	# print '\n movelist after pop: \n', movelist
			# 	# print '\n\n Moving child: ',node,'\n'
			# 	# print 'parent grid: \n', df_grid
			# 	new_vehicle_dict = move(node, copy.deepcopy(vehicle_dict), df_grid)
			# 	# print 'movelist type and node type: ', type(new_movelist), type(node)
			# 	child_df_grid = create_board(new_vehicle_dict)
			# 	print 'child df: \n', child_df_grid
			# 	check_goal(node[1], new_vehicle_dict, archive, df_grid, child_df_grid) #key error: 'r'
			# 	queue.append(child_df_grid)
			# 	# set_up(child_df_grid)
			# 	# print 'test: ', child_df_grid
			# 	# print '\n\n Vehicle dict: ',new_vehicle_dict,'\n'
			# 	# print '\n Child node: \n', child_df_grid, '\n current child:', node[1]
			# 	# print '\n **** end of loop **** \n' 

			# if df_grid not in archive:
			# archive.append(copy.deepcopy(df_grid))
			# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, df_grid)
	



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


################################################################################################
##### 
##### breadth first per auto implementeren
##### fixed auto list  (geen queue)
##### per auto en alle moves:
##### doe move
##### zet terug
##### 	zet in queue (board)
#####	zet in archive



#

# #
# Beam search uses breadth-first search to build its search tree. 
# At each level of the tree, it generates all successors of the states at the current level, 
# sorting them in increasing order of heuristic cost. However, it only stores a predetermined number, β, 
# of best states at each level (called the beam width). Only those states are expanded next. 
# The greater the beam width, the fewer states are pruned. With an infinite beam width, 
# no states are pruned and beam search is identical to breadth-first search.
#  The beam width bounds the memory required to perform the search. Since a goal state could potentially be pruned, 
#  eam search sacrifices completeness (the guarantee that an algorithm will terminate with a solution, if one exists). 
#  Beam search is not optimal (that is, there is no guarantee that it will find the best solution). 
#  It returns the first solution found.

# The beam width can either be fixed or variable. One approach that uses a variable beam width starts with 
# the width at a minimum. If no solution is found, the beam is widened and the procedure is repeated.


################################################################################################
 
################################################################################################

 # best first searsch > trucks vertical in pad naar uitgang hebben priority
 # beam search
################################################################################################





		# # remove explored
		# if node not in explored:
			
		# 	print '\n\n NOT IN EXPLORED NODE: ',node, '\n','direction: ',direction,'\n'
		# 	# movelist2, object_location2, direction2 = get_movelist(key, value, vehicle_dict, movelist)
		# 	# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist)
		# 	print '\n Before grid: \n', df_grid
		# 	# print '\n movelist before \n', movelist
		# 	# explored.append(node)
		# 	print '\n\n GONNA MOVE THIS: ',node[1],'\n'
		# 	vehicle_dict = move(node, vehicle_dict, df_grid)
		# 	print '\n \n VEHICLE DICT: \n\n', vehicle_dict
		# 	df_grid = copy_board(vehicle_dict)
		# 	print 'copyboard vechiledict: \n', vehicle_dict
		# 	print '\n Archive before: \n', archive
		# 	if vehicle_dict not in archive:
		# 		archive.append(vehicle_dict) #copy deepcopy?
		# 	print '\n After grid: \n', df_grid
		# 	print '\n Archive after: \n', archive
		# 	# movelist2, object_location2, direction2 = get_movelist(key, value, vehicle_dict, movelist)
		# 	# print 'MOVELISTS: \n', movelist,'\n',movelist2
		# 	# sys.exit()
		# 	# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist)
		# 	print '\n movelist after \n', movelist
		# 	print '\n explored: \n', explored
		# 	check_goal(node[1], vehicle_dict)

		# 	# movelist, object_location, direction = get_movelist(key, value, vehicle_dict, movelist)

		# else:
		# 	print '\n NO MORE MOVES \n'
		# 	# explored.pop(0)
		# 	shuffle(movelist)






# 			# print vehicle_dict
			
	
		# while queue:

	
		# print 'grid: \n', df_grid
		# print '\n', movelist
	# print 'final grid: \n', df_grid, '\n', movelist
	# print graph	


################################################################################################
##### TO DO: CREATE BREADTH FIRST ALGORITHM BY ADDING TO QUEUE AND GETTING CHILDREN NOTES  #####
################################################################################################
 

# visits all the nodes of a graph (connected component) using BFS
# def bfs_connected_component(graph, start):
# 	print graph	
# 	# queue paths
# 	queue = []
# 	# explored paths
# 	explored = []
# 	for i in range(len(start)):
# 		queue.append(start[i][1:][1:][0])
# 	print queue

# 	while queue:
# 		node = queue.pop(0)
# 		# print node
# 		if node not in explored:
# 			print node
# 			explored.append(node)
# 			check_adjecent(node)
# 			neighbours = graph[node]
# 			print neighbours


# 	sys.exit()
#     # keep track of all visited nodes
# 	explored = []
# 	# keep track of nodes to be checked
# 	queue = [start[1]]

# 	# keep looping until there are nodes still to be checked
# 	while queue:
# 	# pop shallowest node (first node) from queue
# 		node = queue.pop(0)
# 		if node not in explored:
# 	# add node to list of checked nodes
# 			explored.append(node)
# 			neighbours = graph[node]

# 	# add neighbours of node to queue
# 	for neighbour in neighbours:
# 		queue.append(neighbour)
# 	return explored
 





# for index, value in enumerate(grid):
# 	vehicle = car
# 	if vehicle in value:
# 		subindex_vehicle = value.index(vehicle)
# 		check_adjecent(index, subindex_vehicle, vehicle, vehicles)
		

# print 'my car position: ', [index, subindex_vehicle]

# check adjecent grids for other C and save that C with horizontal or vertical information in dictionary


# read grid


# for index, value in enumerate(grid):
# 	if car in value:
# 		subindex_car = value.index(car)
# 		print 'car position: ',[index, subindex_car]





# update grid

# show grids between goal and current location





# horizontal moves

# vertical moves






