import numpy as np
import matplotlib.pyplot as plt

########################################
#DAY 1 ASSIGNMENT
########################################

#QUESTION 1
a = np.arange(40,50)
b = np.arange(50,60)
plt.plot(a,b)
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

#QUESTION 2
days = [1,2,3,4,5,6,7] #days of week
sales_1 = [160,150,140,145,175,165,180] #sales of company1
sales_2 = [70,90,160,150,140,145,175]  #sales of company2
plt.plot(days,sales_1,label="Company 1")
plt.plot(days,sales_2,label="Company 2")
plt.xlabel("week days")
plt.ylabel("company sales")
plt.title("Line Graph")
plt.legend()
plt.plot()
plt.show()

#QUESTION 3
x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

plt.subplot(3,3,1)
plt.plot(x,y1,'r--')

plt.subplot(3,3,2)
plt.plot(x,y2,"g*--")

plt.subplot(3,3,3)
plt.plot(x,y3,"bo")

plt.subplot(3,3,4)
plt.plot(x,y4,"go")

plt.subplot(3,3,5)
plt.plot(x,y5,"g--")

plt.subplot(3,3,6)
plt.plot(x,y1,"r*--")

plt.subplot(3,3,7)
plt.plot(x,y2,"ro")

plt.subplot(3,3,8)
plt.plot(x,y3,"b--")

plt.subplot(3,3,9)
plt.plot(x,y4,"b*--")

plt.show()


