import matplotlib.pyplot as plt


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
                         head_width=.08, head_length=.08,
                         color=color,
                         linestyle=l_style
                         )

    def value(self):
        value = [self.start_x, self.start_y, self.dx, self.dy]
        return value


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
