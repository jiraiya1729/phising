import os
import joblib

def predict(features):
    # Load the SVM model
    model_path = 'H:\phising\phising\model\svc_model.joblib'
    svm_model = joblib.load(model_path)

    # Preprocess features if needed (e.g., scaling or encoding)
    # Ensure that the features are in the same format as they were during training

    # Make predictions
    predictions = svm_model.predict([features])

    return predictions
