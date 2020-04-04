#%%
import seaborn as sns
import numpy as np

x = np.arange(0, 10*np.pi, 0.01)
y = np.sin(x)
y2 = np.cos(x)

ax1 = sns.lineplot(x, y2)
sns.lineplot(x = x, y = y, ax=ax1)

print("valeur min : ", np.min(y))