# Plot the function Gerard draws in lecture 1

# This is for python notebook. Uncomment if you are using notebook
# %matplotlib inline

# This is for Linux KDE. Comment if you are not using it.
import matplotlib
matplotlib.use('Qt5Agg')

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Function to analyze

X = np.arange(-2, 2, 0.05)
Y = np.arange(-2, 2, 0.05)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2 

# Contour plot en 2D

plt.figure()
plt.contour(X, Y, Z, 50)

# Compute gradient 

X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
gradx = 2 * X
grady = 2 * Y 

plt.streamplot(X, Y, gradx, grady)

plt.show()
