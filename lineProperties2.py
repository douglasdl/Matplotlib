import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4]
y1 = [0, 1, 2, 3]

x2 = [5, 6, 7, 8]
y2 = [3, 9, 8, 7]

lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
#plt.setp(lines, 'color', 'r', 'linewidth', 2.0)