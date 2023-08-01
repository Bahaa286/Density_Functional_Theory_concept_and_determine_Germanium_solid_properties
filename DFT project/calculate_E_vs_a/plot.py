import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches

file = 'data.csv'
data = pd.read_csv(file)
x = data['a']
y = data['E']

fig, ax = plt.subplots()

# Plot the curve
ax.plot(x[30:], y[30:])

# Add a rectangle
rect_x = 9.2
rect_y = -631.2
rect_width = 3.6
rect_height = 1.4
rect = patches.Rectangle((rect_x, rect_y), rect_width, rect_height, facecolor='red', alpha=0.3)
ax.add_patch(rect)

# Set plot title and labels
ax.set_title(r'$E_{tot}$ vs $a$')
ax.set_xlabel('Lattice Constant $a$ ($\AA$)')
ax.set_ylabel(r'Total Energy $E_{tot}$ (Ry)')

# Show the legend
ax.legend()

# Show the plot
plt.show()


# calculate min energy a
zip_list = list(zip(y,x))
print(min(zip_list))
