def greet(name):
	print ("Hello! "+name)
x=input(" Enter your name:")
greet(x)
def main():
	print('''              Welcome to simple conventer
		                            --by Harinath
		        Enter required option
		               1.Length
		               2.Weight
		               3.Area
		               4.Volume
		               5.exit''')
	a=int(input("Enter required option "+x+":"))
	if a==1:
	 	print('''Enter the required option
	 	          1.metre to inch
	 	          2.inch to metre
	 	          3.foot to metre
	 	          4.metre to foot
	 	          5.Back''')
	 	len=int(input('Enter your option '+x))
	 	if len==1:
	 		mi=float(input("Entre value in metre:"))
	 		c=(mi)*39.37007
	 		print('The equivalent value in inch are',c)
	 	elif len==2:
	 		im=float(input('Enter value in inches:'))
	 		d=(im)*0.0254
	 		print('The equivalent value in metre is',d)
	 	elif len==3:
	 		fm=float(input('Enter value in foot:'))
	 		e=(fm)*0.304
	 		print('The equivalent value in metre is',e)
	 	elif len==4:
	 		mf=float(input('Enter value in metre:'))
	 		f=(mf)*3.2808399
	 		print('The equivalent value in foot is',f)
	 	elif len==5:
	 		main()
	 	else:
	 		print('Enter correct option '+x)
	 		main()
	if a==2:
		print('''Entre the required option
		            1.Pounds to grams
		            2.Grams to Pounds
		            3.Ounces to grams
		            4.Grams to Ounces
		            5.Back''')
		g=int(input('Enter your option '+x+':'))
		if g==1:
			pg=float(input('Enter value in pounds:'))
			h=(pg)*453.59237
			print('The equivalent value in gram is',h)
		elif g==2:
			gp=float(input('Enter value in grams:'))
			i=(gp)*0.002204623
			print('The equivalent value in pound is',i)
		elif g==3:
			og=float(input('Enter value in ounce:'))
			j=(og)*28.34952
			print('The equivalent value in gram is',j)
		elif g==4:
			go=float(input('Enter value in grams:'))
			k=(go)*0.035273966
			print('The equivalent value in ounce is',k)
		elif g==5:
			main()
		else:
			print('Enter correct option '+x)
			main()
	if a==3:
		print('''Enter  the required option
		           1.m² to acres
		           2.Acres to m²
		           3.m² to hectare
		           4.Hectare to m²
		           5.Back''') 
		l=int(input('Enter required optionoption '+x+':'))
		if l==1:
		   ma=float(input('Enter value in m²:'))
		   m=(ma)*(0.000247)
		   print('The equivalent value in acres are', m)
		elif l==2:
			am=float(input('Entre value in acre:'))
			n=(am)*4046.873
			print('The equivalent value in m² is',n)
		elif l==3:
		       mh=float(input('Enter value in m²:'))
		       o=(mh)*0.0001
		       print('The equivalent value in hectare is',o)
		elif l==4:
		       hm=float(input('Enter value in hectare:'))
		       p=(hm)*1000
		       print("The equivalent value in m² is",p)
		elif l==5:
			main()
		else:
			print('Enter correct option ' ,+x)
			main()
	if a==4:
		print('''Enter  the required option
		           1.m³ to gallons
		           2.m³ to litres
		           3.litres to m³
		           4.gallons to m³
		           5.Back''') 
		vol=int(input('Enter required optionoption '+x+':'))
		if vol==1:
		   mg=float(input('Enter value in m³:'))
		   q=(mg)*219.969
		   print('The equivalent value in gallon are', q)
		elif vol==2:
			ml=float(input('Entre value in m³:'))
			r=(ml)*1000
			print('The equivalent value in litre is',r)
		elif vol==3:
		       lm=float(input('Enter value in litre:'))
		       s=(lm)*0.001
		       print('The equivalent value in m³  is',s)
		elif vol==4:
		       gm=float(input('Enter value in gallon:'))
		       t=(gm)*0.00454609
		       print("The equivalent value in m³ is",t)
		elif vol==5:
			main()
		else:
			print('Enter correct option '+x)
			main()
	elif a==5:
		print("Thank You")
	else:
		print("Enter correct option")
		main()
main()