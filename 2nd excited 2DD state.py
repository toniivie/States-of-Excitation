import numpy as np
from matplotlib import pyplot as plt

j = 15 #boundary/sphere/radius at which if drunkard crosses is arrested, so here has radius of 5
NOS = 100
arrested = [0]*NOS
drunkards = 100000
survived = []

for n in range(drunkards):
        position = [4,4]
        for i in range(NOS):
            probstep = np.random.uniform(0,1)
            if probstep < 0.25:
                if (position[0] + 1)**2 + (position[1])**2 >= j**2:     #moves in positive j_1 direction
                    arrested[i] += 1
                    break
                else:
                    position[0] += 1
                    if position[0] == 0:
                        arrested[i] +=1
                        break
            elif 0.25 < probstep < 0.5:
                if (position[0] - 1)**2 + (position[1])**2 >= j**2:     #moves in negative j_1 direction
                    arrested[i] += 1
                    break
                else:
                    position[0] -= 1
                    if position[0] == 0:
                        arrested[i] +=1
                        break
            elif 0.5 < probstep < 0.75:
                if (position[0])**2 + (position[1]+1)**2 >= j**2:       #moves in positive j_2 direction
                    arrested[i] += 1
                    break
                else:
                    position[1] += 1
            elif 0.75 < probstep :
                if (position[0])**2 + (position[1]-1)**2 >= j**2:      #moves in negative j_1 direction
                    arrested[i] += 1
                    break
                else:
                    position[1] -= 1
                    if position[1] == 0:
                        arrested[i] +=1
                        break

for t in range(4,len(arrested)):
    survived.append(drunkards - sum(arrested[:t]))

xval = range(4,NOS)
logs = np.log(survived)
gradient, intercept = np.polyfit(xval, logs, 1)

#print(gradient, intercept)
SLOBF = []
for x in xval:
    SLOBF.append((x*gradient)+intercept)
    
    
plt.title('Second excited state in two-dimensional system')
plt.xlabel('Number of steps')
plt.ylabel('Log(survived drunkards)')
plt.plot(xval, logs)

print(gradient*(j**2), ((5.1)**2)/4)  # prints the excitation energy value for 2d in experiment (drunkards) to true values from data base
