from src.data_preprocessing import load_data, preprocess_data
from src.model_training import train_model
from src.evaluation import evaluate_model

def main():
    print("Loading dataset...")
    df = load_data('data/student-mat.csv')
    print("Preprocessing data...")
    X_scaled, y, feature_names = preprocess_data(df)
    print("Training model...")
    model, X_test, y_test = train_model(X_scaled, y)
    print("Evaluating model...")
    evaluate_model(model, X_test, y_test, feature_names)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
