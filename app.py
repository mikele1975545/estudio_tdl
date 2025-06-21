import streamlit as st
from datetime import date
import gspread
from google.oauth2.service_account import Credentials
import json

# Leer credencial desde secrets
service_account_info = st.secrets["GOOGLE_SERVICE_ACCOUNT"]
creds = Credentials.from_service_account_info(service_account_info)
gc = gspread.authorize(creds)

# Abrir hoja
SHEET_ID = "AQUÍ_TU_ID_DE_GOOGLE_SHEET"
sheet = gc.open_by_key(SHEET_ID).sheet1

# Interfaz Streamlit
st.set_page_config(page_title="Estudio TDL", page_icon="📝")
st.title("📝 Estudio TDL | Recogida de Datos")

with st.form("estudio_form"):
    fecha = st.date_input("Fecha de la entrevista", value=date.today())
    codigo = st.number_input("Código del paciente", min_value=100, step=1)
    convivencia = st.selectbox("1. ¿Con quién convive?", ["Solo", "Familia", "Residencia", "Albergue", "Sin hogar"])
    laboral = st.selectbox("2. Situación laboral", ["Activo", "Desempleado", "Jubilado/Pensionista"])
    estudios = st.selectbox("3. ¿Ha tenido acceso a estudios?", ["Sí", "No"])
    acceso = st.selectbox("4. ¿Tiene acceso a dispositivos digitales?", ["Sí", "No"])
    actividad = st.selectbox("5. ¿Realiza actividad física?", ["Diario", "2-3 veces semana", "Rara vez", "Nunca"])

    submit = st.form_submit_button("Enviar")

if submit:
    datos = [str(fecha), int(codigo), convivencia, laboral, estudios, acceso, actividad]
    sheet.append_row(datos)
    st.success("✅ Datos enviados correctamente")
