import pandas as pd
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Path to your dataset folder
DATA_FOLDER = 'dataset'  # Update this if needed

# Parameters
MAX_FEATURES = 126  # 2 hands * 21 landmarks * 3 (x, y, z)

def load_data(data_folder):
    all_features = []
    all_labels = []

    for filename in os.listdir(data_folder):
        if filename.endswith('.csv'):
            label = os.path.splitext(filename)[0]
            filepath = os.path.join(data_folder, filename)
            df = pd.read_csv(filepath)

            for _, row in df.iterrows():
                features = row.values.tolist()

                # Pad with 0s if fewer than 126 features (single hand, etc.)
                if len(features) < MAX_FEATURES:
                    features += [0.0] * (MAX_FEATURES - len(features))
                elif len(features) > MAX_FEATURES:
                    features = features[:MAX_FEATURES]

                all_features.append(features)
                all_labels.append(label)

    return np.array(all_features), np.array(all_labels)

# Load data
X, y = load_data(DATA_FOLDER)

# Assign generic feature names f0 to f125
feature_names = [f'f{i}' for i in range(MAX_FEATURES)]
X_df = pd.DataFrame(X, columns=feature_names)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Save the model
with open('gesture_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as gesture_model.pkl")
