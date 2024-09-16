# app/main.py
from fastapi import FastAPI
from api.churn_model.churn_api import router as churn_router
from api.credit_risk_model.credit_risk_api import router as credit_router
# from api.fraud_detection_model.fraud_api import router as fraud_router

app = FastAPI(title='API Modular de Modelos de Machine Learning')

app.include_router(churn_router, prefix='/churn', tags=['Churn Prediction'])
app.include_router(credit_router, prefix='/credit_risk', tags=['Credit Risk Prediction'])
# app.include_router(fraud_router, prefix='/fraud_detection', tags=['Fraud Detection'])



# C:\Users\pytho>curl -X POST "http://127.0.0.1:8000/churn/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"gender\":\"Female\",\"SeniorCitizen\":0,\"Partner\":\"Yes\",\"Dependents\":\"No\",\"tenure\":1,\"PhoneService\":\"Yes\",\"MultipleLines\":\"No\",\"InternetService\":\"DSL\",\"OnlineSecurity\":\"No\",\"OnlineBackup\":\"Yes\",\"DeviceProtection\":\"No\",\"TechSupport\":\"No\",\"StreamingTV\":\"No\",\"StreamingMovies\":\"No\",\"Contract\":\"Month-to-month\",\"PaperlessBilling\":\"Yes\",\"PaymentMethod\":\"Electronic check\",\"MonthlyCharges\":29.85,\"TotalCharges\":29.85}]}"
# {"predictions":[0]}
# C:\Users\pytho>curl -X POST "http://127.0.0.1:8000/credit_risk/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"risk_rate\":4.5,\"credit_limit\":10000,\"income\":50000,\"n_bankruptcies\":0,\"n_accounts\":3,\"n_issues\":1,\"application_time_in_funnel\":5,\"external_data_provider_email_seen_before\":10,\"external_data_provider_fraud_score\":50,\"application_time_applied\":12,\"marketing_channel\":\"Email\",\"email\":\"gmail.com\",\"facebook_profile\":true,\"shipping_state\":\"SP\",\"overnight\":0,\"score_1\":\"A\",\"score_2\":\"A\",\"real_state\":\"SP\"}]}"
# {"predictions":[0]}
# C:\Users\pytho>
