from numpy import meshgrid
from scipy.interpolate import LinearNDInterpolator
with open("coor.txt") as file:
    for line in file:
        x, y = line.split(', ')
        print(x, y)
        X = (10, 20, 20, 10)
        Y = (10, 10, 20, 20)
        Z = (5, 2, 9, 10)
        print(list(zip(X, Y, Z)))
        arr = meshgrid(x, y)
        inter = LinearNDInterpolator(list(zip(X, Y)), Z)
        final_z = inter(float(x), float(y))
        print(final_z)