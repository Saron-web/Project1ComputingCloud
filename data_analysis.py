import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("All_Diets.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

avg_protein = df['Protein(g)'].mean()
avg_carbs = df['Carbs(g)'].mean()
avg_fat = df['Fat(g)'].mean()

print("Average Protein:", avg_protein)
print("Average Carbs:", avg_carbs)
print("Average Fat:", avg_fat)

top_protein = df.nlargest(10, 'Protein(g)')
print(top_protein[['Recipe_name', 'Protein(g)']])

df['Protein_Fat_Ratio'] = df['Protein(g)'] / df['Fat(g)']

plt.figure(figsize=(10,5))
sns.barplot(data=top_protein, x='Recipe_name', y='Protein(g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")

plt.figure(figsize=(8,6))
sns.heatmap(df[['Protein(g)', 'Carbs(g)', 'Fat(g)']].corr(), annot=True)
plt.savefig("heatmap.png")

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Carbs(g)', y='Protein(g)', hue='Diet_type')
plt.savefig("scatter_plot.png")
