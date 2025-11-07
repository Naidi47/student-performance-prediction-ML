# 🎓 Student Performance Prediction Project

## 📘 Overview
This project predicts students' **final grades (G3)** based on their academic, demographic, and social data.  
It uses **Linear Regression** to estimate how different features (study time, absences, prior grades, etc.) influence student performance.

The notebook allows you to:
- Explore data interactively  
- Visualize relationships between features and target  
- Train and evaluate the model in individual code cells  
- View real-time charts, metrics, and outputs  

---

## 📂 Project Structure
```
student_performance_project/
│
├── data/
│   └── student-por.csv               # Dataset (to be added manually)
│
├── notebooks/
│   └── student_performance.ipynb     # Main Jupyter notebook (run cell by cell)
│
├── src/
│   ├── main.py                       # Script version (optional - full pipeline)
│   ├── data_preprocessing.py         # Handles data loading, encoding, and scaling
│   ├── model_training.py             # Trains the ML model
│   └── evaluation.py                 # Evaluates and generates performance report
│
├── outputs/
│   ├── student_performance_model.pkl # Saved trained model
│   └── performance_report.txt        # Model evaluation results
│
├── requirements.txt                  # Python dependencies
├── README.md                         # Documentation
└── .gitignore                        # Ignore cache, data, checkpoints, etc.
```

---

## 🧠 How to Run the Notebook

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Add Dataset
Download the dataset from the [UCI Repository](https://archive.ics.uci.edu/ml/datasets/student+performance)  
and place `student-por.csv` in the `/data` folder.

### 3️⃣ Open the Notebook
You can open and run the notebook in one of two ways:

#### 🖥️ Locally (Jupyter)
```bash
jupyter notebook notebooks/student_performance.ipynb
```

#### ☁️ In Google Colab
Click this badge to open directly in Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naidi47/student-performance-prediction-ML/blob/main/notebooks/student_performance.ipynb)

---

## 📊 Output Example

After running all cells, the notebook will:
- Display charts for data distribution and correlation  
- Print model evaluation metrics  
- Save a performance report in `/outputs/performance_report.txt`  

Example report:
```
=========================================
STUDENT PERFORMANCE PREDICTION REPORT
=========================================
Timestamp         : 2025-11-07 10:45:00
Model Used        : Linear Regression
-----------------------------------------
Mean Absolute Error (MAE) : 1.85
Root Mean Squared Error   : 2.25
R² Score (Accuracy)       : 0.83
-----------------------------------------
Top 5 Important Features:
G2           1.09
G1           0.94
studytime    0.15
absences    -0.08
failures    -0.06
=========================================
Report generated successfully.
=========================================
```

---

## 🎯 Learning Outcomes
- Hands-on practice with **regression analysis**
- Understand how **academic, social, and personal factors** affect student success
- Experience with **EDA**, **feature encoding**, and **scaling**
- Learn **model evaluation and visualization** within Jupyter
- Present an **interactive ML notebook** suitable for portfolio and GitHub

---

## 👨‍💻 Author
**M Brahmanaidu**  
📧 Email: muchukuntlabrahmanaidu@gmail.com  
🌐 GitHub: [Naidi47](https://github.com/Naidi47)  
🔗 LinkedIn: [Brahmanaidu Muchukuntla](https://www.linkedin.com/in/brahmanaidu-muchukuntla-17a1a9242/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naidi47/student-performance-prediction-ML/blob/main/notebooks/student_performance.ipynb)

