from tkinter.ttk import LabeledScale
import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36,49,64]

fig, ax=plt.subplots()

ax.plot(squares, linewidth=3) # The linewidth parameter controls the thickness of the line that plot() generates.

ax.set_title("Squre Numbers", fontsize=24) # sets a title for the chart.
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Squre of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14) #  styles the tick marks, The arguments shown here affect the tick marks on both the x- and y-axes (axis='both') and set the font size of the tick mark labels to 14 (labelsize=14).
plt.show()
