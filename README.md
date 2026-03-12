# 🐍 ML Learning Journey

Decided to lock in and start learning AI/ML properly.  

This repo is basically me documenting the whole journey from **bare-minimum Python knowledge → hopefully competent AI/ML engineer someday**.

---

## 🗺️ The Plan

I'm following a structured roadmap so I don't end up randomly watching AI videos at 2 AM.

### ✅ Phase 1 — Python Foundations
> *Status: Complete ✅*

| Topic | Status |
|-------|--------|
| Variables & Data Types | ✅ Done |
| If / Else Logic | ✅ Done |
| Loops (for, while) | ✅ Done |
| Functions | ✅ Done |
| Lists & Dictionaries | ✅ Done |
| File I/O | ✅ Done |
| Error Handling | ✅ Done |

---

### ✅ Phase 2 — Data Manipulation & Visualization
> *Status: Complete ✅*

| Topic | What I Learned | Status |
|-------|---------------|--------|
| NumPy Arrays | Vectorization, boolean masks, `np.mean()` | ✅ Done |
| Pandas DataFrames | Creating, filtering, selecting columns | ✅ Done |
| Data Cleaning | `dropna()`, `fillna()`, `str.upper()`, removing outliers | ✅ Done |
| Exploratory Data Analysis | Shape, describe, missing values, insights | ✅ Done |
| Matplotlib | Bar charts, histograms | ✅ Done |
| Seaborn | `histplot`, `barplot`, `scatterplot`, `heatmap` | ✅ Done |
| CSV & JSON Files | Read, write, convert between formats | ✅ Done |

---

### ⏳ Phase 3 — Math for ML
> *Status: Up Next ⏳*

| Topic | What I'll Learn | Status |
|-------|----------------|--------|
| Linear Algebra Basics | Vectors, matrices, dot products | ⏳ Pending |
| Matrix Operations | Addition, multiplication with NumPy | ⏳ Pending |
| Probability & Statistics | Mean, variance, distributions | ⏳ Pending |
| Gradients & Derivatives | How ML models actually learn | ⏳ Pending |

---

### ⏳ Phase 4 — Machine Learning Core
> *Status: Coming Soon 🔜*

| Topic | What I'll Learn | Status |
|-------|----------------|--------|
| Scikit-learn Basics | The #1 ML library in Python | ⏳ Pending |
| Linear Regression | Predicting numbers | ⏳ Pending |
| Logistic Regression | Predicting categories | ⏳ Pending |
| Decision Trees | How models make decisions | ⏳ Pending |
| Train / Test Split | Avoiding cheating in ML! | ⏳ Pending |
| Model Evaluation | Accuracy, precision, recall | ⏳ Pending |
| Overfitting & Underfitting | The most common ML problem | ⏳ Pending |
| Cross Validation | Making models more reliable | ⏳ Pending |

---

### ⏳ Phase 5 — Deep Learning & AI
> *Status: Coming Soon 🔜*

| Topic | What I'll Learn | Status |
|-------|----------------|--------|
| Neural Networks | How the brain of AI works | ⏳ Pending |
| TensorFlow / Keras | Building deep learning models | ⏳ Pending |
| PyTorch Basics | The researcher's ML framework | ⏳ Pending |
| CNNs — Image AI | Teaching AI to see | ⏳ Pending |
| NLP & Text AI | Teaching AI to read | ⏳ Pending |
| Transfer Learning | Standing on the shoulders of giants | ⏳ Pending |
| Hugging Face | Using pre-trained AI models | ⏳ Pending |
| Prompt Engineering | Getting the best out of LLMs | ⏳ Pending |
| APIs (OpenAI, Anthropic) | Building real AI-powered apps | ⏳ Pending |

---

## 📁 Repository Structure

```
ml-learning-journey/
├── 📁 phase2-data-manipulation/
│   ├── day1_numpy_basics.py          # Arrays, vectorization, boolean masks
│   ├── day1_pandas_cleaning.py       # DataFrames, filtering, data cleaning
│   ├── day2_eda_titanic.py           # Exploratory Data Analysis on Titanic
│   ├── day2_seaborn_visualization.py # histplot, barplot, scatterplot, heatmap
│   ├── day2_csv_json_files.py        # Reading & writing CSV and JSON files
│   └── day3_eda_zomato.py            # Exploratory Data Analysis on Zomato (Food Delivery App Data)
└── 📁 datasets/
    ├── StudentPerformanceFactors.csv
    └── Zomato.csv
```

---

## 🔍 Real Insights I've Discovered

### 🚢 Titanic Dataset
- Only **38%** of passengers survived
- Female survival rate was **2x higher** than male
- `Cabin` had the most missing values — 687 out of 891 passengers!

### 🎓 Student Performance Dataset
- Exam scores follow a **normal distribution** — most students score 65–70
- **Hours studied** is the #1 factor in exam performance
- Motivation level had surprisingly **little impact** on final scores
- Discovered this with a single Seaborn heatmap — visual EDA is powerful!

---

## 🛠️ Tools Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

---

## 📊 Datasets Explored

| Dataset | Source | Purpose |
|---------|--------|---------|
| Titanic | [GitHub](https://github.com/datasciencedojo/datasets) | EDA & survival analysis |
| Student Performance Factors | [Kaggle](https://www.kaggle.com) | Visualization & correlation analysis |
| Zomato Dataset | [Kaggle](https://www.kaggle.com) | Visualization & correlation analysis |

---

## 💡 Things I've Learned the Hard Way

- `capitalize()` and `upper()` are NOT the same thing 😅
- Always use `index=False` when saving CSVs or you get an ugly extra column
- `np.mean()` ≠ dividing by a hardcoded number
- Commit early, commit often to stay consistent 
- Naming files `test1.py` is just dumb

---

## 🔜 What's Coming Next

- Phase 3 — Gradients, Probability & Linear Algebra (intuitively though, ugh i hate math)
- Phase 4 — First real ML model with Scikit-learn
- More Kaggle datasets & mini projects

---

*Will update regularly as long as i don't lose my sanity.*
*— Reshmmin Raj*
