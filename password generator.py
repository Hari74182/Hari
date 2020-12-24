import random

print('''      Welcome to the random password generator 
                                       •••by Harinath''')
                                       
def get_char(char_list,number):
 	temp_list=[]
 	for i in range (number):
 		temp_list.append(random.choice(char_list))
 		return temp_list
while True:
	total_num=int(input("Enter total no.of letters you want:"))
	upper_num=int(input("Enter no.of uppecase letters you want:"))
	lower_num=int(input("Enter no.of lower case letters you want:"))
	digit_num=int(input("Enter no. of numeric characters you want:"))
	symbol_num=int(input("Enter no. of symbol you want:"))
	
	if total_num<upper_num+lower_num+digit_num+symbol_num:
		print("Given inputs are not correct. Please try again:")
	else:
		break
	
upper_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"," T","U","V","W","X","Y","Z"]
upper_char=list(get_char(upper_list,upper_num))

lower_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lower_char=list(get_char(lower_list,lower_num))

digit_list=["1","2","3","4","5","6","7","8","9"]
digit_char=list(get_char(digit_list,digit_num))

symbol_list=["@","#","₹","&","_","*","?","+","!","%","$","^"]
symbol_char=list(get_char(symbol_list,symbol_num))

unfilled_char_num=total_num-upper_num-lower_num - symbol_num - digit_num 

whole_list=upper_list+lower_list+digit_list+symbol_list
remaining_char=list(get_char(whole_list,unfilled_char_num))

password=upper_char+lower_char +digit_char+ symbol_char +remaining_char

random.shuffle(password)
password="".join(password)
print(password)