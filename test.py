from tensorflow.keras.models import load_model

# Load the saved model
loaded_model = load_model('bitcoin_predictor_model.h5')
X_test
# Verify by predicting with the loaded model
predictions = loaded_model.predict(X_test)
print(predictions)