import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# subplots() can generate one or more plots in the same figure.
# The variable fig represents the entire figure or collection of plots that are generated.
# The variable ax represents a single plot in the figure and is the variable we’ll use most of the time.

ax.plot(squares)

plt.show()