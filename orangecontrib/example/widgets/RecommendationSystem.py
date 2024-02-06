import numpy as np


lines = open("cartoons_table/kids_cartoons.csv").readlines()
cartoons = np.array([[int(cell) for cell in row.split(';')[1:]] for row in lines[1:]])
kids = np.array([row.split(';')[0] for row in lines[1:]])

print(cartoons)
print(kids)