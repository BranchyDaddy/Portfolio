## 📌 About This Folder

This folder contains a collection of laboratory works completed during my university studies.  
Each project demonstrates practical application of data analysis techniques, machine learning models, and business intelligence approaches.

**Key skills demonstrated:**
- Data cleaning & preprocessing (pandas, numpy)
- Exploratory Data Analysis (EDA) with visualizations (matplotlib, seaborn)
- Feature engineering & dimensionality reduction
- Supervised learning (regression, classification)
- NLP & text vectorization (TF-IDF)
- Model evaluation & comparison
- Business insight generation

---

## 📁 Projects Overview

### 1. Pharmaceutical Sales Forecasting (Lab 4)
**File:** `Lab 4.ipynb`

**Task:** Predict sales volume of drug categories based on seasonality.

**Approach:**
- Merged data from 4 sources (sales, products, categories, stores)
- Created seasonal feature from dates
- Built ElasticNet model with cross-validation → improved with Poisson regression

**Results:**
| Metric | ElasticNet | Poisson | Improvement |
|--------|------------|---------|-------------|
| SMAPE  | 43.9%      | 16.5%   | **-62%**    |

**Key insight:** Poison regression significantly outperforms ElasticNet for count-based prediction tasks.

**Skills:** Data merging, EDA, time-based feature engineering, regression, model comparison.

---

### 2. Advertising Effectiveness Analysis (Lab 9)
**File:** `Lab 9.ipynb`

**Task:** Determine which advertising channels (TV, radio, newspaper) most influence product sales.

**Approach:**
- Polynomial regression (up to degree 4) to capture non-linear interactions
- Correlation analysis & feature interaction detection

**Results:**
- TV and radio are primary sales drivers
- Newspaper advertising had near-zero impact
- Polynomial degree 4 gave best predictive quality

**Key insight:** TV and radio have a synergistic effect — using both together produces additional lift.

**Skills:** Polynomial features, interaction effects, regression, visualization.

---

### 3. Author Attribution from Poetry Texts (Lab 5)
**File:** `Lab 5.ipynb`

**Task:** Classify poems by author based on text content.

**Approach:**
- Text vectorization (TF-IDF)
- Compared 4 models: Naive Bayes, Logistic Regression, SVM (RBF), Linear SVM

**Results:**
| Model | Accuracy |
|-------|----------|
| Logistic Regression | **81%** |
| Linear SVM | 80% |
| SVM (RBF) | 77% |
| Naive Bayes | 69% |

**Key insight:** Logistic regression performed best for this multi-class text classification task.

**Skills:** NLP, TF-IDF, multi-class classification, model comparison.

---

### 4. Customer Churn Analysis & Revenue Calculation (Lab 7)
**File:** `Lab 7.ipynb`

**Task:** Analyze telecom customer behavior, calculate revenue per tariff plan, and identify churn patterns.

**Approach:**
- Merged user, call, message, and internet session data
- Calculated actual revenue per user based on tariff overages
- Visualized spending distributions by tariff type

**Results:**
- Users on cheaper tariff (`smart`) paid **higher average bills** than premium tariff users
- `smart` tariff contributed ~3.2x more total revenue than `ultra`
- Only 7.6% of customers churned during the period

**Key insight:** The cheaper tariff generates more revenue due to overage charges — a potential pricing optimization opportunity.

**Skills:** Data merging, revenue modeling, overage calculation, business metrics.

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| Languages | Python |
| Data Manipulation | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn  |
| NLP | TF-IDF vectorization |
| Environment | Jupyter Notebook |

---
