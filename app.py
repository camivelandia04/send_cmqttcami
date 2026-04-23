import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Panel IoT Interactivo",
    page_icon="⚡",
    layout="wide"
)

# ESTILOS PERSONALIZADOS (CSS)
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
        }
        .main {
            background-color: #0e1117;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 50px;
            font-size: 18px;
        }
        .card {
            background-color: #1c1f26;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>⚡ Panel de Control IoT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Interfaz moderna para control MQTT</p>", unsafe_allow_html=True)

# INFO SISTEMA
st.info(f"Python: {platform.python_version()}")

# VARIABLES
broker = "157.230.214.127"
port = 1883

# CALLBACKS
def on_publish(client, userdata, result):
    pass

def enviar_mensaje(topic, payload):
    client = paho.Client("camilov")
    client.on_publish = on_publish
    client.connect(broker, port)
    client.publish(topic, json.dumps(payload))

# LAYOUT EN COLUMNAS
col1, col2 = st.columns(2)

# TARJETA CONTROL DIGITAL
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔘 Control Digital")

    if st.button("Encender 🔥"):
        enviar_mensaje("cmqtt_s", {"Act1": "ON"})
        st.success("Dispositivo ENCENDIDO")

    if st.button("Apagar ❄️"):
        enviar_mensaje("cmqtt_s", {"Act1": "OFF"})
        st.error("Dispositivo APAGADO")

    st.markdown("</div>", unsafe_allow_html=True)

# TARJETA CONTROL ANALÓGICO
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎚️ Control Analógico")

    valor = st.slider("Ajusta el valor", 0.0, 100.0, 50.0)

    st.metric(label="Valor actual", value=valor)

    if st.button("Enviar Valor 🚀"):
        enviar_mensaje("cmqtt_a", {"Analog": float(valor)})
        st.success(f"Valor {valor} enviado correctamente")

    st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.caption("Desarrollado con Streamlit + MQTT | Interfaz rediseñada 🚀")
