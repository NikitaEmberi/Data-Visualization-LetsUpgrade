import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#RELPLOT
df = sns.load_dataset('fmri')
sns.relplot(x='timepoint', y='signal',data = df,hue='region',style='event')
plt.show()

#LINE PLOT
sns.relplot(x='timepoint', y='signal',data = df,kind='line',hue='region',style='event')
plt.show()

#BOX PLOT
sns.catplot(x='subject',y='timepoint',data=df,hue='region',kind='box')
plt.show()



