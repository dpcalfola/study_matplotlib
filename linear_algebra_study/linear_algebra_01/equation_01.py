import matplotlib.pyplot as plt
import numpy as np

# Const
x_min_range = -3
x_max_range = 3
y_min_range = -2
y_max_range = 4
gap = 1

# Make coordinate to square
fig, ax = plt.subplots()
ax.set_box_aspect(1)

# Labeling
plt.xlabel('x axis')
plt.ylabel('y axis')

# Graph range
# [ x-min, x-max, y-min, y-max ]
graph_range = [x_min_range, x_max_range, y_min_range, y_max_range]
plt.axis(graph_range)

# Add grid
plt.grid(color='gray', alpha=.5, linestyle="--")  # 격자
plt.axvline(x=0, color='black')  # x축 진하게
plt.axhline(y=0, color='black')  # y축 진하게

# 눈금 범위와 간격
plt.xticks(np.arange(x_min_range, x_max_range, gap))
plt.yticks(np.arange(y_min_range, y_max_range, gap))

# Equation 1
x_1 = np.linspace(x_min_range, x_max_range)
y_1 = 2 * x_1
plt.plot(x_1, y_1, label='2x - y = 0')

# Equation 2
x_2 = np.linspace(x_min_range, x_max_range)
y_2 = 0.5 * (x_2 + 3)
plt.plot(x_2, y_2, label='-x + 2y = 3')

# legend
plt.legend()

# Save Image
plt.savefig('out/equation_01.png', dpi=500)

# Show
plt.show()
