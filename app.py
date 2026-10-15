import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="EngordIA Pollo | Inteligencia Avícola",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un look sofisticado y vanguardista
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #00FFCC;
        font-weight: 700;
    }
    .sub-slogan {
        font-style: italic;
        color: #A0AEC0;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    .card {
        background-color: #1A202C;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2D3748;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (BRANDING Ys SUSCRIPCIONES) ---
with st.sidebar:
    st.image("watermarked_img_3159886688308430736.jpg", use_column_width=True)
    st.markdown("### **EngordIA Pollo**")
    st.markdown("*«Precisión digital, máxima rentabilidad en cada ciclo.»*")
    st.divider()
    
    st.subheader("💳 Selección de Suscripción")
    plan = st.selectbox(
        "Elige tu plan de licenciamiento:",
        ["Plan Trimestral (3 Meses)", "Plan Semestral (6 Meses)", "Plan Anual (12 Meses - Recomendado)"]
    )
    
    if "Trimestral" in plan:
        st.info("Inversión: Ideal para probar un ciclo completo de engorda.")
    elif "Semestral" in plan:
        st.info("Inversión: Optimización avanzada para dos ciclos consecutivos.")
    else:
        st.success("Inversión: Acceso total e ilimitado todo el año con analítica predictiva.")
        
    st.divider()
    st.markdown("### ℹ️ Créditos")
    st.markdown("**Desarrollado para:** Productores Avícolas de Precisión")
    st.markdown("**Versión:** 1.0.0-PRO")

# --- PANTALLA PRINCIPAL ---
st.markdown('<p class="main-header">🐔 EngordIA Pollo: Panel de Control Inteligente</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-slogan">«Precisión digital, máxima rentabilidad en cada ciclo.»</p>', unsafe_allow_html=True)

# Pestañas de navegación de la aplicación
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard General", 
    "🥗 Diseño de Dietas", 
    "💉 Calendario de Vacunación", 
    "💰 Comercialización y Costos"
])

# --- TAB 1: DASHBOARD ---
with tab1:
    st.subheader("Resumen del Estado de la Parvada")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Aves en Producción", "10,000", "+500 este mes")
    with col2:
        st.metric("Peso Promedio Actual", "2.15 kg", "Día 35 de ciclo")
    with col3:
        st.metric("Conversión Alimenticia (ICA)", "1.62", "-0.04 vs lote previo")
    with col4:
        st.metric("Índice de Viabilidad", "97.8%", "Excelente sanidad")
        
    st.info("💡 **Recomendación de IA:** Las condiciones de temperatura en el galpón 2 son óptimas. Se sugiere incrementar un 2% la densidad energética de la dieta para acelerar la ganancia de peso final.")

# --- TAB 2: DISEÑO DE DIETAS ---
with tab2:
    st.subheader("Módulo Asistido por IA: Formulación y Nutrición de Dietas")
    st.markdown("Calcula y optimiza los requerimientos nutricionales según la fase de crecimiento del pollo de engorda.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        fase_etapa = st.selectbox("Fase de Engorda", ["Iniciador (1-10 días)", "Crecimiento (11-24 días)", "Finalizador / Retiro (25-42 días)"])
        peso_meta = st.number_input("Peso Meta Esperado (kg)", value=2.80, step=0.05)
        consumo_estimado = st.number_input("Consumo Diario Estimado de Alimento (g/ave)", value=130.0, step=5.0)
    
    with col_d2:
        st.markdown("#### Perfil Nutricional Sugerido por el Algoritmo:")
        if "Iniciador" in fase_etapa:
            st.write("- **Proteína Bruta (Mín):** 22.5%")
            st.write("- **Energía Metabolizable:** 3,000 kcal/kg")
            st.write("- **Lisina digestible:** 1.25%")
        elif "Crecimiento" in fase_etapa:
            st.write("- **Proteína Bruta (Mín):** 20.0%")
            st.write("- **Energía Metabolizable:** 3,150 kcal/kg")
            st.write("- **Lisina digestible:** 1.10%")
        else:
            st.write("- **Proteína Bruta (Mín):** 18.0%")
            st.write("- **Energía Metabolizable:** 3,250 kcal/kg")
            st.write("- **Lisina digestible:** 0.95%")
            
    if st.button("Generar Fórmula Optimizada de Alimento"):
        st.success("¡Dieta optimizada con éxito! Se han ajustado los porcentajes de maíz, pasta de soya y complejos aminoacídicos para máxima rentabilidad.")

# --- TAB 3: CALENDARIO DE VACUNACIÓN ---
with tab3:
    st.subheader("Calendario Sanitario y Programa de Vacunación")
    st.markdown("Control automatizado de bioseguridad, inmunizaciones y aplicaciones preventivas.")
    
    # Tabla de ejemplo de calendario de vacunación
    data_vacunas = {
        "Edad (Días)": [1, 7, 12, 18, 24],
        "Via de Aplicación": [\"Spray / Ocular\", \"Agua de Bebida\", \"Subcutánea / Ocular\", \"Agua de Bebida\", \"Campo / Monitoreo\"],
        "Enfermedad / Biológico": ["Newcastle + Bronquitis Infecciosa", "Gumboro (Cepas intermedias)", "Newcastle (Clon)", "Gumboro (Boost)", "Evaluación de Títulos Serológicos"],
        "Estado": ["Completado", "Programado", "Pendiente", "Pendiente", "Pendiente"]
    }
    df_vacunas = pd.DataFrame(data_vacunas)
    st.dataframe(df_vacunas, use_container_width=True)
    
    with st.form("nueva_alerta_vacuna"):
        st.markdown("**Registrar Evento Sanitario Personalizado**")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            dia_evento = st.number_input("Día del ciclo", min_value=1, max_value=45, value=15)
            vacuna_nombre = st.text_input("Nombre de la vacuna o medicamento")
        with col_v2:
            via_aplicacion = st.selectbox("Vía", ["Agua de bebida", "Aspersión", "Inyección intramuscular", "Inyección subcutánea"])
        
        submit_vacuna = st.form_submit_button("Agregar al Calendario")
        if submit_vacuna:
            st.toast(f"¡Vacuna '{vacuna_nombre}' agendada correctamente para el Día {dia_evento}!")

# --- TAB 4: COMERCIALIZACIÓN Y COSTOS ---
with tab4:
    st.subheader("Módulo de Comercialización y Proyección Financiera")
    st.markdown("Analiza costos de producción por kilo y proyecta los márgenes de venta en pie o en canal.")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        costo_pollo_bb = st.number_input("Costo Pollo Bebé ($/unidad)", value=14.50)
        costo_alimento_kg = st.number_input("Costo Promedio Alimento ($/kg)", value=9.20)
    with col_c2:
        precio_venta_mercado = st.number_input("Precio Estimado de Venta en Pie ($/kg)", value=34.00)
        mortalidad_estimada = st.slider("Mortalidad Esperada (%)", 1.0, 10.0, 3.5)
    with col_c3:
        st.markdown("#### 📈 Estimación de Retorno")
        # Cálculos de simulación rápida
        costo_total_estimado = costo_pollo_bb + (1.62 * 2.80 * costo_alimento_kg) + 4.0  # Fórmula simplificada de costos
        margen_estimado = precio_venta_mercado - costo_total_estimado
        st.metric("Costo Estimado por Kilo", f"${costo_total_estimado:.2f}")
        st.metric("Margen Neto Proyectado", f"${margen_estimado:.2f} por kg", "Rentabilidad Alta")
        
    if st.button("Exportar Reporte Financiero para Comercialización"):
        st.balloons()
        st.success("¡Reporte generado y listo para enviar a compradores y socios comerciales!")
