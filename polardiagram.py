import numpy as np
import matplotlib.pyplot as plt

file = open("polar.csv")
pol = np.loadtxt(file, delimiter=";")
speed=np.zeros([38,11])

#windspeed=pol[0][2:-1]
#windspeed=[int(x/1.852) for x in windspeed]
windspeed=[int(x/1.852) for x in pol[0][2:-1]]
theta=pol[:,0]
theta=[x/180.0*3.1415 for x in theta]

for p in range(1,len(pol)):
    speed[p,:]=pol[p,1:]
    
fig = plt.figure(figsize=(12,12))   

ax = fig.add_subplot(projection='polar')              
ax.set_thetamin(1)
ax.set_thetamax(180)
ax.set_theta_direction(-1)
ax.set_theta_offset(90/180*np.pi)
ax.set_xlabel('Wind angle', size=20)
ax.xaxis.labelpad = 0
ax.yaxis.labelpad = -140
ax.set_ylabel('Boatspeed [Knots]', size=20)
ax.tick_params(axis="x", labelsize=15)
ax.tick_params(axis="y", labelsize=15)

for p in range(1,len(speed[0,1:]-1)):
    #print(p,speed[:,p])
    c = ax.plot(theta, speed[:,p], linewidth=4)
    #c = ax.scatter(theta, speed[:,p], marker="o", s=100)
    
lg=[' ']*(len(windspeed))
for p in range(len(windspeed)):
    lg[p]=str(int(windspeed[p]))

ax.legend(lg, title="Windspeed [m/s]", fontsize=20, title_fontsize=13)

fig.savefig("polar.png")
