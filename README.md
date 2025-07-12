# Airbnb Market Analysis and Visualization Dashboard

![GitHub Repo Size](https://img.shields.io/github/repo-size/NithinMN123/Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard)
![Last Commit](https://img.shields.io/github/last-commit/NithinMN123/Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the **Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard** repository! This project analyzes the impact of Airbnb on NYC rentals using a blend of Python, SQL, and Tableau. We built an ETL pipeline, performed forecasting with scikit-learn, and created interactive dashboards to visualize pricing trends and listing saturation.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [ETL Pipeline](#etl-pipeline)
- [Forecasting](#forecasting)
- [Dashboards](#dashboards)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)

## Overview

The goal of this project is to provide insights into the Airbnb market in New York City. By analyzing rental prices and listing saturation, we can understand how Airbnb affects the traditional rental market. This project combines data analysis, visualization, and machine learning techniques to deliver a comprehensive view of the market dynamics.

## Technologies Used

This project utilizes the following technologies:

- **Python**: For data manipulation and analysis.
- **SQL**: For database management and queries.
- **Tableau**: For creating interactive dashboards.
- **scikit-learn**: For machine learning and forecasting.
- **Pandas**: For data manipulation.
- **Matplotlib & Seaborn**: For data visualization.
- **PostgreSQL**: For database management.

## Project Structure

The repository is organized as follows:

```
Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── forecasting_model.ipynb
│
├── src/
│   ├── etl/
│   ├── forecasting/
│   ├── visualization/
│
├── requirements.txt
├── README.md
```

- **data/**: Contains raw and processed datasets.
- **notebooks/**: Jupyter notebooks for exploratory analysis and modeling.
- **src/**: Source code for ETL, forecasting, and visualization.
- **requirements.txt**: List of dependencies.

## Getting Started

To get started with this project, clone the repository and install the required packages.

```bash
git clone https://github.com/NithinMN123/Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard.git
cd Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard
pip install -r requirements.txt
```

## ETL Pipeline

The ETL (Extract, Transform, Load) pipeline is a crucial part of this project. It extracts data from various sources, transforms it for analysis, and loads it into a PostgreSQL database.

### Steps in the ETL Process

1. **Extract**: Data is pulled from various APIs and CSV files.
2. **Transform**: Data is cleaned and structured for analysis.
3. **Load**: The transformed data is loaded into a PostgreSQL database.

The ETL scripts are located in the `src/etl/` directory. You can run them using Python:

```bash
python src/etl/extract.py
python src/etl/transform.py
python src/etl/load.py
```

## Forecasting

We implemented forecasting using scikit-learn. The model predicts future rental prices based on historical data. 

### Steps for Forecasting

1. **Data Preparation**: The dataset is split into training and testing sets.
2. **Model Selection**: We use linear regression for forecasting.
3. **Model Evaluation**: The model is evaluated using metrics like RMSE.

You can find the forecasting code in the `src/forecasting/` directory. Run the forecasting notebook to see the results.

```bash
jupyter notebook notebooks/forecasting_model.ipynb
```

## Dashboards

We created interactive dashboards using Tableau to visualize key metrics. These dashboards help stakeholders understand market trends and make informed decisions.

### Key Features of the Dashboards

- **Pricing Trends**: Visualizes historical rental prices over time.
- **Listing Saturation**: Shows the number of active listings in different neighborhoods.
- **Comparative Analysis**: Compares Airbnb listings with traditional rentals.

To access the dashboards, please refer to the Tableau workbook in the `dashboards/` directory.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, please create a pull request. 

### Steps to Contribute

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

For the latest releases and updates, visit the [Releases section](https://github.com/NithinMN123/Airbnb-Driven-Market-Saturation-and-Forecasting-Visualization-Dashboard/releases). You can download the latest version of the project and execute it on your local machine.

![Download Releases](https://img.shields.io/badge/download-releases-brightgreen)

By exploring the **Releases section**, you can stay updated with the latest changes and improvements made to the project. 

Feel free to dive into the code, analyze the data, and visualize the results. Your feedback is important for making this project better!