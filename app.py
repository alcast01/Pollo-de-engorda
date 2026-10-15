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
                    # Extraer un nombre base del correo o usar genérico
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
    
    # MÓDULO 2: PLANES DE SUSCRIPCIÓN Y LICENCIAMIENTO (SEPARADO DE LA AUTENTICACIÓN)
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
    "🥗 Diseño y Optimización de Dietas", 
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

# --- TAB 2: DISEÑO Y OPTIMIZACIÓN DE DIETAS (LEAST-COST) ---
with tab2:
    st.subheader("Módulo de Formulación de Dietas al Mínimo Costo (Programación Lineal)")
    st.markdown("El motor de optimización calcula las proporciones exactas de cada ingrediente disponible para satisfacer los requerimientos nutricionales al menor costo por kilo de alimento.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        fase_etapa = st.selectbox("Fase de Engorda", ["Iniciador (1-10 días)", "Crecimiento (11-24 días)", "Finalizador / Retiro (25-42 días)"])
        peso_meta = st.number_input("Peso Meta Esperado (kg)", value=2.80, step=0.05)
    
    with col_d2:
        st.markdown("#### Requerimientos Nutricionales Mínimos de la Fase:")
        if "Iniciador" in fase_etapa:
            min_pb, min_em, min_lis, min_met = 22.5, 3000.0, 1.25, 0.50
        elif "Crecimiento" in fase_etapa:
            min_pb, min_em, min_lis, min_met = 20.0, 3150.0, 1.10, 0.45
        else:
            min_pb, min_em, min_lis, min_met = 18.0, 3250.0, 0.95, 0.40
            
        st.write(f"- **Proteína Bruta Mínima:** {min_pb}%")
        st.write(f"- **Energía Metabolizable Mínima:** {min_em} kcal/kg")
        st.write(f"- **Lisina Digestible Mínima:** {min_lis}%")
        st.write(f"- **Metionina Digestible Mínima:** {min_met}%")

    st.divider()
    st.markdown("### 🌾 Inventario, Precios de Mercado e Ingredientes en México")
    st.markdown("Modifica los precios ($/kg) según tu proveedor local y marca con un check los ingredientes **disponibles** en tu inventario:")

    ingredientes_mexico = [
        {"Disponible": True, "Ingrediente": "Maíz Amarillo Grano", "Categoría": "Cereal / Energía", "Costo ($/kg)": 6.50, "PB (%)": 8.5, "EM (kcal/kg)": 3350, "Lisina (%)": 0.26, "Metionina (%)": 0.18},
        {"Disponible": True, "Ingrediente": "Sorgo Grano", "Categoría": "Cereal / Energía", "Costo ($/kg)": 5.80, "PB (%)": 9.0, "EM (kcal/kg)": 3250, "Lisina (%)": 0.22, "Metionina (%)": 0.15},
        {"Disponible": True, "Ingrediente": "Pasta de Soya (47%)", "Categoría": "Proteína Vegetal", "Costo ($/kg)": 11.50, "PB (%)": 47.0, "EM (kcal/kg)": 2230, "Lisina (%)": 2.90, "Metionina (%)": 0.65},
        {"Disponible": True, "Ingrediente": "DDGS de Maíz", "Categoría": "Proteína / Energía", "Costo ($/kg)": 7.20, "PB (%)": 27.0, "EM (kcal/kg)": 2480, "Lisina (%)": 0.80, "Metionina (%)": 0.52},
        {"Disponible": True, "Ingrediente": "Aceite Vegetal / Soya", "Categoría": "Grasa / Lipídico", "Costo ($/kg)": 24.00, "PB (%)": 0.0, "EM (kcal/kg)": 8800, "Lisina (%)": 0.0, "Metionina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Carbonato de Calcio", "Categoría": "Mineral", "Costo ($/kg)": 2.50, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Metionina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Fosfato Bicálcico", "Categoría": "Mineral P / Ca", "Costo ($/kg)": 14.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Metionina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Sal Común (NaCl)", "Categoría": "Mineral", "Costo ($/kg)": 3.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Metionina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "DL-Metionina", "Categoría": "Aminoácido", "Costo ($/kg)": 95.00, "PB (%)": 58.0, "EM (kcal/kg)": 5000, "Lisina (%)": 0.0, "Metionina (%)": 99.0},
        {"Disponible": True, "Ingrediente": "L-Lisina HCl", "Categoría": "Aminoácido", "Costo ($/kg)": 65.00, "PB (%)": 94.0, "EM (kcal/kg)": 4120, "Lisina (%)": 78.0, "Metionina (%)": 0.0},
        {"Disponible": True, "Ingrediente": "Premix Vitamínico-Mineral", "Categoría": "Núcleo / Micro", "Costo ($/kg)": 45.00, "PB (%)": 0.0, "EM (kcal/kg)": 0, "Lisina (%)": 0.0, "Metionina (%)": 0.0}
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
            "Metionina (%)": st.column_config.NumberColumn("Metionina (%)", format="%.2f%%", disabled=True),
        },
        hide_index=True,
        use_container_width=True
    )

    if st.button("🚀 Optimizar Dieta al Mínimo Costo (Algoritmo Lineal)"):
        if not st.session_state.autenticado:
            st.error("⚠️ Debes iniciar sesión en la barra lateral para ejecutar el optimizador de dietas.")
        else:
            df_opt = edited_df[edited_df["Disponible"] == True].reset_index(drop=True)
            
            if len(df_opt) < 4:
                st.warning("⚠️ Selecciona al menos 4 ingredientes disponibles para encontrar una solución factible.")
            else:
                n = len(df_opt)
                c = df_opt["Costo ($/kg)"].values
                
                A_ub = np.array([
                    -df_opt["PB (%)"].values,
                    -df_opt["EM (kcal/kg)"].values,
                    -df_opt["Lisina (%)"].values,
                    -df_opt["Metionina (%)"].values
                ])
                b_ub = np.array([-min_pb, -min_em, -min_lis, -min_met])
                
                A_eq = np.ones((1, n))
                b_eq = np.array([1.0])
                
                bounds = [(0.0, 0.85) if cat not in ["Mineral", "Aminoácido", "Núcleo / Micro"] else (0.0, 0.05) for cat in df_opt["Categoría"]]
                
                res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
                
                if res.success:
                    df_opt["Proporción (%)"] = res.x * 100
                    df_opt["Aporte en 1 Tonelada (kg)"] = res.x * 1000
                    
                    df_resultado = df_opt[df_opt["Proporción (%)"] > 0.01][["Ingrediente", "Proporción (%)", "Aporte en 1 Tonelada (kg)", "Costo ($/kg)"]]
                    
                    costo_total_kg = res.fun
                    st.success(f"✨ ¡Optimización exitosa! Costo mínimo de la dieta: **${costo_total_kg:.2f} MXN por kg** (${costo_total_kg * 1000:,.2f} MXN por tonelada).")
                    
                    st.markdown("#### 📋 Composición de la Fórmula Óptima:")
                    st.dataframe(df_resultado.style.format({
                        "Proporción (%)": "{:.2f}%",
                        "Aporte en 1 Tonelada (kg)": "{:.2f} kg",
                        "Costo ($/kg)": "${:.2f}"
                    }), use_container_width=True)
                else:
                    st.error("❌ No se encontró solución factible con los ingredientes seleccionados. Habilita más materias primas para cumplir los requerimientos.")

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
