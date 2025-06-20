
import streamlit as st
from datetime import date
import gspread
from google.oauth2.service_account import Credentials
import json
import os

# Leer credencial desde secret
service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
creds = Credentials.from_service_account_info(service_account_info)
gc = gspread.authorize(creds)

SHEET_ID = "1tpXTzYzNQKjlqho8Pywo0QulcyXLsr19WMVfEBoSPc8"
sheet = gc.open_by_key(SHEET_ID).sheet1

st.set_page_config(page_title="Estudio TDL", page_icon="💉")
st.title("🧪 Estudio TDL – Recogida de Datos")

with st.form("estudio_form"):
    fecha = st.date_input("Fecha de la entrevista", value=date.today())
    codigo = st.number_input("Código del paciente", min_value=100, step=1)
    convivencia = st.selectbox("1. ¿Con quién convive?", ["Solo", "Familia", "Residencia", "Albergue", "Sin hogar"])
    laboral = st.selectbox("2. Situación laboral", ["Activo", "Desempleado", "Jubilado/Pensionista"])
    acceso = st.selectbox("3. ¿Ha tenido acceso a estudios?", ["Sí", "No"])
    nivel = ""
    if acceso == "Sí":
        nivel = st.selectbox("   ¿Cuál es su nivel académico?", ["Sin estudios", "Básicos", "ESO/BUP", "Universitarios"])
    actividad = st.selectbox("4. ¿Realiza actividad física? ¿Con qué frecuencia?", ["Diario", "3-4 veces a la semana", "Semanal", "2-3 veces al mes", "Raras ocasiones"])
    cambio = st.selectbox("5. ¿Ha habido algún cambio en la actividad tras el TDL?", ["Incremento", "Sin cambios", "Disminución"])
    freq_enf = st.selectbox("6. ¿Cada cuánto le gustaría ser visitado por la enfermera?", ["Más de 1 vez al mes", "Mensualmente", "Cada 3 meses", "Menos de cada 3 meses"])
    coincide_enf = st.selectbox("7. ¿Esa frecuencia coincide con sus visitas actuales?", ["Sí", "No"])
    freq_psiq = st.selectbox("8. ¿Cada cuánto le gustaría ser visitado por su psiquiatra?", ["Más de 1 vez al mes", "Mensualmente", "Cada 3 meses", "Menos de cada 3 meses"])
    coincide_psiq = st.selectbox("9. ¿Esa frecuencia coincide con sus visitas actuales?", ["Sí", "No"])
    recomendar = st.selectbox("10. ¿Recomendaría este tratamiento?", ["Sí", "No"])
    submit = st.form_submit_button("Enviar")

    if submit:
        row = [
            fecha.strftime("%Y-%m-%d"),
            codigo,
            convivencia,
            laboral,
            acceso,
            nivel,
            actividad,
            cambio,
            freq_enf,
            coincide_enf,
            freq_psiq,
            coincide_psiq,
            recomendar
        ]
        sheet.append_row(row)
        st.success("✅ Datos guardados correctamente")
