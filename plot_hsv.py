import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


data = pd.read_csv("my_video.stats.csv")
print(data.describe())
fig, axs = plt.subplots(ncols=2)
# sns.scatterplot(x="Frame", y="delta_lum", data=data,ax=axs[1]).set_title('Delta LUM')
sns.scatterplot(x="Frame", y="delta_hue", data=data,ax=axs[0]).set_title('Delta HUE')
sns.scatterplot(x="Frame", y="delta_sat", data=data,ax=axs[1]).set_title('Delta VAL')
plt.show()
