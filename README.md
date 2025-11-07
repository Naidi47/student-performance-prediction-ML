# 🎓 Student Performance Prediction Project

## 📘 Overview
This project predicts students' **final grades (G3)** based on their academic, demographic, and social data.  
It uses **Linear Regression** to estimate how different features (study time, absences, prior grades, etc.) influence student performance.

---

## 📂 Project Structure
```
student_performance_project/
│
├── data/
│   └── student-mat.csv               # Dataset (to be added manually)
│
├── src/
│   ├── data_preprocessing.py         # Handles data loading, encoding, and scaling
│   ├── model_training.py             # Trains the ML model
│   └── evaluation.py                 # Evaluates and generates performance report
│
├── outputs/
│   ├── student_performance_model.pkl # Saved trained model
│   └── performance_report.txt        # Model evaluation results
│
├── requirements.txt                  # Python dependencies
└── main.py                           # Main pipeline script
```

---

##  How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Add Dataset
Download the dataset from the [UCI Repository](https://archive.ics.uci.edu/ml/datasets/student+performance)  
and place `student-mat.csv` in the `/data` folder.

### 3️⃣ Run the Pipeline
```bash
python main.py
```

---

##  Output Example

After running the project, you’ll get a detailed performance report in `/outputs/performance_report.txt`:

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

##  Learning Outcomes
- Hands-on practice with **regression analysis**
- Experience with **data preprocessing**, **encoding**, and **scaling**
- Understanding **feature importance** in ML models
- Modularized, **production-ready Python ML project structure**

---

## 👨‍💻 Author
**M Brahmanaidu**  
📧 Email: muchukuntlabrahmanaidu@gmail.com  
🌐 GitHub: [Naidi47](https://github.com/Naidi47)  
🔗 LinkedIn: [Brahmanaidu Muchukuntla](https://www.linkedin.com/in/brahmanaidu-muchukuntla-17a1a9242/)
