import numpy as np
a=""
b=[]
f=0
b=0
v=0
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
	k=0
	f=0
	c=0
	d=0
	game()
	while(f==0):
        #code for multi-player
		n=0
		#PLAYER 1 INPUT
		if(d==0 ):
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
				#CHECK FOR THE WIN OF PLAYER 1
							if(s[0][0]=='x' and s[0][1]=='x' and s[0][2]=='x') or (s[1][0]=='x' and s[1][1]=='x' and s[1][2]=='x') or (s[2][0]=='x' and s[2][1]=='x' and s[2][2]=='x') or (s[0][0]=='x' and s[1][1]=='x' and s[2][2]=='x') or (s[0][0]=='x' and s[1][0]=='x' and s[2][0]=='x') or (s[0][1]=='x' and  s[1][1]=='x' and s[2][1]=='x') or (s[0][2]=='x' and  s[1][2]=='x' and s[2][2]=='x') or (s[2][0]=='x'and s[1][1]=='x' and s[0][2]=='x') :
								b=1
								f=1
							game()
							break
			if(f==1):
				break
		#PLAYER 2 INPUT
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
					#CHECK FOR THE WIN OF PLAYER2
							if(s[0][0]== s[0][1]==s[0][2]=='o') or (s[1][0]== s[1][1]== s[1][2]=='o') or (s[2][0]== s[2][1]==s[2][2]=='o') or (s[0][0]== s[1][1]== s[2][2]=='o') or (s[0][0]== s[1][0]==s[2][0]=='o') or (s[0][1]==  s[1][1]== s[2][1]=='o') or (s[0][2]==  s[1][2]== s[2][2]=='o') or (s[2][0]== s[1][1]==s[0][2]=='o') :
								v=1
								f=1
							else:
								f=0
							break
		# CHECK FOR DRAW
		for i in range(3):
				for j in range(3):
						if(s[i][j]=='x' or s[i][j]=='o'):
							n=n+1
		if(n==8):
			f=1
			
		if(f==1):
			break

	if(b==1):
		print("player1 wins")
	elif(v==1):
		print("player2 wins")
	elif(n==8):
		print("Draw")
		


