from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()
X = iris.data 
y = iris.target  
nomes_especies = iris.target_names  


modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)


sepal_length = float(input("Digite o comprimento da sépala (cm): "))
sepal_width = float(input("Digite a largura da sépala (cm): "))
petal_length = float(input("Digite o comprimento da pétala (cm): "))
petal_width = float(input("Digite a largura da pétala (cm): "))


nova_flor = [[sepal_length, sepal_width, petal_length, petal_width]]
predicao = modelo.predict(nova_flor)

print(f"A flor provavelmente é uma {nomes_especies[predicao[0]]}")
