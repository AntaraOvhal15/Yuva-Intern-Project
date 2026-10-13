# Logistics Delivery Performance Analysis and Route Optimization Using Python

## Project Overview

This project analyzes logistics delivery performance using Python and the DataCo Supply Chain Dataset. It focuses on understanding delivery delays, identifying high-risk delivery groups, predicting shipping duration, and evaluating route optimization techniques.

The project combines data cleaning, exploratory data analysis, machine learning, clustering, and route evaluation to generate insights that can support data-driven logistics decisions.

## Project Objectives

* Analyze on-time and late delivery performance.
* Identify shipping delays and high-risk delivery groups.
* Explore delivery performance across shipping modes and other business factors.
* Build a Random Forest regression model to predict actual shipping duration.
* Apply K-Means clustering to identify delivery risk patterns.
* Compare route optimization approaches and evaluate distance reduction.

## Dataset

This project uses the **DataCo Smart Supply Chain for Big Data Analysis** dataset.

* **Dataset Source:** [Kaggle – DataCo Smart Supply Chain for Big Data Analysis](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
* **Original File:** `DataCoSupplyChainDataset.csv`
* **Total Records:** 180,519
* **Original Columns:** 53

The dataset contains order details, customer information, product sales, shipping methods, delivery status, and profitability information.

## Technologies Used

* **Python** – data analysis and machine learning
* **Pandas** – data cleaning and manipulation
* **NumPy** – numerical calculations
* **Matplotlib** – data visualization
* **Seaborn** – statistical visualization
* **Scikit-learn** – regression modeling and clustering
* **Git and GitHub** – version control and project hosting

## Project Workflow

### Week 1: Strategic Planning and Data Exploration

* Defined the project objectives and key performance indicators.
* Explored the dataset structure, columns, and business information.
* Planned the data analysis and modeling workflow.

### Week 2: Data Cleaning and Preprocessing

* Checked data quality and duplicate records.
* Validated important numerical fields.
* Examined outliers and prepared the dataset for analysis.
* Saved the cleaned dataset for subsequent analysis.

### Week 3: Exploratory Data Analysis and Visualization

* Analyzed sales and delivery status distributions.
* Compared actual and scheduled shipping durations.
* Evaluated delivery performance across shipping modes and markets.
* Examined correlations and other business patterns using charts.

### Week 4: Predictive Modeling and Optimization

* Built a Random Forest regression model to predict actual shipping duration.
* Applied K-Means clustering to identify groups with different delivery risk patterns.
* Analyzed late-delivery risk across the resulting clusters.
* Compared baseline, Nearest Neighbor, and optimized routes.

## Key Findings

### Delivery Performance

* **On-Time Delivery Rate:** 45.17%
* **Late Delivery Rate:** 54.83%
* **Average Actual Shipping Duration:** 3.50 days
* **Average Shipping Delay:** 0.57 days

The results indicate that late deliveries are a significant challenge in the analyzed dataset.

### Random Forest Regression

A Random Forest Regressor was developed to predict actual shipping duration.

* **Mean Absolute Error (MAE):** 0.989 days
* **Root Mean Squared Error (RMSE):** 1.269 days
* **R² Score:** 0.389

These results describe the model's performance on the evaluated test data. The R² score indicates that there is room to improve its predictive performance.

### K-Means Clustering

K-Means clustering was used to group orders according to selected delivery and order characteristics.

* **Number of Clusters:** 3
* **Highest-Risk Cluster:** Cluster 1
* **Late-Delivery Risk in Highest-Risk Cluster:** 72.71%
* **Orders in Highest-Risk Cluster:** 47,867

Cluster 1 showed the highest late-delivery risk among the three identified groups.

### Route Optimization

Three approaches were compared using the evaluated sample route:

* **Baseline Route Distance:** 28.27 km
* **Nearest Neighbor Route Distance:** 26.47 km
* **Optimized Route Distance:** 24.73 km
* **Distance Reduction:** Approximately 12.52% compared with the baseline route

The result demonstrates a reduction in distance for the evaluated route. It does not represent a measured reduction across the entire supply chain.

## Repository Contents

The repository includes:

* Python scripts for data cleaning, analysis, regression, clustering, and route optimization.
* Weekly project reports.
* Visualization images and analysis charts.
* `requirements.txt` for Python dependencies.
* `.gitignore` for excluding unnecessary files.

Large dataset files and generated intermediate CSV files are excluded from the repository.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/AntaraOvhal15/Yuva-Intern-Project.git
cd Yuva-Intern-Project
```

### 2. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) and place the original CSV file in the project folder.

### 4. Run the Scripts

Run the data cleaning script first, followed by the analysis, regression, clustering, and route optimization scripts as required by their input dependencies.

**Note:** Some scripts require intermediate CSV files generated by earlier scripts. Check the input file names in each script before running it.

## Conclusion

This project demonstrates the application of Python, exploratory data analysis, and machine learning to logistics delivery performance. It identifies delivery risk patterns, evaluates shipping-duration predictions, and compares route optimization methods to explore potential improvements in logistics operations.

The project provided practical experience in data preprocessing, visualization, regression modeling, clustering, and analytical problem-solving.

## Author

**Antara Ovhal**

GitHub: [AntaraOvhal15](https://github.com/AntaraOvhal15)

