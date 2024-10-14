import numpy as np 
import matplotlib.pyplot as plt


N = 500000                                                                                           # Number of points for the simulation = total amount of points
points_in = 0                                                                                        # Counter for the points
radius = 1                                                                                           # Radius of the quarter of the cirle 
points_coord = np.random.rand(2,N)                                                                   # Random coordanates for the points in the or out the circle.

for i in range (0,N):                                                                                # Loop going through the random coordanates and caculating if they are in the quarter of the circles.
    if points_coord[0,i]**2+points_coord[1,i]**2 < radius**2:
        points_in +=1

continues = np.linspace(0,np.pi/2,N)                                                                 # Space for plooting the quarter of the circle
pi_aprox = 4*points_in/N                                                                             # SAving the approximation of pi.

x=np.cos(continues)                                                                                  # coordonate x,y for the quarter circle   
y=np.sin(continues)
print("The aprox value of pi = ", pi_aprox)


fig,ax= plt.subplots()                                                                                # Plooting part.
ax.scatter(points_coord[0,:],points_coord[1,:], s=1)
ax.plot(x,y,c= "red")


plt.show()