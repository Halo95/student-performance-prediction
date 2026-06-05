"""
Student Performance Prediction

A simple machine learning project that predicts whether a student will pass
based on study habits and academic information.

Author: Brian Quartey
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# -----------------------------
# 1. Create a simple dataset
# -----------------------------
np.random.seed(42)

number_of_students = 200

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 25, number_of_students),
    "attendance_rate": np.random.randint(40, 101, number_of_students),
    "previous_score": np.random.randint(30, 101, number_of_students),
    "sleep_hours": np.random.randint(4, 10, number_of_students),
    "practice_tests": np.random.randint(0, 10, number_of_students),
})

# Create the target variable using simple logic.
# A student is more likely to pass if they study more, attend class often,
# have a good previous score, sleep enough, and complete practice tests.
data["passed"] = (
    (data["study_hours"] >= 8)
    & (data["attendance_rate"] >= 65)
    & (data["previous_score"] >= 50)
    & (data["practice_tests"] >= 2)
).astype(int)


# -----------------------------
# 2. Prepare the data
# -----------------------------
X = data.drop("passed", axis=1)
y = data["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# -----------------------------
# 3. Train the model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# -----------------------------
# 4. Evaluate the model
# -----------------------------
y_pred = model.predict(X_test)

print("Student Performance Prediction Model")
print("=" * 45)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# -----------------------------
# 5. Make a new prediction
# -----------------------------
new_student = pd.DataFrame({
    "study_hours": [12],
    "attendance_rate": [85],
    "previous_score": [70],
    "sleep_hours": [7],
    "practice_tests": [5],
})

prediction = model.predict(new_student)[0]
prediction_probability = model.predict_proba(new_student)[0][1]

print("\nExample Prediction")
print("=" * 45)
print(new_student)
print(f"Prediction: {'Pass' if prediction == 1 else 'Fail'}")
print(f"Probability of Passing: {prediction_probability:.2f}")


# -----------------------------
# 6. Show feature importance
# -----------------------------
feature_importance = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_[0]
}).sort_values(by="coefficient", ascending=False)

print("\nFeature Importance")
print("=" * 45)
print(feature_importance)
