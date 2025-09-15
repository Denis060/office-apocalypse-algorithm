# The "Office Apocalypse" Algorithm: Predicting Commercial Real Estate Vacancy Risk in NYC

## 1. Project Overview
This repository contains the complete codebase and documentation for the **"Office Apocalypse" Algorithm**, a capstone project for the **CS668 Analytics course at Pace University**.

The goal is to develop a **machine learning model** to predict long-term vacancy risk for commercial office buildings in **New York City**, leveraging a diverse set of **public and alternative datasets**.

---

## 2. Problem Statement
The **COVID-19 pandemic** has fundamentally altered workplace culture, popularizing remote and hybrid models that reduce demand for traditional office space.

This shift threatens to create a **commercial vacancy crisis** in NYC, impacting:
- **Property values & tax revenue**
- **Small business viability**
- **Neighborhood vitality**

This project aims to create a **predictive tool** to identify which properties are most at risk of prolonged vacancy (≥12 months), providing **actionable insights** for:
- City planners → conversion and zoning strategies
- Investors & developers → early detection of distressed assets
- Small businesses → anticipating changes in foot traffic

---

## 3. Repository Structure
```
office-apocalypse-algorithm/
├── data/
│   ├── raw/                # Raw, immutable datasets
│   └── processed/          # Cleaned, feature-engineered datasets
│
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_prototyping.ipynb
│
├── scripts/
│   ├── data_processing.py   # Full data cleaning pipeline
│   └── train_model.py       # Train and evaluate final models
│
├── src/
│   └── utils.py             # Helper functions
│
├── final_report/
│   └── CS668_Final_Paper.pdf
│
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

---

## 4. Setup & Installation

**Clone the repository:**
```bash
git clone https://github.com/your-username/office-apocalypse-algorithm.git
cd office-apocalypse-algorithm
```

**Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```


**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Requirements file structure:**
The `requirements.txt` is organized by category for clarity:

```
# Core Libraries
pandas
numpy
scikit-learn
matplotlib
seaborn
geopandas

# Machine Learning
xgboost
lightgbm
shap

# Visualization & Mapping
folium
mapboxgl

# App/Deployment
streamlit

# Notebook Environment
jupyterlab
notebook

# Data Acquisition
beautifulsoup4
requests
```

**Run the analysis notebooks:**
All workflows are documented in the `/notebooks` folder.

---

## 5. Team Members
| Name                    | Role                          |
|-------------------------|-------------------------------|
| **Ibrahim Denis Fofanah** |  |
| **Bright Arowny Zaman**   |                      |
| **Jeevan Hemanth Yendluri** |                  |
|
