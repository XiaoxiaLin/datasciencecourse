import sys
import numpy as np

# These are the classification values 
y = np.array([-1,1,-1,1,-1]);
m = y.size;

# We normalize y
y_normalized = y / np.linalg.norm(y)

# Assume that we are at the sides of the sides of the cube of the following 
# indexes
sides = [0, 1, 4];

if (len(sides) > m):
    sys.exit("Error: len(sides) > m")

# We now apply the Gram-Schmidt algorithm to construct the projection subspace S
c_ortho = np.zeros((len(sides),m))
for i in range(len(sides)):
    c_ortho[i,sides[i]] = 1.0;
    c_ortho[i,:] = c_ortho[i,:] - np.dot(c_ortho[i,:], y_normalized) * y_normalized
    for j in range(0,i):
         c_ortho[i,:] = c_ortho[i,:] - np.dot(c_ortho[i,:], c_ortho[j,:]) * c_ortho[j,:]
    c_ortho[i,:] = c_ortho[i,:] / np.linalg.norm(c_ortho[i,:])

# Assume that this is the gradient we want to project 
g = np.array([2,2,1,3,10]);

# This is the gradient projection orthogonal to the subspace S constructed previously
g_project = g.copy();
g_project = g_project - np.dot(g, y_normalized) * y_normalized
for i in range(len(sides)):
    g_project = g_project - np.dot(g, c_ortho[i,:]) * c_ortho[i,:]
        
# Check g_project is orthogonal to the subspace S
print np.dot(g_project, y_normalized)
for i in range(len(sides)):
    print np.dot(g_project, c_ortho[i,:])
        
