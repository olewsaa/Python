#
# Simple straight line fitting, no numpy, plot using matplotlib

import math
import matplotlib.pyplot as plt

print("Calculate the straint line y=ax+b from x and ys")
# Test data instead of reading file
#x=[1,2,3,4,5]
#y=[2,4,6,8,10]

f=open("xy.dta")
x,y = [], []
for l in f:    
#    row = l.split()
#    print(l, row)
#    x.append(float(row[0]))
#    y.append(float(row[1]))
    x.append(float(l.split()[0]))
    y.append(float(l.split()[1]))

n=len(x)
#print(len(x))
#print(x, sum(x))
#print(y, sum(y))

sum_x  = sum(x)
sum_y  = sum(y)

sum_x2=0.0; sum_y2=0.0;  sum_xy=0.0;
print("Read data n x y")
for j in range(n) :
    print(j+1,": ",x[j],y[j])
    sum_x2 = sum_x2 + x[j]*x[j] 
    sum_y2 = sum_y2 + y[j]*y[j]
    sum_xy = sum_xy + x[j]*y[j]

sxx = sum_x2 - sum_x * sum_x / n
syy = sum_y2 - sum_y * sum_y / n
sxy = sum_xy - sum_x * sum_y / n

#print(sxx, syy, sxy)


a = ((sum_x2*sum_y-sum_x*sum_xy)/len(x))/sxx
b = sxy / sxx
coef = sxy/math.sqrt(sxx*syy)

print("Intercept, slope and coef")
print(a,b, coef)

plt.plot(x,y,'bo')
plt.plot( [x[0], x[n-1]], [a+b*x[0], a+b*x[n-1]] ) # Values for line
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Simple linear regression')
plt.savefig('mkl.png')
plt.show() 


