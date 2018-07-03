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

import grid_class
import vehicle_class
import board_class

board = board_class.board
vehicle = vehicle_class.vehicle
total_vehicles = []
vehicles = {}
mycar = 'R'
car = 'C'
truck = 'T'
finished = False


class algorithm:

	# custom heuristic function for 6x6 boards
	@staticmethod
	def calculate_costs_6x6(current_vehicle, vehicle_dict, child_df_grid, goal):
		cost_p = 0
		h_p = 0
		cost_p = goal[1] - vehicle_dict['R'][1][1] 
		# calculate h(p) by ranging over position of red car and checking grids on the right side of red for any other cars
		for i in range(len(vehicle_dict['R'][:2])+vehicle_dict['R'][0][1],len(child_df_grid)):
			if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
				# checks if blocking vehicles are trucks
				if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) > 3 or (len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) == 3 
					and str(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]).isdigit()):
					for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],
						len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
						# checks if car that blocks R is blocked by any horizontal vehicle
						if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha():
							h_p += 1
					h_p += (2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1])-vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]
				# checks blocking vehicles that are cars
				if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) < 3:
					h_p += 2.2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
		return cost_p + h_p

	# custom heuristic function for 9x9 boards	
	@staticmethod
	def calculate_costs_9x9(current_vehicle, vehicle_dict, child_df_grid, goal):
		cost_p = 0
		h_p = 0
		cost_p = goal[1] - vehicle_dict['R'][1][1] 
		# calculate h(p) by ranging over posision of r and checking grids right of r for any other cars
		for i in range(len(vehicle_dict['R'][:2])+vehicle_dict['R'][0][1],len(child_df_grid)):
			if child_df_grid[i][vehicle_dict['R'][1][0]] == '.' and (i == vehicle_dict['R'][1][1] +1):
				h_p -= 3
			# checks if element is car
			if child_df_grid[i][vehicle_dict['R'][1][0]].isalpha():
				if child_df_grid[i][vehicle_dict['R'][1][0]] == current_vehicle[-2:-1][0]:
					h_p -= 2
				# checks if blocking vehicles are trucks
				if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) > 3 or (len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) == 3 
					and str(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][0]).isdigit()):
					for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],
						len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
						# checks if car that blocks R is blocked by any horizontal vehicle
						if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha(): 
							h_p += 4
						else: h_p += 2
					for x in range(len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0],
						len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][:3])+vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][0][0]+1):
						x = x-4
						if child_df_grid[vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1]][x].isalpha():
							h_p += 2
						else: h_p += 1
					h_p += (1.2**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][2][1])	
				# checks if blocking vehicles are cars	
				if len(vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]]) < 3:
					h_p += 1.3**vehicle_dict[child_df_grid[i][vehicle_dict['R'][1][0]]][1][1]
		f_p = cost_p + h_p

		return (cost_p + h_p)*cost_p

	# a_star cost function with heuristic function
	@staticmethod
	def a_star(moved_nodes, vehicle_dict, child_df_grid, goal):
		blocking_cars = 0
		total_cost = 0
		distance_to_goal = goal[1] - vehicle_dict['R'][1][1] 
		total_cost = moved_nodes + distance_to_goal 
		return total_cost

	# BFS implemenation that uses heapq to sort child nodes for 9x9 boards
	@staticmethod
	def start_bfs_basic_9x9(start_grid, start_time, algorithm_name):
		finished = False
		goal = [4,8]
		z = 0
		iterations = 0
		cost_child = 0
		find_path = dict()
		vehicle_dict = dict()
		archive = deque()
		count_board = 0
		board_count_dict = dict()
		heap_queue = []
		heap_archive = []
		temp_vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(start_grid))
		heapq.heappush(heap_queue,(goal[1] - temp_vehicle_dict['R'][1][1],start_grid))
		find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
		# while heap is not empty
		while heap_queue:
			print 'QUEUE SIZE: ', len(heap_queue)
			print 'ITERATIONS: ', iterations
			vehicle_dict.clear()
			df_grid = heapq.heappop(heap_queue)
			df_grid = df_grid[1]
			print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
			vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(df_grid))
			print "--- %s seconds ---" % (time.time() - start_time)
			# for all vehicles on this particular parent board
			for key, value in vehicle_dict.iteritems():
				vehicle.check_adjecent(key, value, vehicle_dict)
				# creates list of moveable vehicles
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
				if not movelist:
					continue
				while movelist:
					node = movelist.pop(0)
					iterations += 1
					new_vehicle_dict = vehicle.move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
					child_df_grid = board.create_board_9x9(new_vehicle_dict)
					# counts amount of moves made on current child board from start board
					if str(child_df_grid) in board_count_dict:
						count_board = board_count_dict.get(str(child_df_grid))
					# if child not previously visited
					if not child_df_grid in heap_archive:
						board_count_dict[str(child_df_grid)] = count_board + 1
						if algorithm_name == 'a-star':
							cost_child = algorithm.a_star(board_count_dict.get(str(child_df_grid)),new_vehicle_dict,pd.DataFrame(child_df_grid),goal)
						if algorithm_name == 'custom heuristic':
							cost_child = algorithm.calculate_costs_9x9(node, new_vehicle_dict, pd.DataFrame(child_df_grid),goal)
						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						heap_archive.append(child_df_grid)
						 # check if child board reaches goal
						finished = vehicle.check_goal_9x9(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path, start_grid, start_time)
						if finished:
							return
						heapq.heappush(heap_queue,(cost_child, child_df_grid))


	# BFS implemenation that uses heapq to sort child nodes for 6x6 boards
	@staticmethod
	def start_bfs_basic_6x6(start_grid, start_time, algorithm_name):
		finished = False
		goal = [2,5]
		z = 0
		iterations = 0
		cost_child = 0
		find_path = dict()
		vehicle_dict = dict()
		archive = deque()
		count_board = 0
		board_count_dict = dict()
		heap_queue = []
		heap_archive = []
		temp_vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(start_grid))
		heapq.heappush(heap_queue,(goal[1] - temp_vehicle_dict['R'][1][1],start_grid))
		find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
		# while heap is not empty
		while heap_queue:
			print 'QUEUE SIZE: ', len(heap_queue)
			print 'ITERATIONS: ', iterations
			vehicle_dict.clear()
			df_grid = heapq.heappop(heap_queue)
			df_grid = df_grid[1]
			print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
			vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(df_grid))
			print "--- %s seconds ---" % (time.time() - start_time)
			# for all vehicles on this particular parent board
			for key, value in vehicle_dict.iteritems():
				vehicle.check_adjecent(key, value, vehicle_dict)
				# creates list of moveable vehicles
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
				if not movelist:
					continue
				while movelist:
					node = movelist.pop(0)
					iterations += 1
					new_vehicle_dict = vehicle.move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
					child_df_grid = board.create_board_6x6(new_vehicle_dict)
					# counts amount of moves made on current child board from start board
					if str(child_df_grid) in board_count_dict:
						count_board = board_count_dict.get(str(child_df_grid))
					# if child not previously visited
					if not child_df_grid in heap_archive:
						board_count_dict[str(child_df_grid)] = count_board + 1
						if algorithm_name == 'a-star':
							cost_child = algorithm.a_star(board_count_dict.get(str(child_df_grid)),new_vehicle_dict,pd.DataFrame(child_df_grid),goal)
						if algorithm_name == 'custom heuristic':
							cost_child = algorithm.calculate_costs_6x6(node, new_vehicle_dict, pd.DataFrame(child_df_grid),goal)
						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						heap_archive.append(child_df_grid)
						 # check if child board reaches goal
						finished = vehicle.check_goal_6x6(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path, start_grid, start_time)
						if finished:
							return
						heapq.heappush(heap_queue,(cost_child, child_df_grid))

	# Breadth first search constructor
	@staticmethod
	def start_bfs_6x6(start_grid, start_time, algorithm_name):
		z = 0
		find_path = dict()
		goal = [2,5]
		vehicle_dict = dict()
		archive = deque()
		queue = deque()
		count_board = 0
		iterations = 0
		temp_vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(start_grid))
		# creates queue for BFS
		queue.append(start_grid)
		find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
		# while queue is not empty
		while queue:
			vehicle_dict.clear()
			df_grid = queue.popleft()
			print 'QUEUE SIZE: ', len(queue)
			print 'iterations: ', iterations
			print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
			archive.append(df_grid)
			vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(df_grid))
			print "--- %s seconds ---" % (time.time() - start_time)
			# for all vehicles in the parent board
			for key, value in vehicle_dict.iteritems():
				vehicle.check_adjecent(key, value, vehicle_dict)
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
				if not movelist:
					continue
				while movelist:
						iterations += 1
						node = movelist.pop(0)
						new_vehicle_dict = vehicle.move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
						child_df_grid = board.create_board_6x6(new_vehicle_dict)
						# checks in child board has been visited already
						if not child_df_grid in archive:
							find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
							finished = vehicle.check_goal_6x6(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path, start_grid, start_time) #key error: 'r'
							if finished:
								return
							queue.append(child_df_grid)
							archive.append(child_df_grid)

	# random algorithm constructor for 6x6 boards
	@staticmethod
	def start_random_6x6(start_grid, start_time, algorithm_name):
		z = 0
		iterations = 0
		find_path = dict()
		vehicle_dict = dict()
		archive = deque()
		count_board = 0
		heap_queue = []
		heap_archive = []
		queue = []
		temp_vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(start_grid))
		queue.append(start_grid)
		find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
		while queue:
			print 'QUEUE SIZE: ', len(queue)
			print 'ITERATIONS: ', iterations
			vehicle_dict.clear()
			# pick a random board from the queue
			df_grid = queue.pop(random.randrange(len(queue)))
			print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
			vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(df_grid))
			print "--- %s seconds ---" % (time.time() - start_time)
			# for each vehicle on the board
			for key, value in vehicle_dict.iteritems():
				vehicle.check_adjecent(key, value, vehicle_dict)
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
				if not movelist:
					continue
				# for every vehicle that is able to move on the board
				while movelist:
					node = movelist.pop(0)
					iterations += 1
					new_vehicle_dict = vehicle.move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
					# create a child board
					child_df_grid = board.create_board_6x6(new_vehicle_dict)
					# checks if child board has been visited already
					if not child_df_grid in heap_archive:
						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						heap_archive.append(child_df_grid)
						# checks if child board reaches goal
						finished = vehicle.check_goal_6x6(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path, start_grid, start_time)
						if finished:
							return
						queue.append(child_df_grid)

# random algorithm constructor for 9x9 boards
	@staticmethod
	def start_random_9x9(start_grid, start_time, algorithm_name):
		z = 0
		iterations = 0
		find_path = dict()
		vehicle_dict = dict()
		archive = deque()
		count_board = 0
		heap_queue = []
		heap_archive = []
		queue = []
		temp_vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(start_grid))
		queue.append(start_grid)
		find_path[tuple(tuple(x) for x in start_grid)] = tuple(tuple(x) for x in start_grid)
		while queue:
			print 'QUEUE SIZE: ', len(queue)
			print 'ITERATIONS: ', iterations
			vehicle_dict.clear()
			# pick a random board from the queue
			df_grid = queue.pop(random.randrange(len(queue)))
			print ' ----------------------------------------\n parent grid: \n', pd.DataFrame(df_grid),'\n --------------------------------------- \n \n '
			vehicle_dict = board.set_up(vehicle_dict,pd.DataFrame(df_grid))
			print "--- %s seconds ---" % (time.time() - start_time)
			# for each vehicle on the board
			for key, value in vehicle_dict.iteritems():
				vehicle.check_adjecent(key, value, vehicle_dict)
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, pd.DataFrame(df_grid))
				if not movelist:
					continue
				# for every vehicle that is able to move on the board
				while movelist:
					node = movelist.pop(0)
					iterations += 1
					new_vehicle_dict = vehicle.move(node, copy.deepcopy(vehicle_dict), pd.DataFrame(df_grid))
					# create a child board
					child_df_grid = board.create_board_9x9(new_vehicle_dict)
					# checks if child board has been visited already
					if not child_df_grid in heap_archive:
						find_path[tuple(tuple(x) for x in child_df_grid)] = tuple(tuple(x) for x in df_grid)
						heap_archive.append(child_df_grid)
						# checks if child board reaches goal
						finished = vehicle.check_goal_9x9(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, find_path, start_grid, start_time)
						if finished:
							return
						queue.append(child_df_grid)

	# Depth first search constructor, uses stack instead of a queue that is used for the other algorithms				
 	@staticmethod 
	def start_dfs(start_grid):
		start_grid = start_grid
		movelist = []
		vehicle_dict = dict()
		stack = deque()
		stack.append(pd.DataFrame(start_grid))
		while stack:
			vehicle_dict.clear()
			df_grid = stack.popleft()
			vehicle_dict = board.set_up(vehicle_dict,df_grid)
			if not True in [df_grid.equals(x) for x in archive]:
				movelist = []
				for key, value in vehicle_dict.iteritems():
					vehicle.check_adjecent(key, value, vehicle_dict)
					movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, df_grid)
				new_movelist = movelist
				while new_movelist:	
					node = new_movelist.pop(0)
					new_vehicle_dict = move(node, copy.deepcopy(vehicle_dict), df_grid)
					child_df_grid = board.create_board(new_vehicle_dict)
					vehicle.check_goal(node[1], new_vehicle_dict, archive, df_grid, child_df_grid, start_grid) 
					stack.append(child_df_grid)
				# if df_grid not in archive:
				archive.append(copy.deepcopy(df_grid))
				movelist, object_location, direction = board.get_movelist(key, value, vehicle_dict, df_grid)
		
