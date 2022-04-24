import matplotlib.pyplot as plt
import numpy as np

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


# Vector class
class Vector:
    def __init__(self, vector: list):
        self.start_x = 0
        self.start_y = 0
        self.dx = vector[0]
        self.dy = vector[1]

    def move_vector(self, move_x, move_y):
        self.start_x += move_x
        self.start_y += move_y

    def plt_arrow(self, color, l_style='solid'):
        # plt.arrow(x, y, dx, dy)
        return plt.arrow(self.start_x, self.start_y, self.dx, self.dy,
                         length_includes_head=True,
                         head_width=.12, head_length=.15,
                         color=color,
                         linestyle=l_style
                         )

    def value(self):
        value = [self.start_x, self.start_y, self.dx, self.dy]
        return value


#
def draw_scalar_int_multiply(v: Vector, times: int, color, l_style='solid'):
    draw_v = Vector([v.dx, v.dy])
    draw_v.start_x = v.start_x
    draw_v.start_y = v.start_y

    return_legend = ''
    if times == 0:
        return return_legend
    if times > 0:
        pass
    else:
        draw_v.dx *= -1
        draw_v.dy *= -1

    for _ in range(abs(times)):
        return_legend = draw_v.plt_arrow(color, l_style)
        draw_v.start_x += draw_v.dx
        draw_v.start_y += draw_v.dy
    return return_legend


# Vector
p = [2, -1]
q = [-1, 2]
b = [0, 3]

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
plt.savefig('out/vector_02.png', dpi=500)

# Show
plt.title('vector_p + 2 * vector_p = vector_b', pad=10)
plt.show()
