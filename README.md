Credit Risk Analytics & Natural Gas Contract Valuation

JPMorgan Chase Quantitative Research Virtual Experience (Forage)

Project Overview

This repository contains my solutions to the JPMorgan Chase Quantitative Research Virtual Experience offered through Forage. The project applies quantitative finance, machine learning, and optimization techniques to solve real-world business problems in commodity pricing and credit risk management.

The project is divided into four tasks that progressively build practical skills in data analysis, forecasting, financial modeling, predictive analytics, and optimization.

Business Objectives

The project addresses the following business problems:

- Forecast future natural gas prices using historical market data.
- Value natural gas storage contracts under different operating scenarios.
- Predict the probability that a borrower will default on a loan.
- Develop an optimized credit rating system by converting continuous FICO scores into categorical risk ratings.

Project Structure

JP_Morgan_Quantitative_Research_Forage/
├── data/
├── notebooks/
├── src/
|
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- JupyterLab

Repository Contents

Task 1 – Natural Gas Price Forecasting

Developed a forecasting model using historical natural gas prices to estimate future monthly prices and generate daily price estimates through interpolation.

Task 2 – Natural Gas Storage Contract Valuation

Built a reusable pricing model to estimate the value of natural gas storage contracts while accounting for storage costs, transportation costs, injection and withdrawal schedules, and profitability under different scenarios.

Task 3 – Probability of Default Modeling

Developed a supervised machine learning model to estimate the probability that a borrower will default on a loan using financial and credit-related characteristics. The model was also used to calculate the expected financial loss associated with each loan.

Task 4 – FICO Score Bucketing and Credit Rating

Implemented a dynamic programming algorithm to optimize FICO score buckets using a log-likelihood objective function. The resulting credit rating system converts continuous FICO scores into discrete risk categories suitable for downstream machine learning models.

Key Skills Demonstrated

- Time Series Forecasting
- Financial Modeling
- Contract Valuation
- Machine Learning
- Credit Risk Analytics
- Dynamic Programming
- Probability of Default (PD) Modeling
- Expected Loss (EL) Estimation
- Python Programming
- Data Analysis and Visualization

Future Improvements

Potential extensions to this project include:

- Hyperparameter tuning of the machine learning model.
- Comparison of multiple classification algorithms.
- Advanced time series forecasting techniques.
- More sophisticated optimization methods for credit score bucketing.
- Interactive dashboards for visualizing model outputs.

Acknowledgements

This project was completed as part of the JPMorgan Chase Quantitative Research Virtual Experience hosted on Forage.
