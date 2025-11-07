import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df, target_col='G3'):
    label_enc = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = label_enc.fit_transform(df[col])
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, X.columns
