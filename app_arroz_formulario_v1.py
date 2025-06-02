
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Sistema de Gestión de Arroz V1", layout="centered")

st.title("🌾 Sistema de Gestión de Parcelas de Arroz V1")

# Lista de variedades (tomadas de tu mapa)
variedades = [
    "PAMPEIRO",
    "CATIANA COMUN",
    "CATIANA RI",
    "424 RI",
    "902 CL",
    "A 704"
]

# Inicializamos la sesión de datos si no existe
if "datos" not in st.session_state:
    st.session_state["datos"] = []

# Formulario de carga
with st.form("formulario_parcela"):
    st.subheader("➕ Cargar nueva parcela")
    parcela = st.text_input("Nombre de la parcela")
    hectareas = st.number_input("Superficie (has)", min_value=0.0, step=0.01)
    variedad = st.selectbox("Variedad", variedades)
    fecha_siembra = st.date_input("Fecha de siembra", value=datetime.date(2024, 8, 1))
    fecha_cosecha = st.date_input("Fecha de cosecha", value=datetime.date(2025, 2, 1))

    ciclo = (fecha_cosecha - fecha_siembra).days

    submitted = st.form_submit_button("Agregar parcela")

    if submitted:
        nueva_fila = {
            "Parcela": parcela,
            "Hectáreas": hectareas,
            "Variedad": variedad,
            "Fecha Siembra": fecha_siembra,
            "Fecha Cosecha": fecha_cosecha,
            "Ciclo (días)": ciclo
        }
        st.session_state["datos"].append(nueva_fila)
        st.success("✅ Parcela agregada correctamente")

# Mostrar tabla de parcelas cargadas
if st.session_state["datos"]:
    st.subheader("📊 Parcelas cargadas")
    df = pd.DataFrame(st.session_state["datos"])
    st.dataframe(df, use_container_width=True)

    # Descarga de Excel
    @st.cache_data
    def convertir_excel(df):
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        return output.getvalue()

    datos_excel = convertir_excel(df)
    st.download_button(
        label="📥 Descargar Excel",
        data=datos_excel,
        file_name="parcelas_arroz.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.warning("No hay parcelas cargadas aún.")
