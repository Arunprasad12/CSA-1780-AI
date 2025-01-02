import numpy as np
import tensorflow as tf
from tensorflow import keras

# Generate some toy data for demonstration
np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.randint(2, size=(100,))

# Build a simple feedforward neural network
model = keras.Sequential([
    keras.layers.Input(shape=(5,)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10, batch_size=16)

# Make predictions
sample_input = np.random.rand(5)
predictions = model.predict(np.array([sample_input]))
print("Sample Input:", sample_input)
print("Predictions:", predictions)
