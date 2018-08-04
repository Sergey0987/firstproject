#Вывести длинны полуосей эллипса орбиты самой далекой планеты - кортеж

def findFarthestOrbit(listOfOrbits):
    from functools import reduce
    from math import pi

    listOfSquareOrbits = list(map(lambda kortez_axis: reduce(lambda semiminorAxis, majorSemiaxis: semiminorAxis * majorSemiaxis * pi, kortez_axis), listOfOrbits))

#    print(listOfSquareOrbits)
    
    max_orbita = reduce(lambda x,y: max(x,y), listOfSquareOrbits)

    find_axis_max_orbit = tuple(filter(lambda kortez_axis: reduce(lambda semiminorAxis, majorSemiaxis: semiminorAxis * majorSemiaxis * pi, kortez_axis) == max_orbita, listOfOrbits))

    find_axis_max_orbit = tuple(list(find_axis_max_orbit)[0])

    return find_axis_max_orbit

print(findFarthestOrbit([(4,1),(17,1),(7,13),(11,10)]))
