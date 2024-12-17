from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from CustomPerceptron import CustomPerceptron
from MyFunctions import saveOutput
from Colors import Colors

print(f"########### {Colors.GREEN} Start {Colors.RESET}############")

def main():
    # Charger les données Iris
    data = load_iris()

    # Extraction des caractéristiques (X) et des labels (y)
    x = data.data.tolist()  # Convertir en liste pour compatibilité avec CustomPerceptron
    y = data.target.tolist()

    print(f"# Number of examples: {Colors.RED}{len(x)}{Colors.RESET}")
    print(f"# Number of features: {Colors.RED}{len(x[0])}{Colors.RESET}")
    print(f"# Features: {data.feature_names}")
    print(f"# Classes: {data.target_names}")

    # Séparation en ensembles d'entraînement et de test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print(f"----------- {Colors.YELLOW} Y' Predicted {Colors.RESET} -------------")

    # Initialisation et entraînement du perceptron personnalisé
    model = CustomPerceptron(learning_rate=0.01, n_iters=1000)
    model.fit(x_train, y_train)

    # Affichage des résultats
    print(f"Fitted weights: {model.getWeights()}")
    print(f"Bias W0: {model.getBias()}")

    # Prédictions sur les ensembles d'entraînement et de test
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    print(f"{Colors.YELLOW}{Colors.BOLD}y' (test) = {y_test_pred} {Colors.RESET}")
    print(f"Accuracy on training set: {model.score(x_train, y_train):.2f}")
    print(f"Accuracy on test set: {model.score(x_test, y_test):.2f}")

    print(f"------------ {Colors.GREEN} Y Desired {Colors.RESET} ------------")
    print(f"y (test) = {y_test}")

    # Sauvegarde des résultats dans un fichier
    weights = model.getWeights()
    function = f"function = {weights[0]}*x1 + {weights[1]}*x2 + {weights[2]}*x3 + {weights[3]}*x4 + {model.getBias()}\n"
    saveOutput(function, y_test_pred)

if __name__ == "__main__":
    main()