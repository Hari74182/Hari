import numpy as np
matrix=None
def mat():
	R=int(input('Enter no. of rows: '))
	C=int(input('Enter no. of columns:'))
	print("Enter the entries in a single line (separated by space): ")
	entries=list(map(int,input().split()))
	matrix=np.array(entries).reshape(R,C)
	print(matrix)
mat()
matrix global
print(matrix.T)