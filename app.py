
import streamlit as st
import json
import pygsheets
import pandas as pd
from datetime import datetime

# Autenticación con Google Sheets usando Streamlit Secrets
service_account_info = st.secrets["gcp_service_account"]
gc = pygsheets.authorize(service_account_info=json.loads(json.dumps(service_account_info)))

# ID de la hoja de cálculo de Google Sheets
sheet_id = "1VQKD3lLJm2R2YNX-gEpE19h_SFR_s3ZyeSrMeyqW6zk"

# Abre la hoja de cálculo
sh = gc.open_by_key(sheet_id)
wks = sh[0]

st.title("Encuesta de satisfacción con el tratamiento inyectable")

# Definir preguntas y opciones
preguntas = {
    "¿Cuánto dolor has sentido en el momento de la inyección?": [
        "Ninguno", "Muy poco", "Poco", "Moderado", "Intenso"
    ],
    "¿En qué zona te han administrado la inyección?": [
        "Deltoides izquierdo", "Deltoides derecho", "Glúteo izquierdo", "Glúteo derecho"
    ],
    "¿Sientes que el dolor ha durado más que en otras ocasiones?": [
        "Sí", "No", "No lo sé"
    ],
    "¿Cuál era tu tratamiento en la inyección anterior?": [
        "Palmeux", "Xeplion", "Otra paliperidona inyectable mensual", "Otra paliperidona inyectable trimestral", "Otra paliperidona inyectable semestral", "No lo recuerdo"
    ],
    "¿Has notado alguna diferencia en el momento de la administración o en el dolor respecto a la inyección anterior?": [
        "Sí", "No", "No lo sé"
    ]
}

respuestas = {}

# Mostrar preguntas
for pregunta, opciones in preguntas.items():
    respuesta = st.selectbox(pregunta, opciones)
    respuestas[pregunta] = respuesta

# Botón para enviar
if st.button("Enviar respuestas"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fila = [now] + list(respuestas.values())
    wks.append_table(fila)
    st.success("¡Respuestas enviadas correctamente!")
