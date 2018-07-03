import cProfile
import algorithm_class 
import grid_class
import vehicle_class
import board_class
import time
import sys

def start():
	algorithm = algorithm_class.algorithm
	boards = grid_class.grid
	start_time = time.time()

	number = None
	number_2 = None
	while number is None:
	    input_value = input("Please enter board (1 to 6): ")
	    try:
	        # convert string to number
	        number = int(input_value)
	    except ValueError:
	        # incorrect number
	        print("{input} is not a number, please enter a correct number".format(input=input_value))
	while number_2 is None:
	    input_value_2 = input("Please choose algorithm number: 1 (A-star), 2 (BFS), 3 (Custom heuristic), 4 (Random)  ")
	    try:
	        # covert string to number
	        number_2 = int(input_value_2)
	    except ValueError:
	        # incorrect number
	        print("{input} is not a correct number, please enter a correct number".format(input=input_value))

	# 6x6 boards
	if 1 <= number <= 3:
		new_board = boards.board(number)
		# selects right algorithm
		if number_2 == 1:
			custom_heuristic = algorithm.start_bfs_basic_6x6(new_board,start_time, 'a-star')
		if number_2 == 2:
			custom_heuristic = algorithm.start_bfs_6x6(new_board,start_time, 'bfs')
		if number_2 == 3:
			custom_heuristic = algorithm.start_bfs_basic_6x6(new_board,start_time, 'custom heuristic')
		if number_2 == 4:
			custom_heuristic = algorithm.start_random_6x6(new_board,start_time, 'random')
	# 9x9 boards
	if 4 <= number <= 6:
		new_board = boards.board(number)
		# selects right algorithm
		if number_2 == 1:
			custom_heuristic = algorithm.start_bfs_basic_9x9(new_board,start_time, 'a-star')
		if number_2 == 4:
			custom_heuristic = algorithm.start_random_9x9(new_board,start_time, 'random')
		if number_2 == 3:
			custom_heuristic = algorithm.start_bfs_basic_9x9(new_board,start_time, 'custom heuristic')
		if number_2 == 2:
			print 'BFS is not implemented for 9x9 boards'
			sys.exit()

start()