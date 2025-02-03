# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample student data
data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 50, 65, 70, 85, 90, 45, 55, 60, 75],
    "Pass": [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]  # 0 = Fail, 1 = Pass
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['Marks']]  # Independent variable (Marks)
y = df['Pass']     # Dependent variable (Pass/Fail)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Display results
print("Model Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Predictions for Test Data:\n", pd.DataFrame({'Marks': X_test['Marks'], 'Actual': y_test, 'Predicted':y_pred}))
