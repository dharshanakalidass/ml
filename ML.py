# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Step 1: Load Dataset
boston_data = pd.read_csv("C:/keerthana/BostonHousing.csv")

# Separate features and target
X = boston_data.drop('medv', axis=1)  # 'medv' is the target column (Median value of owner-occupied homes)
y = boston_data['medv']

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate the Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Step 5: Save the Model
joblib.dump(model, "boston_linear_regression_model.pkl")
print("Model saved as 'boston_linear_regression_model.pkl'")

# Step 6: Load the Model
loaded_model = joblib.load("boston_linear_regression_model.pkl")
print("Loaded model from file.")

# Step 7: Make Predictions with the Loaded Model
# Use first 5 rows from the test set for predictions
new_data = X_test.iloc[:5]
predictions = loaded_model.predict(new_data)
print("Predictions for new data:", predictions)

# Display new data and predictions
print("Input Data:\n", new_data)
print("Predicted Prices:\n",predictions)
