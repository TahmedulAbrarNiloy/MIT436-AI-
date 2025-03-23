import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
population =[2.519, 3.692,5.263,6.972]
#plt.plot(year,population)
# Scattter function does not draw a line just puts the dots in places
plt.scatter(year,population)
plt.show()

#Exercise 1
# Print the last item from year and population. We can use negative index to access the last element in a 
# list in the python
print(year[-1])
print(population[-1])
# Put the x-axis on a logarithmic scale
#plt.xscale('log')
# Show plot
#plt.show()