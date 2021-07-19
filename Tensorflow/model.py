import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras.layers.core import Activation

data = keras.datasets.fashion_mnist

(train_img, train_label), (test_img, test_label) = data.load_data()

class_names = ['T-shirt/Top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

train_img  = train_img/255.0
test_img = test_img/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(156, activation="relu"),
    keras.layers.Dense(54, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
    ])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_img, train_label, epochs=5)

loss, acc = model.evaluate(test_img, test_label)

print("Loss:", loss)
print("Accuracy:", acc)