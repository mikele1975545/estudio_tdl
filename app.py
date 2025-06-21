import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="Estudio TDL", page_icon="📋", layout="centered")

st.title("Encuesta de satisfacción - Inyectables de larga duración")

# Preguntas
preguntas = [
    "¿Ha presentado el paciente dolor durante la inyección?",
    "¿El dolor fue leve, moderado o intenso?",
    "¿Ha presentado el paciente alguna reacción local en el punto de inyección?",
    "¿Cuál ha sido la duración aproximada de la administración del inyectable?",
    "¿Qué tipo de inyectable se ha administrado?",
    "¿Ha expresado el paciente preferencia por alguno de los tratamientos recibidos?",
    "¿Desea añadir alguna observación adicional?"
]

# Formulario
with st.form("formulario"):
    respuestas = []
    for pregunta in preguntas:
        if "observación" in pregunta.lower():
            respuesta = st.text_area(pregunta)
        else:
            respuesta = st.text_input(pregunta)
        respuestas.append(respuesta)

    submitted = st.form_submit_button("Enviar")

# Enviar respuestas a Google Sheets
if submitted:
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_key("1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk").sheet1
        sheet.append_row(respuestas)
        st.success("¡Respuestas enviadas correctamente!")
    except Exception as e:
        st.error(f"Error al enviar respuestas: {e}")
