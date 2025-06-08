from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the IRIS dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.40, random_state=42)

# Print the number of items in the test sample
print(f"Quantidade de itens na amostra de teste: {len(X_test)}")