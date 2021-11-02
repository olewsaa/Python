import numpy as np
import matplotlib.pyplot as plt

file = open("polar.csv")
pol = np.loadtxt(file, delimiter=";")
speed=np.zeros([38,11])

#windspeed=pol[0][2:-1]
#windspeed=[int(x/1.852) for x in windspeed]
windspeed=[int(x/1.852) for x in pol[0][2:-1]]
#print(windspeed)
theta=pol[:,0]
theta=[x/180.0*3.1415 for x in theta]

for p in range(1,len(pol)):
    speed[p,:]=pol[p,1:]
    
fig = plt.figure(figsize=(12,12))   

ax = fig.add_subplot(projection='polar')              
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_direction(1)
ax.set_theta_offset(-90/180*np.pi)

#print(speed[:,9])
for p in range(1,len(speed[0,1:]-1)):
    #print(p,speed[:,p])
    c = ax.plot(theta, speed[:,p],linewidth=3)
    c = ax.scatter(theta, speed[:,p], marker="o", s=100)
    
lg=[' ']*(len(windspeed))
for p in range(len(windspeed)):
    lg[p]=str(int(windspeed[p]))

ax.legend(lg)
fig.savefig("polar.png")
