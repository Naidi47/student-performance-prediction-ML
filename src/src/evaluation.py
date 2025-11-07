import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
from datetime import datetime

def evaluate_model(model, X_test, y_test, feature_names, output_path='outputs/performance_report.txt'):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    importance = pd.Series(model.coef_, index=feature_names)
    top_features = importance.sort_values(ascending=False).head(5)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        "=========================================
"
        "STUDENT PERFORMANCE PREDICTION REPORT
"
        "=========================================
"
        f"Timestamp         : {timestamp}
"
        "Model Used        : Linear Regression
"
        "-----------------------------------------
"
        f"Mean Absolute Error (MAE) : {mae:.2f}
"
        f"Root Mean Squared Error   : {rmse:.2f}
"
        f"R^2 Score (Accuracy)      : {r2:.2f}
"
        "-----------------------------------------
"
        "Top 5 Important Features:
"
        f"{top_features.to_string()}
"
        "=========================================
"
        "Report generated successfully.
"
        "=========================================
"
    )
    print(report)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    return mae, rmse, r2
