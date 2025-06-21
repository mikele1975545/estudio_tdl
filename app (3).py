
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Configuración de acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("myenfermeria-463615-69b941c0812f.json", scope)
client = gspread.authorize(credentials)

sheet = client.open_by_key("1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk").sheet1

st.title("Encuesta para profesionales de enfermería")

# Preguntas de la encuesta
genero = st.selectbox("Género del paciente", ["Hombre", "Mujer", "Otro"])
edad = st.selectbox("Edad", ["<18", "18-30", "31-45", "46-65", ">65"])
facilidad = st.selectbox("¿Cómo calificarías la facilidad de administración de la inyección?",
                         ["Muy fácil", "Fácil", "Neutral", "Difícil", "Muy difícil"])
dolor = st.selectbox("¿El paciente refiere dolor durante la inyección?", ["Sí", "No"])
grado_dolor = st.selectbox("¿Qué grado de dolor refiere el paciente?",
                           ["Sin dolor", "Leve", "Moderado", "Intenso"])
tratamiento = st.selectbox("¿Qué tratamiento ha recibido el paciente?",
                            ["Palmeux", "Xeplion", "Paliperidona EFG", "Otro"])
comentarios = st.text_area("Comentarios adicionales")

if st.button("Enviar respuesta"):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [fecha, genero, edad, facilidad, dolor, grado_dolor, tratamiento, comentarios]
    sheet.append_row(data)
    st.success("Respuesta enviada con éxito. ¡Gracias por participar!")
