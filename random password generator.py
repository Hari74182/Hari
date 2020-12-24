import random
def pas():
	upper_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"," T","U","V","W","X","Y","Z"]
	upper_char=random.choice(upper_list)
	
	lower_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	lower_char=random.choice(lower_list)
	
	digit_list=["1","2","3","4","5","6","7","8","9"]
	digit_char=random.choice(digit_list)
	
	symbol_list=["@","#","₹","&","_","*","?","+","!","%","$","^"]
	symbol_char=random.choice(symbol_list)
	
	password=(upper_char+ lower_char+ digit_char+symbol_char)
	
	password=password+(upper_char+ lower_char+ digit_char+symbol_char)
	print(password)
	
print('''Welcome to the random password generator
                                   •••By Harinath '''  )
print('''The minimum requirements for a strong password are 
                    •8 Digits
                    •1 Uppercase
                    •1 Lowercase
                    •1 Number
                    •1 symbol   ''')
print("The random password generated is")
pas()