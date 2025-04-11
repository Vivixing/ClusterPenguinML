from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente entrenado
model = joblib.load("adaboost_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Obtener los datos del JSON enviado en la solicitud
        data = request.get_json()
        
        # Extraer los valores
        bill_length_mm = data["bill_length_mm"]
        bill_depth_mm = data["bill_depth_mm"]
        flipper_length_mm = data["flipper_length_mm"]
        body_mass_g = data["body_mass_g"]
        
        # Convertirlos en un array para la predicción
        features = np.array([[bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g]])
        
        # Realizar la predicción
        prediction = model.predict(features)
        
        # Retornar la respuesta en JSON
        return jsonify({"sex": str(prediction[0])})

    
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
