# app/api/churn_model/churn_api.py

from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

router = APIRouter()

# Carregar o pipeline treinado
pipeline = joblib.load(r'C:\Users\pytho\Documents\GitHub\SynthAI\IA\app\api\churn_model\churn_pipeline.joblib')

# Definir o esquema de dados de entrada
class ChurnInput(BaseModel):
    data: list  # Lista de dicionários com os dados de entrada

@router.post('/predict')
def predict_churn(input_data: ChurnInput):
    # Converter a lista de dicionários em DataFrame
    df = pd.DataFrame(input_data.data)

    # Pré-processamento adicional, se necessário
    # Converter 'TotalCharges' para numérico
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # Substituir 'No internet service' e 'No phone service' por 'No'
    df.replace('No internet service', 'No', inplace=True)
    df.replace('No phone service', 'No', inplace=True)

    # Fazer previsões usando o pipeline
    predictions = pipeline.predict(df)

    # Retornar as previsões
    return {'predictions': predictions.tolist()}
