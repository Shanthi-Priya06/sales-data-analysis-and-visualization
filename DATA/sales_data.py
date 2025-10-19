import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("sales_data.xlsx")
data.columns=data.columns.str.strip()

print(data.head())

sns.lineplot(x="Month",y="Sales",hue="Product",data=data,marker="o")
plt.title("Mothly sales by product")
plt.show()

sns.barplot(x="Product",y="Profit",data=data,estimator=sum)
plt.title("Total profit by product")
plt.show()

sns.heatmap(data.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

