
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="Encuesta de satisfacción", layout="centered")

# Autenticación con Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("myenfermeria-463615-69b941c0812f.json", scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key("1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk").sheet1

st.title("Encuesta de satisfacción")

with st.form("formulario"):
    codigo_paciente = st.text_input("Código del paciente (número entre 100-999)", max_chars=3)

    dolor = st.selectbox("¿Ha sentido dolor al administrar la inyección?",
                         ["Nada de dolor", "Poco dolor", "Algo de dolor", "Mucho dolor", "Dolor insoportable"])

    enrojecimiento = st.selectbox("¿Se ha producido enrojecimiento o inflamación en la zona de la inyección?",
                                  ["No", "Sí, leve", "Sí, moderado", "Sí, intenso"])

    sangrado = st.selectbox("¿Ha sangrado tras la administración?",
                            ["No", "Sí, muy poco", "Sí, moderado", "Sí, abundante"])

    sensacion = st.selectbox("¿Ha notado alguna sensación anómala en la zona?",
                             ["Ninguna", "Hormigueo", "Calor o ardor", "Adormecimiento", "Dolor persistente"])

    general = st.selectbox("¿Cuál es su satisfacción general con la inyección recibida?",
                           ["Muy satisfecho/a", "Satisfecho/a", "Ni satisfecho/a ni insatisfecho/a",
                            "Insatisfecho/a", "Muy insatisfecho/a"])

    submitted = st.form_submit_button("Enviar")

    if submitted:
        if not codigo_paciente.isdigit() or not (100 <= int(codigo_paciente) <= 999):
            st.error("Introduce un código válido entre 100 y 999.")
        else:
            sheet.append_row([codigo_paciente, dolor, enrojecimiento, sangrado, sensacion, general])
            st.success("¡Gracias! Tus respuestas han sido registradas correctamente.")
