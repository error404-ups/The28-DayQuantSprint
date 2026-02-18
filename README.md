# 📈 The 28-Day Quant Sprint

> *A self-driven 28-day journey to build Machine Learning for Quantitative Finance skills from the ground up — inspired by the research of Dr. Abhishek Jindal at DAIICT on stock movement prediction and portfolio optimization.*

---

## 🎯 Objective

This repository documents my structured 28-day sprint to gain hands-on experience at the intersection of **Machine Learning and Quantitative Finance**. The goal is to go from foundational Python and finance concepts to building research-grade projects involving NLP-based stock prediction, portfolio optimization, and options pricing — directly inspired by published academic work.

**Inspired by:**
- *"Integrating Price and Textual Data for Next-Day Stock Movement Prediction"* — Jindal et al., CODS-COMAD 2024
- *"FOUI-LR: Future-Oriented Ulcer Index for Portfolio Optimization"* — Jindal et al., CIMA 2025

---

## 🗂️ Repository Structure

```
The-28-Day-Quant-Sprint/
│
├── Week1_Financial_Data_Foundations/
│   ├── Day1_OHLCV_and_Returns.ipynb
│   ├── Day2_Volatility_and_Risk_Metrics.ipynb
│   ├── Day3_Sharpe_Ratio_and_Ulcer_Index.ipynb
│   ├── Day4_Candlestick_Charts_and_Indicators.ipynb
│   ├── Day5_RSI_MACD_Feature_Engineering.ipynb
│   ├── Day6_Correlation_and_Portfolio_Basics.ipynb
│   └── Day7_Week1_Mini_Project.ipynb
│
├── Week2_ML_for_Finance/
│   ├── Day8_Logistic_Regression_Stock_Prediction.ipynb
│   ├── Day9_Feature_Engineering_for_TimeSeries.ipynb
│   ├── Day10_Avoiding_Data_Leakage.ipynb
│   ├── Day11_Neural_Networks_in_PyTorch.ipynb
│   ├── Day12_Training_NN_on_Stock_Data.ipynb
│   ├── Day13_Model_Evaluation_Finance.ipynb
│   └── Day14_Week2_Mini_Project.ipynb
│
├── Week3_NLP_Sentiment_Analysis/
│   ├── Day15_Text_Preprocessing_Finance.ipynb
│   ├── Day16_VADER_Sentiment_Analysis.ipynb
│   ├── Day17_FinBERT_Financial_Sentiment.ipynb
│   ├── Day18_Combining_Text_and_Price_Features.ipynb
│   ├── Day19_StockNet_Dataset_Exploration.ipynb
│   ├── Day20_Replicating_Jindal_2024_Paper.ipynb
│   └── Day21_Week3_Mini_Project.ipynb
│
├── Week4_Portfolio_Optimization_and_Options/
│   ├── Day22_Markowitz_Mean_Variance.ipynb
│   ├── Day23_Ulcer_Index_Portfolio_Optimization.ipynb
│   ├── Day24_Black_Scholes_Pricer.ipynb
│   ├── Day25_Neural_Network_Options_Pricer.ipynb
│   ├── Day26_BS_vs_ML_Comparison.ipynb
│   ├── Day27_RL_for_Trading_Introduction.ipynb
│   └── Day28_Final_Project_and_Summary.ipynb
│
├── assets/
│   └── plots/
│
└── README.md
```

---

## 📅 Week-by-Week Breakdown

### Week 1 — Financial Data Foundations
Getting comfortable with real financial data, key metrics, and technical indicators using Python.

**Key concepts:** OHLCV data, log returns, volatility, Sharpe Ratio, Ulcer Index, moving averages, RSI, MACD

**Tools:** `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`

---

### Week 2 — Machine Learning for Finance
Applying core ML concepts to stock movement prediction — the right way, avoiding common pitfalls like data leakage.

**Key concepts:** Binary classification, feature engineering with time series, train/test split for financial data, neural networks in PyTorch

**Tools:** `scikit-learn`, `PyTorch`, `pandas`

---

### Week 3 — NLP & Sentiment Analysis
Combining news sentiment with price data to predict stock movement — directly replicating the methodology of the CODS-COMAD 2024 paper.

**Key concepts:** Text preprocessing, VADER sentiment, FinBERT, multimodal feature fusion, StockNet dataset

**Tools:** `transformers`, `FinBERT`, `NLTK`, `VADER`

---

### Week 4 — Portfolio Optimization & Options Pricing
Building portfolio optimization models and comparing classical Black-Scholes pricing against Neural Network-based approaches.

**Key concepts:** Markowitz optimization, Ulcer Index portfolio optimization, Black-Scholes model, Neural Network options pricer, intro to RL for trading

**Tools:** `scipy`, `PyTorch`, `numpy`

---

## 🚀 Key Projects

### 1. Stock Movement Predictor (Week 2 + 3)
A binary classifier that predicts next-day stock movement (up/down) by combining:
- Price-based features (returns, RSI, MACD, rolling volatility)
- Text-based features (FinBERT sentiment from financial news headlines)

Inspired directly by: *Jindal et al., CODS-COMAD 2024*

---

### 2. Ulcer Index Portfolio Optimizer (Week 4)
Implementation and comparison of:
- Classical Markowitz Mean-Variance Optimization
- Future-Oriented Ulcer Index based optimization (FOUI-LR)

Inspired directly by: *Jindal et al., CIMA 2025*

---

### 3. Black-Scholes vs Neural Network Options Pricer (Week 4)
A comparative study of classical and ML-based options pricing:
- Black-Scholes analytical pricer implemented from scratch
- Neural Network pricer trained on real options data
- Analysis of where Black-Scholes breaks down and where ML does better

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Data | `yfinance`, `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn` |
| Machine Learning | `scikit-learn`, `PyTorch` |
| NLP | `transformers`, `FinBERT`, `NLTK`, `VADER` |
| Finance | `scipy`, `QuantConnect` |
| Version Control | `git`, `GitHub` |

---

## 📚 References & Inspiration

1. Jindal, A. et al. — *"Integrating Price and Textual Data for Next-Day Stock Movement Prediction"*, CODS-COMAD 2024. [Link](https://link.springer.com/article/10.1007/s44248-025-00076-w)
2. Jindal, A. et al. — *"FOUI-LR: Future-Oriented Ulcer Index for Portfolio Optimization"*, CIMA 2025.
3. Hilpisch, Y. — *Python for Finance*, O'Reilly Media
4. Ding, X. et al. — *StockNet Dataset*, ACL 2018

---

## 📈 Progress Tracker

| Week | Status | Key Deliverable |
|---|---|---|
| Week 1 — Financial Data Foundations | 🟡 In Progress | Portfolio metrics notebook |
| Week 2 — ML for Finance | ⬜ Not Started | Stock movement classifier |
| Week 3 — NLP Sentiment Analysis | ⬜ Not Started | Text + price predictor |
| Week 4 — Portfolio & Options | ⬜ Not Started | BS vs NN options pricer |

---

## 👤 About

This sprint is part of my preparation for ML research in Quantitative Finance. I am documenting every step of the learning process — including mistakes, dead ends, and breakthroughs — to build both skills and accountability.

**Connect:** [LinkedIn](http://www.linkedin.com/in/poojan-patel-422837373) | [GitHub]([https://github.com/error404-ups](https://github.com/error404-ups))

---

*"An investment in knowledge pays the best interest." — Benjamin Franklin*