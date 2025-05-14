#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Pandas and Matplotlib
# 
# This notebook demonstrates data loading, exploration, analysis, and visualization using Python libraries.

# ## Task 1: Load and Explore the Dataset

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# For better looking plots in the notebook
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Enable inline plots
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Load the iris dataset from sklearn
from sklearn.datasets import load_iris

# Load the data
iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data['species'] = [iris.target_names[target] for target in iris.target]

# Display the first few rows of the dataset
print("First 5 rows of the iris dataset:")
iris_data.head()


# In[3]:


# Explore the structure of the dataset
print("Dataset shape:", iris_data.shape)
print("\nDataset information:")
iris_data.info()


# In[4]:


# Check for missing values
print("\nMissing values in each column:")
print(iris_data.isnull().sum())


# In[5]:


# Get basic statistics of the dataset
print("\nBasic statistics of numerical columns:")
iris_data.describe()


# ## Task 2: Basic Data Analysis

# In[6]:


# Compute basic statistics for each numerical column by species group
print("Summary statistics grouped by species:")
species_stats = iris_data.groupby('species').describe()
species_stats


# In[7]:


# Perform more focused analysis for each feature by species
for feature in iris.feature_names:
    print(f"\nAnalysis of {feature} by species:")
    print(iris_data.groupby('species')[feature].agg(['mean', 'median', 'std', 'min', 'max']))


# In[8]:


# Identify patterns or interesting findings
print("\nInteresting findings:")
print("1. Sepal length and width differ significantly between species")
print("2. Petal measurements show the clearest separation between species")
print("3. Setosa has the smallest petal dimensions but largest sepal width")
print("4. Virginica generally has the largest dimensions except for sepal width")

# Calculate correlation matrix to find relationships between features
correlation_matrix = iris_data.drop('species', axis=1).corr()
print("\nCorrelation matrix between features:")
correlation_matrix


# ## Task 3: Data Visualization

# In[9]:


# 1. Line chart: Average feature values by species
plt.figure(figsize=(12, 6))

# Get mean values for each feature by species
feature_means = iris_data.groupby('species').mean().T

# Create the line chart
feature_means.plot(marker='o')
plt.title('Average Feature Values by Species')
plt.xlabel('Features')
plt.ylabel('Average Value (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[10]:


# 2. Bar chart: Compare feature values across categories
plt.figure(figsize=(14, 8))

# Set up the positions for the bars
species_list = iris_data['species'].unique()
x = np.arange(len(species_list))
width = 0.2
multiplier = 0

# Create grouped bars for each feature
for feature in iris.feature_names:
    offset = width * multiplier
    feature_means = iris_data.groupby('species')[feature].mean()
    plt.bar(x + offset, feature_means, width, label=feature)
    multiplier += 1

# Add labels and legend
plt.xlabel('Species')
plt.ylabel('Average Value (cm)')
plt.title('Comparison of Feature Averages Across Species')
plt.xticks(x + width, species_list)
plt.legend(loc='best')
plt.tight_layout()
plt.show()


# In[11]:


# 3. Histogram: Distribution of sepal length
plt.figure(figsize=(12, 8))

# Create separate histograms for each species
for species in species_list:
    plt.hist(iris_data[iris_data['species'] == species]['sepal length (cm)'], 
             bins=10, alpha=0.5, label=species)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length by Species')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[12]:


# 4. Scatter plot: Relationship between sepal length and sepal width
plt.figure(figsize=(10, 8))

# Create scatter plot with different colors for each species
for species in species_list:
    subset = iris_data[iris_data['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], 
                label=species, alpha=0.7, s=70)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Relationship Between Sepal Length and Sepal Width')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[13]:


# Additional visualization: Pairplot to show relationships between all features
sns.pairplot(iris_data, hue='species', height=2.5, markers=['o', 's', 'D'])
plt.suptitle('Pairwise Relationships Between Features', y=1.02)
plt.tight_layout()
plt.show()


# In[14]:


# Heatmap of correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', vmin=-1, vmax=1, 
            square=True, linewidths=0.5)
plt.title('Correlation Matrix of Iris Features')
plt.tight_layout()
plt.show()


# ## Summary of Findings
# 
# 1. **Dataset Characteristics**:
#    - 150 samples with 4 features (sepal length, sepal width, petal length, petal width)
#    - 3 different species of iris: setosa, versicolor, and virginica
#    - No missing values in the dataset
# 
# 2. **Statistical Analysis**:
#    - Setosa has the smallest petal dimensions but widest sepals
#    - Virginica generally has the largest dimensions overall
#    - Petal measurements show more variation between species than sepal measurements
# 
# 3. **Correlations and Relationships**:
#    - Strong positive correlation (0.96) between petal length and petal width
#    - Moderate negative correlation (-0.11) between sepal length and sepal width
#    - Petal dimensions are better predictors of species than sepal dimensions
# 
# 4. **Visual Observations**:
#    - Setosa is clearly distinguishable from the other two species
#    - Versicolor and virginica show some overlap in measurements
#    - The three species form distinct clusters in the feature space
# 
# This analysis demonstrates how exploratory data analysis combined with visualizations can reveal patterns and relationships in the data that might not be immediately obvious from the raw numbers.
