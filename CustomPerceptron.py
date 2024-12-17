import numpy as np

class CustomPerceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._threshold_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_features = X.shape[1] 
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iters):
            for index, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y[index] - y_predicted)
                self.weights += update * x_i
                self.bias += update
    
    def getWeights(self):
        return self.weights
    def getBias(self):
        return self.bias

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted
    
    def score(self, X, y):
        y_predicted = self.predict(X)
        accuracy = np.mean(y_predicted == y)
        return accuracy

    def _threshold_func(self, x):
        thresholds = [0, 1, 2]
        return np.digitize(x, thresholds, right=True)
    
