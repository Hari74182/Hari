
import random
print('''Welcome to stome paper scissor  game!
                                          --by Harinath ''')
a=input('Enter your name: ')
print('''            1- stone
            2-paper
            3-scissor
Guess the number from 1 to 3''')
n = random.randint(1, 3)
guess=None
while guess != n: 
	n = random.randint(1,3)
	guess = int(input('Your try '+a+': '))
	print(n)
if guess==n:
	print('You lost ',a)