import numpy as np
a=""
b=[]
f=0
print("Do you want to play tic-tac-toe")
print("Press S to play single-player and M to play multi-player ")
w,h=2,2
s=[[1,2,3],[4,5,6],[7,8,9]]
s1=[[1,2,3],[4,5,6],[7,8,9]]
def game():
	for i in range(3):
		for j in range(3):
			print(s[i][j],end=" ")
		print()
	
a=input()
if (a=="M"):
	c=0
	d=0
	game()
	while(f==0):
        #code for multi-player
		if(d==0):
			print("This the turn for player1 :")
			print("Enter the location where you want to put a cross")
			k=int(input())
			for i in range(3):
				for j in range(3):
					if(s1[i][j]==k):
						if(s[i][j]=='x' or s[i][j]=='o'):
							print("invalid move")
							c=1
							game()
							break
						else:
							s[i][j]='x'
							c=0
							game()
							break
		if(c==0):
			print("This the turn for player2 :")
			print("Enter the location where you want to put a circle")
			k=int(input())
			for i in range(3):
				for j in range(3):
					if(s1[i][j]==k):
						if(s[i][j]=='x' or s[i][j]=='o'):
							print("invalid move")
							d=1
							game()
							break
						else:
							s[i][j]='o'
							d=0
							game()
							break
	
		
