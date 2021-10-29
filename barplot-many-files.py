#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt


# Set some constants and initialise some variables.
colours=["mistyrose", "skyblue", "lime", "khaki", "plum", "yellow", "brown", "black", "grey", "orange", "purple", "olive", "pink", "white", "cyan"]
hatch=["\\\\\\", "///", "...", "ooo", "xxx",  "+++"]

maxbw=0.0; minbw=100000.0; filename=[]; p=[]; clients=[]
plt.figure(figsize=(10, 6)) # Size of the figure 10x6 inches.


# Main program start :

print("NPB analyse")
files=len(sys.argv)-1 
print("Number of input files :",files)

# Main loop, scan through the input files, extract information
# print and plot the results.

for filenr in range(files):  
    filename.append(str(sys.argv[filenr+1]))
    print("input file name nr ", filenr+1, filename[filenr])
    f = open(filename[filenr], 'r')
    t=f.readlines()
    
    for line in t:
        if "cores" in line:
            ln=line.split()
            cores=int(ln[2])
    print("Cores used in file ",filename[filenr],": ",cores)
    j=0;
    b=[0,0,0,0,0,0,0,0,0];

    for line in t:    
        tests = ["bt","cg","ep","ft","is","lu","mg","sp","ua"]
        #print "NPB performance"
        #print line
        if  tests[j] in line:
            ln=line.split("=")
            b[j]=float(ln[1])
        j=j+1

# Plotting part start:

    w=0.4/files 
    ind = np.arange(9)
    p.append(plt.bar(ind+w*2*filenr, b, width=2*w, align='center', alpha=1.0, color=colours[filenr], hatch=hatch[filenr], log=1))
    plt.ylim([100,2e5])
#    plt.clip="False"
    plt.xticks(ind+w*filenr, tests)
    plt.ylabel("Performance  [Mflops/s]")
    plt.xlabel("NPB test")
    plt.suptitle("NPB performance",fontsize=18)
#   suptitle('bold figure suptitle', fontsize=14, fontweight='bold')    
    plt.title("OpenMP version using "+format(cores)+" theads")

# for filenr in range(files) End


# Finish plot, after looping through all the input files.

leg=[]     # Legend boxes from plt.bar handle
legtxt=[]  # Legend label from number of clients
for lg in range(files):
    leg.append(p[lg])
    if "log" in filename[lg]:
        fn=filename[lg].replace(".log","")
 #       print fn
    legtxt.append(fn)    
#    print lg,legtxt

#plt.legend(leg,legtxt)
plt.legend(leg,legtxt)
plt.savefig("compilers-npb.svg") 
plt.savefig("compilers-npb.png") 
plt.show()

exit(0)
