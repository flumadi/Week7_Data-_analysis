import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

def load_iris_data():
    # This loads the Iris dataset directly from the internet
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text))

def main():
    print("=== Iris Flower Analysis ===")
    
    # Load data
    iris_df = load_iris_data()
    print("\nFirst 5 flowers:")
    print(iris_df.head())
    
    # Basic analysis
    print("\nAverage measurements by species:")
    print(iris_df.groupby('species').mean())
    
    # Create visualizations
    plt.figure(figsize=(15, 10))
    
    # 1. Box plot of measurements
    plt.subplot(2, 2, 1)
    iris_df.boxplot(by='species', column=['sepal_length'])
    plt.title('Sepal Length by Species')
    
    # 2. Scatter plot
    plt.subplot(2, 2, 2)
    colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}
    for species, group in iris_df.groupby('species'):
        plt.scatter(group['sepal_length'], group['petal_length'], 
                   color=colors[species], label=species)
    plt.title('Sepal vs Petal Length')
    plt.legend()
    
    # 3. Histogram
    plt.subplot(2, 2, 3)
    iris_df['sepal_width'].hist()
    plt.title('Sepal Width Distribution')
    
    # 4. Bar chart
    plt.subplot(2, 2, 4)
    iris_df.groupby('species')['petal_width'].mean().plot(kind='bar')
    plt.title('Average Petal Width')
    
    plt.tight_layout()
    plt.savefig('iris_analysis.png')
    print("\nCharts saved as iris_analysis.png")

if __name__ == "__main__":
    main()