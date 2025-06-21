
import streamlit as st
import pandas as pd
import datetime
import gspread
from google.oauth2.service_account import Credentials

# Configuración de conexión con Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(".streamlit/myenfermeria-463615-69b941c0812f.json", scopes=scope)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key("1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk")
worksheet = spreadsheet.sheet1

st.set_page_config(page_title="Encuesta de satisfacción - Palmeux", layout="centered")

st.title("Encuesta de satisfacción sobre tratamientos inyectables de larga duración")

# Opciones fijas para los desplegables
zonas = ["Hospital Clínic", "Hospital de Bellvitge", "Hospital de Alcorcón", "CSMA Cornellà", "Hospital de Vic", "CSMA Collblanch"]
respuestas = ["Sí", "No", "Pendiente", "Enviado", "No interesa"]
dolor = ["Nada", "Poco", "Moderado", "Mucho"]

# Preguntas del formulario
codigo_paciente = st.text_input("Código del paciente (número identificador anonimizado)")
fecha = st.date_input("Fecha de administración", value=datetime.date.today())
zona = st.selectbox("Centro", zonas)
producto = st.selectbox("¿Qué paliperidona se le ha administrado al paciente?", ["Palmeux", "Xeplion", "Paliperidona genérica"])

doler_inyeccion = st.selectbox("¿La inyección le ha dolido?", dolor)
comparacion = st.selectbox("Si ha probado otros tratamientos, ¿cómo se compara esta inyección con las otras?", ["Peor", "Igual", "Mejor", "No aplica"])
comentarios = st.text_area("Comentarios adicionales (opcional)")

if st.button("Enviar respuestas"):
    data = [str(codigo_paciente), str(fecha), zona, producto, doler_inyeccion, comparacion, comentarios]
    worksheet.append_row(data)
    st.success("¡Respuestas enviadas correctamente!")
