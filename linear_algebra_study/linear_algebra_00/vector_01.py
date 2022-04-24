import matplotlib.pyplot as plt
import numpy as np

# Const
x_min_range = -2
x_max_range = 4
y_min_range = -2
y_max_range = 4
gap = 0.5

# Range
graph_range = [x_min_range, x_max_range, y_min_range, y_max_range]
plt.axis(graph_range)

# Grid
plt.grid(color='gray', alpha=.5, linestyle="--")
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

plt.xticks(np.arange(x_min_range, x_max_range, gap))
plt.yticks(np.arange(y_min_range, y_max_range, gap))

#
# Vector
a = [2, -1]
b = [-1, 2]

# Draw vector
plt.arrow(0, 0, a[0], a[1], head_width=.15, head_length=.15, color='blue')
plt.arrow(0, 0, b[0], b[1], head_width=.15, head_length=.15, color='red')


# Show
plt.show()
