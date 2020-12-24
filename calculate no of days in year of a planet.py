from math import pi
r= float(input('enter ther radius'))
v=float(input('entre the speed of rotation'))
r=r*1000000
year= 2*pi*r/v
year=year/(60*60*24)
print('no. of days=',year)