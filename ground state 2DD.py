import numpy as np
from matplotlib import pyplot as plt

j = 7 #Here j=J, the boundary condition
NOS = 100
arrested = [0]*NOS
drunkards = 1000
survived = []

for n in range(drunkards):
        position = [0,0]
        for i in range(NOS):
            probstep = np.random.uniform(0,1)
            if probstep < 0.25:
                if (position[0] + 1)**2 + (position[1])**2 >= j**2:   #moves in positive j_1 direction
                    arrested[i] += 1
                    break
                else:
                    position[0] += 1
            elif 0.25 < probstep < 0.5:
                if (position[0] - 1)**2 + (position[1])**2 >= j**2:   #moves in negative j_1 direction
                    arrested[i] += 1
                    break
                else:
                    position[0] -= 1
            elif 0.5 < probstep < 0.75:
                if (position[0])**2 + (position[1]+1)**2 >= j**2:     #moves in positive j_2 direction
                    arrested[i] += 1
                    break
                else:
                    position[1] += 1
            elif 0.75 < probstep :
                if (position[0])**2 + (position[1]-1)**2 >= j**2:     #moves in negative j_2 direction
                    arrested[i] += 1
                    break
                else:
                    position[1] -= 1


#NOS - the number of steps
#using j steps plot graph
#where j=J in thus case
#plot from J+5 to remove curveture from beginning of graph
for t in range(j+5,len(arrested)):
    survived.append(drunkards - sum(arrested[:t]))

xval = range(j+5, NOS)


logs = np.log(survived)
gradient, intercept = np.polyfit(xval, logs, 1)

SLOBF = []
for x in xval:
    SLOBF.append((x*gradient)+intercept)
#plot xval against SLOBF 
plt.title('Ground state energy in two-dimensional system')
plt.plot(xval, logs)
plt.xlabel('Number of steps')
plt.ylabel('log(survived drunkards)')

print(gradient*(j**2), ((2.4)**2)/4)

