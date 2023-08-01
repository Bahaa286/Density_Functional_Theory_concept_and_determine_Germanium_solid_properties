import matplotlib.pyplot as plt
from decimal import Decimal
import numpy as np

double_data = []
inner_list = []

with open('ge.bands.gnu', 'r') as file:
    for line in file:
        if line.strip() == '':
            double_data.append(inner_list)
            inner_list = []
        if(line.strip() != ''):
            inner_list.append(line.strip())

xl = []
yl = []
for list in double_data:
    x = []
    y = []
    for point in list:
        x.append(float(point.split()[0]))
        y.append(float(point.split()[1]))
    
    xl.append(x)
    yl.append(y)

plt.xlabel('momentum (k points)')
plt.ylabel('energy bands (eV)')
plt.title(r'$E_B$ vs $K$')

for i in range(20):
    plt.plot(xl[i], yl[i])

plt.hlines(8.6,0,19, colors='red', linestyles='--', label='split between valence and conducting')

plt.show()



