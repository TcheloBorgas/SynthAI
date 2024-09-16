# app/api/credit_risk_model/credit_risk_api.py

from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib
from pycaret.classification import load_model, predict_model

router = APIRouter()

# Carregar o pipeline completo do modelo de risco de crédito
pipeline = load_model(r'C:\Users\pytho\Documents\GitHub\SynthAI\IA\app\api\credit_risk_model\credit_risk_pipeline')

# Carregar as colunas esperadas
expected_columns = joblib.load(r'C:\Users\pytho\Documents\GitHub\SynthAI\IA\app\api\credit_risk_model\expected_columns.joblib')

# Definir o esquema de dados de entrada
class CreditRiskInput(BaseModel):
    data: list  # Lista de dicionários com os dados de entrada

@router.post('/predict')
def predict_credit_risk(input_data: CreditRiskInput):
    # Converter a lista de dicionários em DataFrame
    df = pd.DataFrame(input_data.data)

    # Adicionar colunas faltantes com valor padrão (por exemplo, 0 ou NaN)
    missing_cols = set(expected_columns) - set(df.columns)
    for col in missing_cols:
        df[col] = 0  # Ou outro valor padrão apropriado

    # Garantir que as colunas estão na mesma ordem
    df = df[expected_columns]

    # Fazer previsões usando o pipeline
    predictions = predict_model(pipeline, data=df)

    # Extrair a coluna de previsão (ajustado para 'prediction_label')
    preds = predictions['prediction_label'].tolist()

    # Retornar as previsões
    return {'predictions': preds}
