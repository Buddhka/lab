import random
import io
import subprocess
import time
from contextlib import redirect_stdout
import numpy as np
import os,sys
from PIL import Image, ImageGrab, ImageDraw
from tkinter import Tk, Canvas, Frame, BOTH, Button

def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(str(maze[i][j]), end="")
			elif (maze[i][j] == '⬜'):
				print(str(maze[i][j]), end="")
			else:
				print(str(maze[i][j]), end="")
			
		print('\n')

def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '⬜'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '⬜'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '⬜'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '⬜'):
		s_cells += 1

	return s_cells

f = open('utility.txt','r')
s = f.readlines()
filepath = ''.join(s[0:1]).rstrip()
f.close()
width1,height1 = 800,800
wall = '⬛'
cell = '⬜'
unvisited = 'u'
height = int(''.join(s[1:2]).rstrip())
width = int(''.join(s[2:3]).rstrip())
maze = []


for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

maze[starting_height-1][starting_width] = '⬛'
maze[starting_height][starting_width - 1] = '⬛'
maze[starting_height][starting_width + 1] = '⬛'
maze[starting_height + 1][starting_width] = '⬛'

while (walls):
	rand_wall = walls[int(random.random()*len(walls))-1]

	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '⬜'):
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = '⬜'

				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]-1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]+1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]-1] = '⬛'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '⬜'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = '⬜'

				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]-1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]-1] = '⬛'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]+1] = '⬛'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '⬜'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = '⬜'

				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]+1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]-1] = '⬛'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]+1] = '⬛'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '⬜'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = '⬜'

				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '⬜'):
						maze[rand_wall[0]][rand_wall[1]+1] = '⬛'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]+1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != '⬜'):
						maze[rand_wall[0]-1][rand_wall[1]] = '⬛'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = '⬛'

for i in range(0, width):
	if (maze[1][i] == '⬜'):
		maze[0][i] = '⬜'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == '⬜'):
		maze[height-1][i] = '⬜'
		break
#----------------------------------------------------------------------
#50 пикселей на 1 единицу ширины или высоты, bmp file 
printMaze(maze)
image1 = Image.new("RGB",(800,800))
draw = ImageDraw.Draw(image1)
print('pause')
f = open('export.txt','w')
for i in range(0,height):
	for j in range(0,width):
		if maze[i][j] == '⬛':
						draw.rectangle(((width1/width)*j,(height1/height)*i,(width1/width)*(j+1),(height1/height)*(i+1)),fill ='#000000' , outline = '#000000')
						f.write('1')
		else:
						draw.rectangle(((width1/width)*j,(height1/height)*i,(width1/width)*(j+1),(height1/height)*(i+1)),fill ='#ffffff' , outline = '#ffffff')
						f.write('0')
		
	print('\n')
	f.write('\n')
filename = '/PILImage.png'
image1.save(filepath + filename,"PNG")
f.close()
print(filepath)
