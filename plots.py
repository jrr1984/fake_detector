import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


data = pd.read_csv("threshold.csv")
print(data.describe())
fig, axs = plt.subplots(ncols=2)
sns.scatterplot(x="Frame", y="Delta RGB", data=data,ax=axs[0]).set_title('Delta RGB')
sns.scatterplot(x="Frame", y="Delta Frame", data=data,ax=axs[1]).set_title('Delta Frame')
plt.show()
