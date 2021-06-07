def input_board():
	'''
	reads from readfile.txt and creates a board
	returns - board / sudoku
	'''

	file = open('readfile.txt',mode='r')
	board=[]
	for x in file:
		row=[]
		for ch in x:
			if ch=='\n':
				pass
			else:
				row.append(int(ch))
		board.append(row)

	file.close()
	return board


def print_board(bo):
	'''
	prints the board in a stylised fashion 
	'''
	for i in range(len(bo)):
		if i%3==0 and i!=0:
			print('- - - - - - - - - - - -')

		for j in range(len(bo[0])):
			if j%3==0 and j!=0:
				print(' | ',end="")

			if j==8:
				print(bo[i][j])
			else:
				print(str(bo[i][j])+' ',end="")


def find_empty(bo):
	'''
	finds empty spaces i.e. '0' on the board 
	returns tuple (i,j)
	'''
	for row in range(9):
		for col in range(9):
			if(bo[row][col]== 0):
				return (row,col)
	return False

def valid(bo,num,pos):
	'''
	checking if the board is valid
	bo - board
	num - number we entered in the board
	pos - tuple (x,y) , position of the entry on the board

	returns True is number is valid , False if not 
	'''
	x,y = pos
	#checking if row is valid
	for i in range(len(bo[0])):
		if bo[x][i] == num: 
			return False

	#checking if column is valid
	for i in range(len(bo)):
		if bo[i][y]==num:
			return False

	#check box say (0,4)
	box_x = x//3 # box_x = 0  
	box_y = y//3 # box_y= 1

	for i in range(box_x*3, box_x*3 +3):
		for j in range(box_y*3, box_y*3 +3):
			if bo[i][j]==num and (i,j)!=pos:
				return False

	return True


def solve(bo):
	'''
	takes board as the input 
	if we do not find an empty space i.e. reached the end, as we are using backtracking, the only way to reach the
	end is if we have found the solution and we output the board
	
	else
	we keep backtracking using recursion till we find the valid solution 

	returns True or False

	'''
	found = find_empty(bo)
	if not found:
		return True
	else:
		row,col = found

	for i in range(1,10):
		if valid(bo,i,(row,col)):
			bo[row][col]= i

			if solve(bo):
				return True

			bo[row][col]=0
	return False



if __name__ == "__main__":
	board = input_board()
	print("before the solving")
	print_board(board)
	print(" ")
	solve(board)
	print(" ")
	print("after the solving")
	print_board(board)




