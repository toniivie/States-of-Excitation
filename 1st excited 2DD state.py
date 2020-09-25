import numpy as np
from matplotlib import pyplot as plt

j = 11 #boundary/sphere/radius at which if drunkard crosses is arrested, so here has radius of 5
NOS = 100  #THE NUMBER OF STEPS TAKEN
arrested = [0]*NOS
drunkards = 10000
survived = []

for n in range(drunkards):
        position = [3,3]
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
                if (position[0])**2 + (position[1]-1)**2 >= j**2:        #moves in negative j_2 direction
                    arrested[i] += 1
                    break
                else:
                    position[1] -= 1

#plot from 0 steps get straight horizontal line at beginning
#so end up plotting from 3rd step below:
for t in range(3,len(arrested)):
    survived.append(drunkards - sum(arrested[:t]))

xvalues = range(3,NOS)
logs = np.log(survived)
gradient, intercept = np.polyfit(xvalues, logs, 1)

SLOBF = []
for x in xvalues:
    SLOBF.append((x*gradient)+intercept)
    
#plot xval against SLOBF , where SLOBF = is the line of best fit
    
plt.title('First excited state in two-dimensional system')
plt.xlabel('Number of steps')
plt.ylabel('Log(survived drunkards)')
plt.plot(xvalues, logs)

print(gradient*(j**2), ((3.8)**2)/4)  # prints the excitation energy value for 2d in experiment (drunkards) to true values from data base
#probstep -  the probability of steps taken by drukard