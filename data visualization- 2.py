import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn

#QUESTION 1
df = pd.DataFrame(randn(10,4), columns=['a','b','c','d'])
df.plot.bar()
plt.title("Bar Graph")
plt.xlabel("X-axis (rows)")
plt.ylabel("Y-axis (columns)")
plt.show()
