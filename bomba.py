mat =[]
xlenght = int(input())
ylenght = int(input())

def populate_left(x,y,value):
	mat[x][y] = value
	populate_diagonal_left_up(x,y,value)
	populate_diagonal_left_down(x,y,value)
	if(x==0):
		return 0;
	else:
		populate_left(x-1,y,value+12)

def populate_diagonal_left_up(x,y,value):
	mat[x][y] = value
	if(x==0 or y==0):
		return 0;
	else:
		return populate_diagonal_left_up(x-1,y-1,value+11)

def populate_diagonal_left_down(x,y,value):
	mat[x][y] = value
	if(x==0 or y==ylenght-1):
		return 0;
	else:
		return populate_diagonal_left_down(x-1,y+1,value+13)

def populate_right(x,y,value):
	mat[x][y] = value
	populate_diagonal_right_up(x,y,value)
	populate_diagonal_right_down(x,y,value)
	if(x==xlenght-1):
		return 0;
	else:
		populate_right(x+1,y,value+16)

def populate_diagonal_right_up(x,y,value):
	mat[x][y] = value
	if(x==xlenght-1 or y==0):
		return 0;
	else:
		return populate_diagonal_right_up(x+1,y-1,value+17)

def populate_diagonal_right_down(x,y,value):
	mat[x][y] = value
	if(x==xlenght-1 or y==ylenght-1):
		return 0;
	else:
		return populate_diagonal_right_down(x+1,y+1,value+15)		

def populate_down(x,y,value):
	mat[x][y] = value
	if(y==ylenght-1):
		return 0;
	else:
		populate_diagonal_left_down(x-1,y+1,value+13)
		populate_diagonal_right_down(x+1,y+1,value+15)
		return populate_down(x,y+1,value+14)

def populate_up(x,y,value):
	mat[x][y] = value
	if(y==0):
		return 0
	else:
		populate_diagonal_right_up(x+1,y-1,value+17)
		populate_diagonal_left_up(x-1,y-1,value+11)
		return populate_up(x,y-1,value+10)


def printarray():
	for x in range(xlenght-1):
		for y in range(ylenght-1):
			print(mat[y][x], end=' | ')
		print()
	print('\n---------------')

def main():
	for x in range(xlenght):
		temp = []
		for y in range(ylenght):
			temp.append(0)
		mat.append(temp)

	xPlode = int(input())
	yPlode = int(input())

	populate_left(xPlode,yPlode, 0)
	printarray()
	populate_right(xPlode,yPlode, 0)
	printarray()
	populate_down(xPlode,yPlode, 0)
	printarray()
	populate_up(xPlode,yPlode, 0)
	printarray()

main()
