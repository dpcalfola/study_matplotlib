import matplotlib.pyplot as plt
import numpy as np

# Import my custom class
from linear_algebra_study.classes_and_functions.vector_class import Vector, draw_scalar_int_multiply

# Const
x_min_range = -2
x_max_range = x_min_range + 6
y_min_range = -2
y_max_range = y_min_range + 6
gap = 1

# Make coordinate to square
fig, ax = plt.subplots()
ax.set_box_aspect(1)

# Range
graph_range = [x_min_range, x_max_range, y_min_range, y_max_range]
plt.axis(graph_range)

# Grid
plt.grid(color='gray', alpha=.5, linestyle="--")
plt.axhline(y=0, color='black', alpha=.3)
plt.axvline(x=0, color='black', alpha=.3)

plt.xticks(np.arange(x_min_range, x_max_range, gap))
plt.yticks(np.arange(y_min_range, y_max_range, gap))

# Vector
p = [2, -1]
q = [-1, 2]
b = [0, 3]

# Vector : imported class (vector_class.py)
vector_p = Vector(p)
vector_q = Vector(q)
vector_b = Vector(b)

legend_p = vector_p.plt_arrow('blue')
legend_q = vector_q.plt_arrow('green')
legend_b = vector_b.plt_arrow('red')

# move starting point
vector_q.move_vector(2, -1)

# vector_q * 2
legend_m = draw_scalar_int_multiply(vector_q, 2, 'darkorange', 'dotted')

# Set legend
plt.legend([legend_p, legend_q, legend_b, legend_m], [f'vector_p {p}', f'vector_q {q}', f'vector_b {b}', '2*vector_p'])

# Save Image
plt.savefig('out/vector_01.png', dpi=500)

# Show
plt.title('vector_p + 2 * vector_p = vector_b', pad=10)
plt.show()
