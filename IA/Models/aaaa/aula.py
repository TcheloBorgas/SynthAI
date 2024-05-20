#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

app = Flask(__name__, template_folder=r'C:\Users\pytho\Documents\GitHub\SynthAI\IA\API\template')

rf_model = joblib.load(r'C:\Users\pytho\Documents\GitHub\SynthAI\IA\API\model')

# Definir os nomes das características e valores padrão
feature_names = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
    'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
    'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
] + [f'feature{i}' for i in range(20)]  # Adicionando características genéricas para chegar a 41

default_values = [0] * 41  # Ajuste conforme necessário, exemplo com zeros

# Definir um dicionário para mapear nomes de características a índices
feature_index = {name: i for i, name in enumerate(feature_names)}

#━━━━━━❮Função Produto❯━━━━━━━
def pred_churn(TotalCharges, MonthlyCharges, tenure):
    # Criar um array com valores padrão
    input_features = np.array(default_values, dtype=float)

    # Atualizar os valores com base nos dados fornecidos
    input_features[feature_index['TotalCharges']] = TotalCharges
    input_features[feature_index['MonthlyCharges']] = MonthlyCharges
    input_features[feature_index['tenure']] = tenure

    # Fazer a previsão
    pred_val = rf_model.predict_proba([input_features])
    prob_churn = pred_val[0][1]

    # Avaliar a probabilidade e retornar a mensagem correspondente
    if prob_churn < 0.25:
        return 'Chance Quase Nula de Churn'
    elif prob_churn < 0.50:
        return 'Pouca Chance de Churn'
    elif prob_churn < 0.60:
        return 'Chance Moderada de Churn'
    elif prob_churn < 0.75:
        return 'Chance Alta de Churn'
    else:
        return 'Chance Extrema de Churn'

#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        TotalCharges = float(request.form.get('TotalCharges'))
        MonthlyCharges = float(request.form.get('MonthlyCharges'))
        tenure = float(request.form.get('tenure'))
        pred = pred_churn(TotalCharges, MonthlyCharges, tenure)
    return render_template('index.html', pred=pred)

#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

if __name__ == '__main__':
    app.run(debug=True)
