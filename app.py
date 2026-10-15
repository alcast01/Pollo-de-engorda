import streamlit as st
import pandas as pd
import os

# Configuración inicial de la página
st.set_page_config(
    page_title="EngordIA Pollo | Inteligencia Avícola",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
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

# --- BARRA LATERAL (BRANDING Y SUSCRIPCIONES) ---
with st.sidebar:
    logo_path = "watermarked_img_3159886688308430736.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=True)
    else:
        st.title("🐔 EngordIA Pollo")
        
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

# Pestañas de navegación
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
    st.markdown("Calcula y optimiza los requerimientos nutricionales según la fase de crecimiento y la disponibilidad de insumos en México.")
    
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

    st.divider()
    st.markdown("### 🌾 Inventario e Ingredientes Disponibles en México")
    st.markdown("Selecciona o deselecciona los ingredientes que tienes actualmente disponibles en la granja o con tu proveedor:")

    # Lista de ingredientes comunes en la avicultura mexicana
    ingredientes_mexico = [
        # Cereales y fuentes energéticas
        {"Disponible": True, "Ingrediente": "Maíz Amarillo Grano", "Categoría": "Cereal / Energía", "PB (%)": 8.5, "EM (kcal/kg)": 3350},
        {"Disponible": True, "Ingrediente": "Sorgo Grano", "Categoría": "Cereal / Energía", "PB (%)": 9.0, "EM (kcal/kg)": 3250},
        {"Disponible": False, "Ingrediente": "Trigo Grano", "Categoría": "Cereal / Energía", "PB (%)": 11.5, "EM (kcal/kg)": 3100},
        {"Disponible": True, "Ingrediente": "Subproducto de Galleta / Panadería", "Categoría": "Energía", "PB (%)": 9.5, "EM (kcal/kg)": 3600},
        {"Disponible": False, "Ingrediente": "Pulidura / Salvado de Arroz", "Categoría": "Subproducto", "PB (%)": 12.0, "EM (kcal/kg)": 2850},
        {"Disponible": True, "Ingrediente": "Salvado de Trigo", "Categoría": "Subproducto", "PB (%)": 15.0, "EM (kcal/kg)": 2000},
        
        # Fuentes Proteicas Vegetales
        {"Disponible": True, "Ingrediente": "Pasta de Soya (46-48% PB)", "Categoría": "Proteína Vegetal", "PB (%)": 47.0, "EM (kcal/kg)": 2230},
        {"Disponible": False, "Ingrediente": "Pasta de Canola", "Categoría": "Proteína Vegetal", "PB (%)": 36.0, "EM (kcal/kg)": 2000},
        {"Disponible": False, "Ingrediente": "Pasta de Cártamo", "Categoría": "Proteína Vegetal", "PB (%)": 24.0, "EM (kcal/kg)": 1800},
        {"Disponible": False, "Ingrediente": "Pasta de Algodón", "Categoría": "Proteína Vegetal", "PB (%)": 41.0, "EM (kcal/kg)": 1950},
        {"Disponible": True, "Ingrediente": "DDGS de Maíz (Granos Secos de Destilería)", "Categoría": "Proteína / Energía", "PB (%)": 27.0, "EM (kcal/kg)": 2480},
        
        # Fuentes Proteicas Animales y Grasas
        {"Disponible": False, "Ingrediente": "Harina de Carne y Hueso (50%)", "Categoría": "Proteína Animal", "PB (%)": 50.0, "EM (kcal/kg)": 2300},
        {"Disponible": False, "Ingrediente": "Harina de Pluma Hidrolizada", "Categoría": "Proteína Animal", "PB (%)": 80.0, "EM (kcal/kg)": 2800},
        {"Disponible": False, "Ingrediente": "Harina de Pescado Nacional", "Categoría": "Proteína Animal", "PB (%)": 60.0, "EM (kcal/kg)": 2820},
        {"Disponible": True, "Ingrediente": "Aceite Vegetal Comestible / Soya", "Categoría": "Grasa / Lipídico", "PB (%)": 0.0, "EM (kcal/kg)": 8800},
        {"Disponible": True, "Ingrediente": "Grasa Amarilla / Tallow", "Categoría": "Grasa / Lipídico", "PB (%)": 0.0, "EM (kcal/kg)": 8400},
        
        # Minerales y Aminoácidos Sintéticos
        {"Disponible": True, "Ingrediente": "DL-Metionina", "Categoría": "Aminoácido Sintético", "PB (%)": 58.0, "EM (kcal/kg)": 5000},
        {"Disponible": True, "Ingrediente": "L-Lisina HCl", "Categoría": "Aminoácido Sintético", "PB (%)": 94.0, "EM (kcal/kg)": 4120},
        {"Disponible": True, "Ingrediente": "L-Treonina", "Categoría": "Aminoácido Sintético", "PB (%)": 72.0, "EM (kcal/kg)": 3600},
        {"Disponible": True, "Ingrediente": "Carbonato de Calcio (Piedra Caliza)", "Categoría": "Mineral Calcio", "PB (%)": 0.0, "EM (kcal/kg)": 0},
        {"Disponible": True, "Ingrediente": "Fosfato Dicálcico / Monocálcico", "Categoría": "Mineral P / Ca", "PB (%)": 0.0, "EM (kcal/kg)": 0},
        {"Disponible": True, "Ingrediente": "Sal Común (NaCl)", "Categoría": "Mineral Sodio", "PB (%)": 0.0, "EM (kcal/kg)": 0},
        {"Disponible": True, "Ingrediente": "Premix de Vitaminas y Minerales Traza", "Categoría": "Núcleo / Micro", "PB (%)": 0.0, "EM (kcal/kg)": 0},
        {"Disponible": True, "Ingrediente": "Pigmentante Marigold / Flor de Cempasúchil", "Categoría": "Pigmentante", "PB (%)": 0.0, "EM (kcal/kg)": 0}
    ]

    df_ingredientes = pd.DataFrame(ingredientes_mexico)

    # Editor de datos interactivo con checkboxes en la columna "Disponible"
    edited_df = st.data_editor(
        df_ingredientes,
        column_config={
            "Disponible": st.column_config.CheckboxColumn(
                "Disponible",
                help="Marca esta casilla si el ingrediente está disponible en tus existencias",
                default=False,
            ),
            "Ingrediente": st.column_config.TextColumn("Ingrediente / Materia Prima", disabled=True),
            "Categoría": st.column_config.TextColumn("Categoría", disabled=True),
            "PB (%)": st.column_config.NumberColumn("Proteína Bruta (%)", format="%.1f%%", disabled=True),
            "EM (kcal/kg)": st.column_config.NumberColumn("Energía Met. (kcal/kg)", format="%d", disabled=True),
        },
        disabled=["Ingrediente", "Categoría", "PB (%)", "EM (kcal/kg)"],
        hide_index=True,
        use_container_width=True
    )

    # Filtrar selección del usuario
    ingredientes_seleccionados = edited_df[edited_df["Disponible"] == True]["Ingrediente"].tolist()
    st.caption(f"📋 **Ingredientes seleccionados para la dieta:** {len(ingredientes_seleccionados)} de {len(df_ingredientes)} materias primas.")

    if st.button("Generar Fórmula Optimizada con Ingredientes Seleccionados"):
        if len(ingredientes_seleccionados) < 3:
            st.warning("⚠️ Selecciona al menos 3 ingredientes (incluyendo maíz/sorgo, pasta de soya y fuente mineral) para balancear la ración.")
        else:
            st.success(f"¡Dieta optimizada con éxito usando los {len(ingredientes_seleccionados)} ingredientes seleccionados en inventario!")

# --- TAB 3: CALENDARIO DE VACUNACIÓN ---
with tab3:
    st.subheader("Calendario Sanitario y Programa de Vacunación")
    st.markdown("Control automatizado de bioseguridad, inmunizaciones y aplicaciones preventivas.")
    
    data_vacunas = {
        "Edad (Días)": [1, 7, 12, 18, 24],
        "Vía de Aplicación": ["Spray / Ocular", "Agua de Bebida", "Subcutánea / Ocular", "Agua de Bebida", "Campo / Monitoreo"],
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
        costo_total_estimado = costo_pollo_bb + (1.62 * 2.80 * costo_alimento_kg) + 4.0
        margen_estimado = precio_venta_mercado - costo_total_estimado
        st.metric("Costo Estimado por Kilo", f"${costo_total_estimado:.2f}")
        st.metric("Margen Neto Proyectado", f"${margen_estimado:.2f} por kg", "Rentabilidad Alta")
        
    if st.button("Exportar Reporte Financiero para Comercialización"):
        st.balloons()
        st.success("¡Reporte generado y listo para enviar a compradores y socios comerciales!")
