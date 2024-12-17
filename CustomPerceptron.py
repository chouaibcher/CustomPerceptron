from typing import Callable, List, Optional

class CustomPerceptron:
    def __init__(self, learning_rate: float = 0.01, n_iters: int = 1000, 
                 activation_func: Callable[[float], float] = None) -> None:
        self.lr: float = learning_rate
        self.n_iters: int = n_iters
        self.activation_func: Callable[[float], float] = activation_func if activation_func else self.relu
        self.weights: Optional[List[float]] = None
        self.bias: float = 0

    def fit(self, X: List[List[float]], y: List[float]) -> None:
        n_features: int = len(X[0]) 
        self.weights = [0.0] * n_features
        self.bias = 0

        for _ in range(self.n_iters):
            for index, x_i in enumerate(X):
                # Calcul de la sortie linéaire
                linear_output: float = sum(w * x for w, x in zip(self.weights, x_i)) + self.bias
                y_predicted: float = self.activation_func(linear_output)

                # Mise à jour des poids et du biais
                update: float = self.lr * (y[index] - y_predicted)
                self.weights = [w + update * x for w, x in zip(self.weights, x_i)]
                self.bias += update
    
    def getWeights(self) -> Optional[List[float]]:
        return self.weights

    def getBias(self) -> float:
        return self.bias

    def predict(self, X: List[List[float]]) -> List[float]:
        y_predicted = [
            self.activation_func(sum(w * x for w, x in zip(self.weights, x_i)) + self.bias) 
            for x_i in X
        ]
        return y_predicted
    
    def score(self, X: List[List[float]], y: List[float]) -> float:
        y_predicted = self.predict(X)
        accuracy: float = sum(y_p == y_t for y_p, y_t in zip(y_predicted, y)) / len(y)
        return accuracy

    @staticmethod
    def relu(x: float) -> float:
        """Applique la fonction ReLU."""
        return max(0, x)