import numpy as np


class MachineLearningModel:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_trained = False
        self.coefficient = None
        self.intercept = None

    def train(self, X_axis, Y_axis):
        x_mean = X_axis.mean()
        y_mean = Y_axis.mean()
        numerator = ((X_axis - x_mean) * (Y_axis - y_mean)).sum()
        denominator = ((X_axis - x_mean) ** 2).sum()
        self.coefficient = numerator / denominator
        self.intercept = y_mean - (self.coefficient * x_mean)
        self.is_trained = True

    def predict(self, input_data):

        if self.is_trained is False:
            return "Oops it seems like model isn't trained."

        return self.intercept + self.coefficient * input_data


# Creating an instance of MachineLearningModel
ml_model = MachineLearningModel(
    "Simple Linear Regression Model", "Linear Regression")

# mock training data
X_axis = np.array([1.0, 2.0, 3.0])
Y_axis = np.array([2.0, 3.0, 4.0])

# Training the model
ml_model.train(X_axis, Y_axis)

# Training status after training
print(f"Model {ml_model.name} is trained: {ml_model.is_trained}")

# Make a prediction with new input data
input_data = 4.0
prediction = ml_model.predict(input_data)
print(f"Input: {input_data}")
print(f"Prediction: {prediction}")
