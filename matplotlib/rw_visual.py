import matplotlib.pyplot as pyplot
from random_walk import RandWalk
while True:
	rw = RandWalk()
	rw.fill_walk()
	pyplot.figure(figsize=(10,6))
	point_nums = list(range(rw.num_points))
	pyplot.scatter(rw.x_values, rw.y_values, c = point_nums, cmap=pyplot.cm.Blues, s=15)
	pyplot.scatter(0, 0, c = 'green', edgecolors='none', s=100)
	pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none',s=100)
	pyplot.show()
	keep_running = input("run again?(y/n): ")
	if keep_running == 'n':
		break
    

