# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
import pandas as pd
data = pd.read_csv('/content/sample_data/Life expectancy Data.csv')
data.head()
data.info()
data.describe()
data.dtypes
features = list(data.columns)
print("Available features:", features)
selected_features = [features[3], features[2], features[4], features[5], features[6]]
print("Selected features: ", selected_features)
fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(data[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)
  reference_feature = selected_features[4]
y = data[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(data[f], y)
  ax.set_xlabel(f)

plt.show()
import matplotlib.pyplot as plt

reference_feature = selected_features[1]  # The reference feature
comparison_feature = selected_features[0]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(data[reference_feature], data[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

# Display the plot
plt.show()
