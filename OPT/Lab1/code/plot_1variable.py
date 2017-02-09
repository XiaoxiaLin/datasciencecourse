# Plot x^2

# This is for Linux KDE
import matplotlib
matplotlib.use('Qt5Agg')

# This is general
import matplotlib.pyplot as plt
import numpy as np

# _Function to plot
X = np.arange(-5, 5, 0.25)
Y = X**2; 

# Plot 
line, = plt.plot(X, Y)
plt.show()

