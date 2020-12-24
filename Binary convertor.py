print('''           Welcome to the binary convertor
                                        •••by Harinath''')
while True:                                       
	a= input('Enter something :')
	b=''.join(format(ord(x),'b')for x in a)
	print('The equivalent binary form is',b)

	