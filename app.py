import streamlit as st
import pandas as pd
import json
from google.oauth2.service_account import Credentials
import gspread
from datetime import date

st.title("Encuesta de Satisfacción - Inyectable de Larga Duración")

# Conexión con Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(st.secrets["GOOGLE_SERVICE_ACCOUNT"], scopes=scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(st.secrets["SHEET_ID"]).sheet1

st.markdown("### Fecha de hoy")
fecha = st.date_input("Seleccione la fecha", value=date.today())

st.markdown("### 1. ¿Con quién convive actualmente?")
convivencia = st.selectbox("", ["Solo", "Familia", "Residencia", "Albergue", "Sin hogar"])

st.markdown("### 2. ¿Cuál es su situación laboral?")
laboral = st.selectbox("", ["Activo", "Desempleado", "Jubilado/Pensionista"])

st.markdown("### 3. ¿Ha tenido acceso a estudios?")
acceso_estudios = st.selectbox("", ["Sí", "No"])
nivel_estudios = ""
if acceso_estudios == "Sí":
    nivel_estudios = st.selectbox("Nivel académico:", ["Sin estudios", "Básicos", "ESO/BUP", "Universitarios"])

st.markdown("### 4. ¿Realiza actividad física? ¿Con qué frecuencia?")
actividad_fisica = st.selectbox("", ["Diario", "3-4 veces/semana", "Semanal", "2-3 veces/mes", "Raras ocasiones"])

st.markdown("### 5. ¿Ha cambiado alguna actividad desde el uso de TDL?")
cambio_actividad = st.selectbox("", ["Incremento", "Sin cambios", "Disminución"])

st.markdown("### 6. ¿Con qué frecuencia le gustaría ser visitado por la enfermera?")
frecuencia_enfermera = st.selectbox("", ["Más de 1 vez al mes", "Mensualmente", "Cada 3 meses", "Menos de cada 3 meses"])

st.markdown("### 7. ¿Esta frecuencia se corresponde con sus visitas programadas?")
frecuencia_enfermera_actual = st.selectbox("", ["Sí", "No"])

st.markdown("### 8. ¿Con qué frecuencia le gustaría ser visitado por su psiquiatra?")
frecuencia_psiquiatra = st.selectbox("", ["Más de 1 vez al mes", "Mensualmente", "Cada 3 meses", "Menos de cada 3 meses"])

st.markdown("### 9. ¿Esta frecuencia se corresponde con sus visitas programadas?")
frecuencia_psiquiatra_actual = st.selectbox("", ["Sí", "No"])

st.markdown("### 10. ¿Recomendaría este tratamiento?")
recomendacion = st.selectbox("", ["Sí", "No"])

if st.button("Enviar respuestas"):
    fila = [
        str(fecha), convivencia, laboral, acceso_estudios, nivel_estudios,
        actividad_fisica, cambio_actividad, frecuencia_enfermera,
        frecuencia_enfermera_actual, frecuencia_psiquiatra,
        frecuencia_psiquiatra_actual, recomendacion
    ]
    sheet.append_row(fila)
    st.success("¡Respuestas enviadas correctamente!")