import matplotlib as mpl
import matplotlib.pyplot as plt

plt.ion()
print(mpl.is_interactive())

a = [1, 2, 3, 4, 5, 6, 7]
print(a)

plt.plot(a)
plt.show()


b = [1.5, 3.0]
plt.plot(b)
plt.show()