import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticación
gc = gspread.service_account(filename="myenfermeria-463615-69b941c0812f.json")

# Abrir hoja de cálculo
sheet = gc.open_by_key("1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk").sheet1

st.title("Encuesta para pacientes")

# Lista de preguntas
preguntas = [
    "¿Qué tratamiento inyectable mensual has recibido?",
    "¿Sientes molestias o dolor con el tratamiento?",
    "¿Has notado diferencias entre tratamientos?",
    "¿Preferirías seguir con el tratamiento actual?"
]

respuestas = []
with st.form(key="formulario"):
    for pregunta in preguntas:
        respuesta = st.text_input(pregunta)
        respuestas.append(respuesta)
    submitted = st.form_submit_button("Enviar")

# Guardar en Google Sheets
if submitted:
    sheet.append_row(respuestas)
    st.success("¡Gracias por responder!")
