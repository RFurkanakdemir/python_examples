"""daire alanı ve çevresi"""
from cmath import pi


r=input('yarıçap giriniz:  ')
r=int(r)
alan=pi*r**2
cevre=2*pi*r
print("alan=",alan)
print("\ncevre= ",cevre)