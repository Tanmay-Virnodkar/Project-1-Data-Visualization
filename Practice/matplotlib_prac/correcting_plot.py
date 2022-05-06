import matplotlib.pyplot as plt

x_vals = [1,2,3,4,5,6,7,8]
y_vals = [1,4,9,16,25,36,49,64]

fig, ax = plt.subplots()

ax.plot(x_vals, y_vals, linewidth = 3)

ax.set_title('Square Number Data', fontsize = 15)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

ax.tick_params('both', labelsize = 14)

plt.show()