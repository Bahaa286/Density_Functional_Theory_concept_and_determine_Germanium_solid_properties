import math
import numpy as np

list = []
n = 0
with open('ge.bands', 'r') as file:
    for line in file:
        if not line.strip().startswith('&'):
            list.append(line.strip())

            n = n+1

k = []
bands = []

for i in range(len(list)):
    if(i%3==0):
        splitted_str = list[i].split()
        splitted_double = [float(element) for element in splitted_str]
        k.append(splitted_double)
    elif (i%3==1):
        bands.append(list[i])
    elif (i%3==2):
        splitted_str = (bands[len(bands)-1] + ' ' + list[i]).split()
        splitted_double = [float(element) for element in splitted_str]
        bands[len(bands)-1] = splitted_double

k_magnitude = []

for i in k:
    k_magnitude.append(math.sqrt(math.pow(i[0],2) + math.pow(i[1],2) + math.pow(i[2],2)))

bands = np.array(bands)
print(np.argmax(bands.transpose()[4]))



