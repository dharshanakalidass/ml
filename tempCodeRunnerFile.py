import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = pd.read_csv("C:/keerthana/Book2.csv")

# Step 2: Encode the Date to numerical values
le = LabelEncoder()
data['DateEncoded'] = le.fit_transform(data['Date'])

# Step 3: Prepare the data for training
X = data[['DateEncoded']]
y = data['GoldRate']

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
predicted = model.predict(X_test)

# Step 7: Display results
print("Model Coefficient:", model.coef_[0])
print("Model Intercept:", model.intercept_)
print("Predictions for Test Data:")
for actual, pred in zip(y_test, predicted):
    print(f"Actual: {actual}, Predicted: {pred}")

# Step 8: Visualize the data
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Linear Fit')
plt.xlabel('Date Encoded')
plt.ylabel('Gold Rate')
plt.title('Gold Rate Prediction')
plt.legend()
plt.show()