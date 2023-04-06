import tensorflow as tf
import numpy as np
import json

# load dataset.json
with open("dataset.json", "r") as f:
    dataset = json.loads(f.read())

# generate training data from dataset
training_data = []
for game in dataset:
    for move in game:
        training_data.append((move["board"], move["move"]))

# shuffle training data
np.random.shuffle(training_data)

# split training data into training and validation sets
split = int(len(training_data) * 0.8)

training_set = training_data[:split]
validation_set = training_data[split:]

# convert training and validation sets to numpy arrays
training_set = np.array(training_set)
validation_set = np.array(validation_set)

# create model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(9,)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(9, activation=tf.nn.tanh)
])

# compile model
model.compile(optimizer="adam", loss="mean_squared_error", metrics=["accuracy"])

# train model
model.fit(training_set[:, 0], training_set[:, 1], epochs=10, validation_data=(validation_set[:, 0], validation_set[:, 1]))

# save model
model.save("model.h5")
