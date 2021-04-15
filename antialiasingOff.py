import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialiasing