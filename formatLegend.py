import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
x = np.arange(0, 5, 0.2)

# red dashes, blue squares and green triangles
#plt.plot(x, x, 'r--', label='Linear', x, x**2, 'bs', label='Squared', x, x**3, 'g^', label='Cubic')
plt.plot(x, x, 'r--', label='Linear')
plt.plot(x, x**2, 'bs', label='Squared')
plt.plot(x, x**3, 'g^', label='Cubic')


# Create the legend (location , background color, transparency, border)
legend = plt.legend(loc='best', facecolor='white', framealpha=0.5, edgecolor="black");

# Change Legend text color
for text in legend.get_texts():
    text.set_color("black") 

plt.show()