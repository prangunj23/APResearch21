import csv 
import tensorflow as tf

from sklearn.model_selection import train_test_split

with open("data.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_training, y_training, epochs=20)

model.evaluate(X_testing, y_testing, verbose=2)