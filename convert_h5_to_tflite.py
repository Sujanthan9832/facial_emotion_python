import tensorflow as tf

# Load the trained .h5 model
model = tf.keras.models.load_model("model.h5")  # Change "model.h5" to your model's path

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted TFLite model
with open("model.tflite", "wb") as f:
    f.write(tflite_model)

print("Model successfully converted to TFLite format and saved as model.tflite")