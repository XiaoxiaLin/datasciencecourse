# Plot x^2+y^2

# This is for Linux KDE
import matplotlib
matplotlib.use('Qt5Agg')

# This is general
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Surface to plot
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

# Surface plot 3D + contour plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                linewidth=0, antialiased=False)
ax.contour(X,Y,Z,30,zdir='z',offset=0)

plt.show()

