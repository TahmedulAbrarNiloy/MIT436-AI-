import matplotlib.pyplot as plt
year = list(range(1951, 2011))  # Years from 1951 to 2010
populations = [
    2.56, 2.61, 2.66, 2.71, 2.76, 2.81, 2.86, 2.92, 2.98, 3.04, 
    3.10, 3.17, 3.24, 3.31, 3.38, 3.45, 3.52, 3.60, 3.68, 3.76, 
    3.85, 3.94, 4.03, 4.12, 4.22, 4.32, 4.42, 4.52, 4.63, 4.74, 
    4.85, 4.96, 5.08, 5.20, 5.32, 5.44, 5.56, 5.69, 5.82, 5.95, 
    6.08, 6.21, 6.34, 6.47, 6.60, 6.73, 6.86, 6.99, 7.12, 7.25, 
    7.38, 7.51, 7.64, 7.77, 7.90, 8.03, 8.16, 8.29, 8.42, 8.55
]

year= [1800,1850,1950] + year
populations=[1.0,1.262,1.65]+populations

plt.plot(year,populations)
plt.xlabel('Year')
plt.ylabel('Populations')
plt.title('World population projection from 1950 to 2010')

#ytricks function is used to start the y scale from a perticular position
# The second part is naming the scales. We call them labels
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])

plt.show()

