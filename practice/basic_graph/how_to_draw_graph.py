import matplotlib as mpl
import matplotlib.pyplot as plt

# Labeling
plt.title("my first graph")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Graph 01
# 1차원 데이터를 넣으면 y축으로 간주한다
# x축 == index
# 두 점만으로도 그래프를 그린다.
data_a = [1.5, 3.0]
plt.plot(data_a)

# Graph 02 - add another graph
data_b = [3.5, 2.5]
plt.plot(data_b)

# Show
plt.show()
