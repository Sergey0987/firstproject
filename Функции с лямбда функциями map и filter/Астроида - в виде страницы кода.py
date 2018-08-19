# d - расстояние между двумя точками
#x1 = 0.75
#y1 = 0
#R = 1
#t = [0;2p]
#d = sqrt((x2 - x1)**2 + (y2-y1)**2)
#x = R*cos**3 t
#y = R*sin**3 t

#1 градус = p/180 радиан
#1 радиан = 180/p радусов

from math import pi
from math import cos
from math import sin
from math import sqrt

x1 = 0.75
y1 = 0
x2 = 0
y2 = 0
R = 1
gradus = 0
gradus_max = 360
koeff_one_radian = 0.0175
t = 0
d = 0


while gradus < gradus_max:
    if gradus == 0:
         t = gradus * koeff_one_radian
         x2 = R * ((3*cos(t) + cos(3*t))/4)
         y2 = R * ((3*sin(t) - sin(3*t))/4)
         d_min = sqrt((x2-x1)**2 + (y2-y1)**2)
         gradus = gradus + 1
         print(d_min)
    else:
        t = gradus * koeff_one_radian
        x2 = R * ((3*cos(t) + cos(3*t))/4)
        y2 = R * ((3*sin(t) + sin(3*t))/4)
        d = sqrt((x2-x1)**2 + (y2-y1)**2)
        if d < d_min:
            d_min = d
        gradus = gradus + 1
        print(d_min)








            
    
