# Week7_Data_analysis
# Iris Dataset Analysis with Pandas and Matplotlib

## Project Description
This project demonstrates fundamental data analysis and visualization techniques using Python's Pandas and Matplotlib libraries.  
The analysis is performed on the classic Iris dataset, which contains measurements of iris flowers from three different species.  

## Features
- **Data Loading & Exploration**: Loads the Iris dataset and examines its structure  
- **Data Cleaning**: Checks for and handles missing values  
- **Statistical Analysis**: Computes descriptive statistics and group comparisons  
- **Data Visualization**: Creates four different types of plots to reveal patterns  

## Requirements  
- Python 3.6+  
- Required packages:  
  - pandas  
  - matplotlib  
  - scikit-learn (for dataset loading)  

Install requirements with:  
pip install pandas matplotlib scikit-learn  
File Structure  
iris_analysis/  
├── iris_data_analysis.py  # Main analysis script  
├── iris_analysis.png      # Generated visualization  
└── README.md              # This file  
How to Run  
Clone/download the repository  

Run the analysis script:  
python iris_data_analysis.py  
## Analysis Output  
-The script produces:  
Console output showing:  
✅First 5 rows of data  
✅Dataset structure information  
✅Missing value counts  
✅Statistical summaries  
✅Interesting findings  

## 📚Visualization file (iris_analysis.png) containing:  
-Line chart of sepal length  
-Bar chart of average sepal length by species  
-Histogram of sepal width distribution  
-Scatter plot of sepal vs petal length  

* Key Findings  
Species Differences:  
Setosa has significantly smaller petals than other species  
Versicolor and virginica can be distinguished by petal width  

* Measurement Patterns:  
Sepal width shows the least variation across species  
Strong correlation between petal length and sepal length  

* Customization  
To analyze a different dataset:  
Replace the dataset loading code in iris_data_analysis.py  
Update column names in the analysis and visualization sections  
Modify plot titles and labels accordingly  
Enjoy analyzing the Iris dataset! 🌸📊  
