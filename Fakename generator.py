from faker import Faker

print('''            Welcome to the fake name generator
                                         •••by Harinath   ''')
try:
	def fakename():
		a=int(input('''Enter the native country
		                    1-Australia
		                    2-Bulgarian
		                    3-Bosnian
		                    4-Czech
		                    5-German
		                    6-Danish
		                    7-Greek
		                    8-Canada
		                    9-Great Britain
		                    10-Hindi
		                    11-New Zealand
		                    12-United States
		                    13-Spain
		                    14-Russian
		                    15-Japanese
		                    16-Chinese	
	'''))
		 
		if a==1:
			fake=Faker("en_AU")
			a=fake.name()
			print(a)
			
		elif a==2:
			fake=Faker("bg_BG")
			a=fake.name()
			print(a)
			
		elif a==3:
			fake=Faker("bs_BA")
			a=fake.name()
			print(a)
			
		elif a==4:
			fake=Faker("cs_CZ")
			a=fake.name()
			print(a)
		
		elif a==5:
			fake=Faker("de_DE")
			a=fake.name()
			print(a)
		
		
		elif a==6:
			fake=Faker("dk_DK")
			a=fake.name()
			print(a)
			
		
		elif a==7:
			fake=Faker("el_GR")
			a=fake.name()
			print(a)
		
		
		elif a==8:
			fake=Faker("en_CA")
			a=fake.name()
			print(a)
		
		
		elif a==9:
			fake=Faker("en_GB")
			a=fake.name()
			print(a)
			
		
		elif a==10:
			fake=Faker('hi_IN')
			a=fake.name()
			print(a)
			
		
		elif a==11:
			fake=Faker("en_NZ")
			a=fake.name()
			print(a)
			
		
		elif a==12:
			fake=Faker("en_US")
			a=fake.name()
			print(a)
			
		
		elif a==13:
			fake=Faker("es_ES")
			a=fake.name()
			print(a)
		
		
		elif a==14:
			fake=Faker("ru_RU")
			a=fake.name()
			print(a)
			
		
		elif a==15:
			fake=Faker("ja_JP")
			a=fake.name()
			print(a)
			
		elif a==16:
			fake=Faker("zh_CN")
			a=fake.name()
			print(a)
			
		else:
			print('Enter correct option :')
			fakename()
		
except ValueError:
	print("Enter a number from 1 to 16")
fakename()