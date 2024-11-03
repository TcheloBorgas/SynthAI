# app.py

import streamlit as st
import requests
import json

# Configuração da URL base da API FastAPI
API_URL = "http://127.0.0.1:8000"

# Título da aplicação
st.title("API Modular de Modelos de Machine Learning")
st.sidebar.title("Modelos de Previsão")
st.sidebar.write("Selecione o modelo para realizar previsões.")

# Seleção do modelo
model_choice = st.sidebar.selectbox(
    "Escolha o Modelo",
    ("Risco de Crédito", "Churn Prediction", "Detecção de Fraude")
)

# Função para fazer requisição à API
def get_prediction(endpoint, data):
    url = f"{API_URL}/{endpoint}/predict"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps({"data": [data]}))
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao obter previsão")
        return None

# Interface para o modelo de Risco de Crédito
if model_choice == "Risco de Crédito":
    st.subheader("Previsão de Risco de Crédito")
    
    # Campos de entrada para o modelo
    risk_rate = st.number_input("Risk Rate", value=4.5)
    credit_limit = st.number_input("Credit Limit", value=10000)
    income = st.number_input("Income", value=50000)
    n_bankruptcies = st.number_input("Number of Bankruptcies", value=0)
    n_accounts = st.number_input("Number of Accounts", value=3)
    n_issues = st.number_input("Number of Issues", value=1)
    application_time_in_funnel = st.number_input("Application Time in Funnel", value=5)
    external_data_provider_email_seen_before = st.number_input("Email Seen Before (times)", value=10)
    external_data_provider_fraud_score = st.number_input("Fraud Score", value=50)
    application_time_applied = st.number_input("Application Time Applied", value=12)
    marketing_channel = st.text_input("Marketing Channel", value="Email")
    email = st.text_input("Email Domain", value="gmail.com")
    facebook_profile = st.checkbox("Facebook Profile", value=True)
    shipping_state = st.text_input("Shipping State", value="SP")
    overnight = st.number_input("Overnight", value=0)
    score_1 = st.text_input("Score 1", value="A")
    score_2 = st.text_input("Score 2", value="A")
    real_state = st.text_input("Real State", value="SP")
    
    # Dicionário de dados
    data = {
        "risk_rate": risk_rate,
        "credit_limit": credit_limit,
        "income": income,
        "n_bankruptcies": n_bankruptcies,
        "n_accounts": n_accounts,
        "n_issues": n_issues,
        "application_time_in_funnel": application_time_in_funnel,
        "external_data_provider_email_seen_before": external_data_provider_email_seen_before,
        "external_data_provider_fraud_score": external_data_provider_fraud_score,
        "application_time_applied": application_time_applied,
        "marketing_channel": marketing_channel,
        "email": email,
        "facebook_profile": facebook_profile,
        "shipping_state": shipping_state,
        "overnight": overnight,
        "score_1": score_1,
        "score_2": score_2,
        "real_state": real_state
    }
    
    if st.button("Obter Previsão"):
        result = get_prediction("credit_risk", data)
        if result:
            st.write("Previsões:", result["predictions"])

# Interface para o modelo de Churn Prediction
elif model_choice == "Churn Prediction":
    st.subheader("Previsão de Churn")
    
    # Campos de entrada para o modelo
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.number_input("Senior Citizen", value=0)
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure", value=1)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly_charges = st.number_input("Monthly Charges", value=29.85)
    total_charges = st.number_input("Total Charges", value=29.85)
    
    # Dicionário de dados
    data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
    
    if st.button("Obter Previsão"):
        result = get_prediction("churn", data)
        if result:
            st.write("Previsões:", result["predictions"])

# Interface para o modelo de Detecção de Fraude
elif model_choice == "Detecção de Fraude":
    st.subheader("Detecção de Fraude")
    
    # Campos de entrada para o modelo
    step = st.number_input("Step", value=1)
    amount = st.number_input("Amount", value=1000.0)
    oldbalance_org = st.number_input("Old Balance Origin", value=5000.0)
    newbalance_orig = st.number_input("New Balance Origin", value=4000.0)
    oldbalance_dest = st.number_input("Old Balance Destination", value=10000.0)
    newbalance_dest = st.number_input("New Balance Destination", value=11000.0)
    transaction_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT"])
    
    # Dicionário de dados
    data = {
        "step": step,
        "amount": amount,
        "oldbalanceOrg": oldbalance_org,
        "newbalanceOrig": newbalance_orig,
        "oldbalanceDest": oldbalance_dest,
        "newbalanceDest": newbalance_dest,
        "type": transaction_type
    }
    
    if st.button("Obter Previsão"):
        result = get_prediction("fraud_detection/fraud", data)
        if result:
            st.write("Previsões:", result["predictions"])
