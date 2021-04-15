import matplotlib.pyplot as plt

plt.ion()

plt.title("interactive test")
plt.xlabel("index")
ax = plt.gca()
ax.plot([3.1, 2.2])