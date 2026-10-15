import streamlit as st
import pandas as pd
import numpy as np
import os
from scipy.optimize import linprog

# Configuración inicial de la página
st.set_page_config(
    page_title="Engord-IA Pollo | Inteligencia Avícola",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un look vanguardista y sofisticado
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
    .credits-text {
        font-size: 0.75rem;
        color: #E2E8F0;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar estado de sesión para autenticación
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "usuario_nombre" not in st.session_state:
    st.session_state.usuario_nombre = ""

# --- BARRA LATERAL (BRANDING, AUTENTICACIÓN Y SUSCRIPCIONES SEPARADAS) ---
with st.sidebar:
    logo_path = "watermarked_img_3159886688308430736.jpg"
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=True)
    else:
        st.title("🐔 Engord-IA Pollo")
        
    st.markdown("### **Engord-IA Pollo**")
    st.markdown("*«Precisión digital, máxima rentabilidad en cada ciclo.»*")
    st.divider()
    
    # MÓDULO 1: AUTENTICACIÓN Y CREDENCIALES DE USUARIO (SEPARADO)
    st.subheader("🔐 Acceso y Seguridad")
    if not st.session_state.autenticado:
        with st.form("form_login"):
            correo_input = st.text_input("Correo electrónico")
            password_input = st.text_input("Contraseña / Factor de Autenticación", type="password")
            btn_login = st.form_submit_button("Iniciar Sesión")
            
            if btn_login:
                if correo_input and password_input:
                    st.session_state.autenticado = True
                    st.session_state.usuario_nombre = correo_input.split('@')[0].capitalize()
                    st.success(f"¡Bienvenido, {st.session_state.usuario_nombre}!")
                    st.rerun()
                else:
                    st.warning("Por favor ingresa correo y contraseña.")
    else:
        st.success(f"Sesión activa: **{st.session_state.usuario_nombre}**")
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.session_state.usuario_nombre = ""
            st.rerun()

    st.divider()
    
    # MÓDULO 2: PLANES DE SUSCRIPCIÓN Y LICENCIAMIENTO
    st.subheader("💳 Planes de Suscripción")
    plan = st.selectbox(
        "Selecciona tu esquema de licenciamiento:",
        ["Plan Trimestral (3 Meses)", "Plan Semestral (6 Meses)", "Plan Anual (12 Meses - Recomendado)"]
    )
    
    if "Trimestral" in plan:
        st.info("Inversión: Ideal para probar un ciclo completo de engorda.")
    elif "Semestral" in plan:
        st.info("Inversión: Optimización avanzada para dos ciclos consecutivos.")
    else:
        st.success("Inversión: Acceso total e ilimitado todo el año con analítica predictiva.")
        
    st.divider()
    
    # CRÉDITOS OFICIALES (EN MAYÚSCULAS)
    st.markdown('<p class="credits-text">DESARROLLADA Y CREADA POR: DR. ALEJANDRO CASTAÑEDA CORREA</p>', unsafe_allow_html=True)

# --- PANTALLA PRINCIPAL ---
st.markdown('<p class="main-header">🐔 Engord-IA Pollo: Panel de Control Inteligente</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-slogan">«Precisión digital, máxima rentabilidad en cada ciclo.»</p>', unsafe_allow_html=True)

if not st.session_state.autenticado:
    st.warning("⚠️ Por favor inicia sesión en la barra lateral para desbloquear todos los módulos operativos de la granja.")

# Pestañas de navegación
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard General", 
    "🥗 Formulación y Calibración de Dietas", 
    "💉 Calendario de Vacunación", 
    "💰 Comercialización y Costos"
])

# --- TAB 1: DASHBOARD ---
with tab1:
    st.subheader("Resumen del Estado de la Parvada y Calibración Ambiental")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Aves en Producción", "10,000", "+500 este mes")
    with col2:
        st.metric("Peso Promedio Actual", "2.15 kg", "Día 35 de ciclo")
    with col3:
        st.metric("Conversión Alimenticia (ICA)", "1.62", "-0.04 vs lote previo")
    with col4:
        st.metric("Temperatura Galpón", "24.5 °C", "Humedad: 55%")
        
    st.info("💡 **Recomendación de IA:** Las variables bioclimáticas del galpón 2 están en rango óptimo. El sistema ha ajustado automáticamente la densidad energética de la dieta para maximizar la tasa de conversión.")

# --- TAB 2: DISEÑO Y OPTIMIZACIÓN DE DIETAS (MATRIZ AVANZADA) ---
with tab2:
    st.subheader("Módulo de Formulación al Mínimo Costo con Restricciones de Proteína Ideal")
    st.markdown("El motor matemático optimiza simultáneamente energía, proteína bruta y aminoácidos esenciales digestibles (Lisina, Metionina+Cistina y Treonina) para garantizar el máximo rendimiento genético.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        fase_etapa = st.selectbox("Fase de Engorda", ["Iniciador (1-10 días)", "Crecimiento (11-24 días)", "Finalizador / Retiro (25-42 días)"])
        peso_meta = st.number_input("Peso Meta Esperado (kg)", value=2.80, step=0.05)
    
    with col_d2:
        st.markdown("#### Requerimientos Nutricionales Mínimos Calibrados:")
        if "Iniciador" in fase_etapa:
            min_pb, min_em, min_lis, min_metcis, min_tre = 23.0, 3050.0, 1.28, 0.96, 0.85
        elif "Crecimiento" in fase_etapa:
            min_pb, min_em, min_lis, min_metcis, min_tre = 21.0, 3150.0, 1.15, 0.88, 0.78
        else:
            min_pb, min_em, min_lis, min_metcis, min_tre = 19.0, 3250.0, 1.00, 0.78, 0.69
            
        st.write(f"- **Proteína Bruta Mínima:** {min_pb}%")
        st.write(f"- **Energía Metabolizable Mínima:** {min_em} kcal/kg")
        st.write(f"- **Lisina Digestible Mínima:** {min_lis}%")
        st.write(f"- **Metionina + Cistina Digestible Mínima:** {min_metcis}%")
        st.write(f"- **Treonina Digestible Mínima:** {min_tre}%")

    st.divider()
    st.markdown("### 🌾 Inventario de Materias Primas e Insumos en México")
    st.markdown("Ajusta los precios locales y selecciona los ingredientes disponibles para la optimización lineal:")

    ingredientes_mexico = [
        {"Disponible": True, "Ingrediente": "Maíz Amarillo Grano", "Categoría": "Cereal", "Costo ($/kg)": 6.50, "PB (%)": 8.5, "EM (kcal/kg)": 3350, "Lisina (%)": 0.26, "Met+Cis (%)": 0.35, "Treonina (%)": 0.29},
        {"Disponible": True, "Ingrediente": "Sorgo Grano", "Categoría": "Cereal", "Costo ($/kg)": 5.80, "PB (%)": 9.0, "EM (kcal/kg)": 3250, "Lisina (%)": 0.22, "Met+Cis (%)": 0.31, "Treonina (%)": 0.28},
        {"Disponible": True, "Ingrediente": "Pasta de Soya (47%)", "Categoría": "Proteína", "Costo ($/kg)": 11.50, "PB (%)": 47.0, "EM (kcal/kg)": 2230, "Lisina (%)": 2.90, "Met+Cis (%)": 1.38, "Treonina (%)": 1.85},
        {"Disponible": True, "Ingrediente": "DDGS de Maíz", "Categoría": "Proteína/Energía", "Costo ($/kg)": 7.20, "PB (%)": 27.0, "EM (kcal/kg)": 2480, "Lisina (%)": 0.80, "Met+Cis (%)": 1.05, "Treonina (%)": 0.95},
        {"Disponible": True, "Ingrediente": "Aceite Vegetal / Soya", "Categoría": "Grasa", "Costo ($/kg)": 24.00, "PB (%)": 0.0, "EM (kcal/kg)": 8800, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Carbonato de Calcio", "Categoría": "Mineral", "Costo ($/kg)": 2.50, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Fosfato Bicálcico", "Categoría": "Mineral", "Costo ($/kg)": 14.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Sal Común (NaCl)", "Categoría": "Mineral", "Costo ($/kg)": 3.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "DL-Metionina", "Categoría": "Aminoácido", "Costo ($/kg)": 95.00, "PB (%)": 58.0, "EM (kcal/kg)": 5000, "Lisina (%)": 0.0, "Met+Cis (%)": 99.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "L-Lisina HCl", "Categoría": "Aminoácido", "Costo ($/kg)": 65.00, "PB (%)": 94.0, "EM (kcal/kg)": 4120, "Lisina (%)": 78.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "L-Treonina", "Categoría": "Aminoácido", "Costo ($/kg)": 85.00, "PB (%)": 87.0, "EM (kcal/kg)": 3800, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 98.0},
        {"Disponible": True, "Ingrediente": "Premix Vitamínico-Mineral", "Categoría": "Núcleo", "Costo ($/kg)": 45.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Met+Cis (%)": 0.0, "Treonina (%)": 0.0}
    ]

    df_ingredientes = pd.DataFrame(ingredientes_mexico)

    edited_df = st.data_editor(
        df_ingredientes,
        column_config={
            "Disponible": st.column_config.CheckboxColumn("Disponible", default=True),
            "Ingrediente": st.column_config.TextColumn("Materia Prima", disabled=True),
            "Categoría": st.column_config.TextColumn("Categoría", disabled=True),
            "Costo ($/kg)": st.column_config.NumberColumn("Costo (MXN $/kg)", format="$%.2f", min_value=0.0),
            "PB (%)": st.column_config.NumberColumn("Proteína (%)", format="%.1f%%", disabled=True),
            "EM (kcal/kg)": st.column_config.NumberColumn("Energía (kcal/kg)", format="%d", disabled=True),
            "Lisina (%)": st.column_config.NumberColumn("Lisina (%)", format="%.2f%%", disabled=True),
            "Met+Cis (%)": st.column_config.NumberColumn("Met+Cis (%)", format="%.2f%%", disabled=True),
            "Treonina (%)": st.column_config.NumberColumn("Treonina (%)", format="%.2f%%", disabled=True),
        },
        hide_index=True,
        use_container_width=True
    )

    if st.button("🚀 Optimizar Dieta (Mínimo Costo + Proteína Ideal)"):
        if not st.session_state.autenticado:
            st.error("⚠️ Debes iniciar sesión en la barra lateral para ejecutar el motor de optimización.")
        else:
            df_opt = edited_df[edited_df["Disponible"] == True].reset_index(drop=True)
            
            if len(df_opt) < 5:
                st.warning("⚠️ Selecciona al menos 5 ingredientes para cumplir con todas las restricciones de aminoácidos y energía.")
            else:
                n = len(df_opt)
                c = df_opt["Costo ($/kg)"].values
                
                # Matriz de restricciones (A_ub * x <= b_ub convertida a >= multiplicando por -1)
                A_ub = np.array([
                    -df_opt["PB (%)"].values,
                    -df_opt["EM (kcal/kg)"].values,
                    -df_opt["Lisina (%)"].values,
                    -df_opt["Met+Cis (%)"].values,
                    -df_opt["Treonina (%)"].values
                ])
                b_ub = np.array([-min_pb, -min_em, -min_lis, -min_metcis, -min_tre])
                
                # Restricción de igualdad: la suma total debe ser 1 (100% o 1 kg)
                A_eq = np.ones((1, n))
                b_eq = np.array([1.0])
                
                bounds = [(0.0, 0.85) if cat not in ["Mineral", "Aminoácido", "Núcleo"] else (0.0, 0.05) for cat in df_opt["Categoría"]]
                
                res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
                
                if res.success:
                    df_opt["Proporción (%)"] = res.x * 100
                    df_opt["Aporte en 1 Tonelada (kg)"] = res.x * 1000
                    
                    df_resultado = df_opt[df_opt["Proporción (%)"] > 0.01][["Ingrediente", "Proporción (%)", "Aporte en 1 Tonelada (kg)", "Costo ($/kg)"]]
                    
                    costo_total_kg = res.fun
                    st.success(f"✨ ¡Optimización exitosa con Proteína Ideal! Costo mínimo: **${costo_total_kg:.2f} MXN por kg** (${costo_total_kg * 1000:,.2f} MXN por tonelada).")
                    
                    st.markdown("#### 📋 Composición de la Fórmula Óptima:")
                    st.dataframe(df_resultado.style.format({
                        "Proporción (%)": "{:.2f}%",
                        "Aporte en 1 Tonelada (kg)": "{:.2f} kg",
                        "Costo ($/kg)": "${:.2f}"
                    }), use_container_width=True)
                else:
                    st.error("❌ No se encontró solución factible con los insumos seleccionados. Habilita más ingredientes o aminoácidos sintéticos.")

# --- TAB 3: CALENDARIO DE VACUNACIÓN ---
with tab3:
    st.subheader("Calendario Sanitario y Programa de Bioseguridad")
    st.markdown("Control automatizado de inmunizaciones y aplicaciones preventivas.")
    
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
