from time import sleep

board = [
	[1,1,0,1,1,1,1,1,1,1],
	[1,1,0,1,1,0,0,0,0,5],
	[1,1,0,1,1,0,1,1,1,1],
	[0,0,0,0,0,0,1,1,1,1],
	[1,1,1,1,0,1,1,1,1,1],
	[1,1,1,1,0,1,1,1,1,1]
]
#printing the board in a fancy way
def print_board(brd):
	for row in range(0,len(brd)):
		print(""" 
		""")
		for col in range(0,len(brd[0])):
			if col == 0:
				print(end='')
			else:
				print('|',end='')

			if brd[row][col] == 1:
				print(f'  # ',end='')
			elif brd[row][col] == 0:
				print(' __ ',end='')
			else:
				print(f'{brd[row][col]}',end='')


def outofbounce(pos,brd):
	row  = pos[0]
	col = pos[1]

	if row >= len(brd)-1 or \
		row < 0 or \
		col > len(brd[0])-1 or \
		col < 0 :
		return True
	return False

print(outofbounce((3,-1),board))


def front_clear(pos,brd):
    row  = pos[0]
    col = pos[1]

    if brd[row][col] == 1:
        return False
    return True

#dfs algorithm for matrix graph
def find_path(pos,brd,location,COUNT=0,sign=' ?? '):
	COUNT += 1
	row,col = pos    
	if brd[row][col] == location:
		return True
	direction = [
        (-1,0),#top
        (0,-1), #left
		(1,0),#down
		(0,1),#right	
	    ]
	for dir in direction:
		new_x = row + dir[0]
		new_y = col + dir[1]
		prev = pos
		#checking if the its not out of bounce

		if brd[new_x][new_y] == sign:
			pos = prev
			continue 
		if not front_clear((new_x,new_y),brd):
		    continue

		if not outofbounce((new_x,new_y),brd) and front_clear((new_x,new_y),brd):

			brd[row][col] = sign

			pos = (new_x,new_y)

			sleep(1)
			print('\n')
			print(pos,'\n')

			print_board(brd)
			if find_path(pos,brd,location,COUNT,sign):
				return True
		elif outofbounce((new_x,new_y),brd):
			return False
	return 



#get the start position from where you want to begin the search
def get_start_pos():
	start = None
	while True:
		start = input('\n\nEnter starting position both x and y(e.g 24): ')
		if len(start) != 2 or not start.isdigit():
			print('please enter 2 integers(e.g 24)')
			continue
		else:
			break

	x_pos,y_pos = int(start[0]),int(start[1])
	return (x_pos,y_pos)



#the main driver function
def main(num):
	print_board(board)
	if find_path(get_start_pos(),board,num):
		print('\npath found')

main(5)