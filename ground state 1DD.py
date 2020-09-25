import numpy as np
from matplotlib import pyplot as plt

j = 8 #Here j=J, the boundary condition
NOS = 100
drunkards = 1000
arrested = [0]*NOS
survived = []

for n in range(drunkards):
        position = [0] 
        for i in range(NOS):
            probstep = np.random.uniform(0,1)
            if probstep < 0.5:
                if position[0] + 1 == j: #moves in positive j direction
                    arrested[i] +=1
                    break
                else:
                    position[0] += 1
            elif 0.5 < probstep:
                if position[0] - 1 == -j:#moves in negative j direction
                    arrested[i] +=1
                    break
                else:
                    position[0] -= 1

#need to plot from 0 steps
#xval = range(NOS)
#NOS is the number of steps
#using j steps plot graph
for t in range(j,len(arrested)):
    survived.append(drunkards - sum(arrested[:t]))
    
xval = range(j,NOS)


logs = np.log(survived)
gradient, intercept = np.polyfit(xval, logs, 1)
SLOBF = [] #empty array for line of best fit
for x in xval:
    SLOBF.append((x*gradient)+intercept)
#plot xval against SLOBF 
plt.title('Ground state energy in one-dimension')
plt.plot(xval, logs)
plt.xlabel('Number of steps')
plt.ylabel('Log(survived drunkards)')
#plt.show()

print(gradient*(j**2), (np.pi**2)/8)