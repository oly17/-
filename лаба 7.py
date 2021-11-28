from numpy import *
import matplotlib.pyplot as plt
x=linspace(0,10,100)
y=x^cos(x^2)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()