
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", SCOPE)
client = gspread.authorize(CREDS)

SHEET_ID = "1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk"
SHEET = client.open_by_key(SHEET_ID).sheet1

# --- OPCIONES DESPLEGABLES ---
opciones_genero = ["Hombre", "Mujer", "Otro", "Prefiero no decirlo"]
opciones_edad = ["<18", "18-25", "26-35", "36-45", "46-60", ">60"]
opciones_informacion = [
    "Personal sanitario", "Paciente actual", "Paciente anterior", 
    "Familiar o acompañante", "Otro"
]
opciones_tiempo = [
    "Menos de 1 mes", "1-6 meses", "6-12 meses", "Más de 1 año"
]
opciones_tratamiento = ["Mensual", "Trimestral", "Semestral", "No sé"]
opciones_dolor = ["Nada", "Poco", "Moderado", "Mucho", "Insoportable"]
opciones_efectos = ["Sí", "No", "No lo sé"]
opciones_comparacion = [
    "Sí, más cómodo", "Igual de cómodo", "Menos cómodo", "No he probado otros"
]
opciones_general = ["Muy satisfecho/a", "Satisfecho/a", "Neutral", "Insatisfecho/a", "Muy insatisfecho/a"]

# --- FORMULARIO ---
st.title("Encuesta de satisfacción sobre el tratamiento")

with st.form("formulario"):
    st.subheader("Datos personales")
    genero = st.selectbox("Género", opciones_genero)
    edad = st.selectbox("Edad", opciones_edad)
    info = st.selectbox("¿Por qué tienes esta información?", opciones_informacion)

    st.subheader("Sobre el tratamiento")
    tiempo = st.selectbox("¿Cuánto tiempo llevas recibiendo tratamiento?", opciones_tiempo)
    tipo = st.selectbox("¿Qué tipo de tratamiento recibes?", opciones_tratamiento)
    dolor = st.selectbox("¿Cuánto dolor sientes al administrarte la inyección?", opciones_dolor)
    efectos = st.selectbox("¿Has tenido efectos secundarios?", opciones_efectos)
    comparacion = st.selectbox("Comparado con otros tratamientos, ¿cómo es este?", opciones_comparacion)
    general = st.selectbox("En general, ¿cómo valoras este tratamiento?", opciones_general)

    enviado = st.form_submit_button("Enviar")

    if enviado:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fila = [fecha, genero, edad, info, tiempo, tipo, dolor, efectos, comparacion, general]
        SHEET.append_row(fila)
        st.success("✅ ¡Formulario enviado correctamente!")
