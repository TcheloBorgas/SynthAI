# # app/api/fraud_detection_model/fraud_api.py

# from fastapi import APIRouter
# from pydantic import BaseModel
# import pandas as pd
# import joblib

# router = APIRouter()

# # Carregar o pipeline completo
# pipeline = joblib.load('app/api/fraud_detection_model/fraud_detection_pipeline.joblib')

# # Definir o esquema de dados de entrada
# class FraudInput(BaseModel):
#     data: list  # Lista de dicionários com os dados de entrada

# @router.post('/predict')
# def predict_fraud(input_data: FraudInput):
#     # Converter a lista de dicionários em DataFrame
#     df = pd.DataFrame(input_data.data)

#     # Fazer previsões usando o pipeline
#     predictions = pipeline.predict(df)

#     # Retornar as previsões
#     return {'predictions': predictions.tolist()}
