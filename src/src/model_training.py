from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y, model_path='outputs/student_performance_model.pkl'):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model, X_test, y_test
