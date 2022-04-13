import matplotlib.pyplot as plt
import numpy as np

# Labeling
plt.xlabel('x axis')
plt.ylabel('y axis')

# Const
min_range = -2
max_range = 2
gap = 0.5

# Add grid
plt.grid(color='gray', alpha=.5, linestyle="--")  # 격자
plt.axvline(x=0, color='black')  # x축 진하게
plt.axhline(y=0, color='black')
plt.xticks(np.arange(min_range, max_range, gap))

# Equation 1
x_1 = np.linspace(min_range, max_range)
y_1 = -2 * x_1 + 3
plt.plot(x_1, y_1, label='2x + y = 3')

# Equation 2
x_2 = np.linspace(min_range, max_range)
y_2 = 0.5 * (x_2 + 1)
plt.plot(x_2, y_2, label='x - 2y = -1')

# Show legend
plt.legend()

# Save Image
plt.savefig('graph_out/graph_01.png', dpi=300)

# Show graph
plt.show()

