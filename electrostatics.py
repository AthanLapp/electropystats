# Import pylab inline
from pylab import *
seterr(all='ignore') # ignore all floating point errors

N = 101 # Number of points in x-coordinate and y-coordinate each
a, b = linspace(-5, 5, N), linspace(-5, 5, N) # Set evenly spaced points within the interval -5 and 5
xa, ya = meshgrid(a, b)     # A meshgrid in the xy plane. xa contains the x-coordinates
Ex = zeros_like(xa)         # 2D array to store the Ex and
Ey = zeros_like(ya)         # Ey components

Q = [(109, 1, 0), (-10, -1, 0), (1, 0, 1)]  # Charges (Value, x-cord, y-cord)

for q in Q:  # mark charge locations
    if q[0]>0:
    	text(q[1], q[2], 'o', color = 'r', fontsize=(math.log(1.1+abs(q[0]), 1.1)), va='center', ha='center')
    else:
    	text(q[1], q[2], 'o', color = 'c', fontsize=(math.log(1.1+abs(q[0]), 1.1)), va='center', ha='center')
		
for i in range(N):      # calculate Ex and Ey at each point in the grid, due to all charges
    for j in range(N):
        x, y = xa[i,j], ya[i,j]
        for k in range(len(Q)): # sum over the charges
            
            Ex[i,j] += Q[k][0]*(x-Q[k][1])/ ((x-Q[k][1])**2+(y-Q[k][2])**2)**(1.5)
            Ey[i,j] += Q[k][0]*(y-Q[k][2])/ ((x-Q[k][1])**2+(y-Q[k][2])**2)**(1.5)

sumQ = 0
for k in range(len(Q)): # sum over the charges 
    sumQ += abs(Q[k][0])

sumQ = math.log(3+sumQ/2, 3)-0.82
streamplot(xa, ya, Ex, Ey, color='b', density=sumQ ) #plot the field lines using streamplot
show() # show the plot