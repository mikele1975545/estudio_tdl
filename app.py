
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

    dolor = st.selectbox("¿Ha referido dolor durante la administración?",
                         ["No", "Leve", "Moderado", "Intenso"])

    sangrado = st.selectbox("¿Ha habido sangrado tras la administración?",
                            ["No", "Puntiforme", "Moderado", "Abundante"])

    enrojecimiento = st.selectbox("¿Ha habido enrojecimiento o inflamación local tras la administración?",
                                  ["No", "Leve", "Moderado", "Intenso"])

    sensacion = st.selectbox("¿Ha notado alguna sensación anómala en la zona?",
                             ["No", "Hormigueo", "Calor o ardor", "Adormecimiento", "Dolor persistente"])

    general = st.selectbox("¿Cuál es su nivel de satisfacción general con la inyección recibida?",
                           ["Muy satisfecho/a", "Satisfecho/a", "Indiferente", "Insatisfecho/a", "Muy insatisfecho/a"])

    submitted = st.form_submit_button("Enviar")

    if submitted:
        if not codigo_paciente.isdigit() or not (100 <= int(codigo_paciente) <= 999):
            st.error("Introduce un código válido entre 100 y 999.")
        else:
            sheet.append_row([codigo_paciente, dolor, sangrado, enrojecimiento, sensacion, general])
            st.success("¡Gracias! Tus respuestas han sido registradas correctamente.")
