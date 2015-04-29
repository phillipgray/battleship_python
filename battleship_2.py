from bs_module import *

the_size = 8
new_board = board_fill(the_size)
# print new_board

print_board(new_board)

whole_board_list = generate_position_list(the_size)

taken_list = []

test_1 = ship_start_space(whole_board_list)
# print ship_direction()

ans_1 = generate_location(5, whole_board_list, taken_list)

print ans_1