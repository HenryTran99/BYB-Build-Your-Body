from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen zur Fitness-App!"

# Beispiel für eine Route, die einen Trainingsplan zurückgibt
@app.route('/get-training-plan', methods=['POST'])
def get_training_plan():
    data = request.get_json()
    # Hier würdest du die Logik hinzufügen, um den Trainingsplan basierend auf den User-Daten zu erstellen
    # Zum Beispiel, je nach Fitnesslevel und Zielen des Nutzers
    return jsonify({
        "training_plan": "Hier ist dein Trainingsplan basierend auf den angegebenen Daten!"
    })

if __name__ == "__main__":
    app.run(debug=True)