import streamlit as st
import pandas as pd
import numpy as np
import os
from scipy.optimize import linprog

# Inicializar estado de sesión para autenticación y 2FA
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "usuario_nombre" not in st.session_state:
    st.session_state.usuario_nombre = ""
if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None
if "auth_stage" not in st.session_state:
    st.session_state.auth_stage = "planes"  # "planes", "login", "2fa_verify"
if "mock_code" not in st.session_state:
    st.mock_code = "1234"

# Configuración de la página
st.set_page_config(
    page_title="Engord-IA Pollo | Inteligencia Avícola",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded" if st.session_state.autenticado else "collapsed"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #00FFCC;
        font-weight: 700;
        margin-bottom: 0px;
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

# Ruta común del logotipo
logo_path = "watermarked_img_17480332752636885818.jpg"

# ==============================================================================
# PANEL IZQUIERDO (BARRA LATERAL) - SOLO VISIBLE SI EL USUARIO ESTÁ AUTENTICADO
# ==============================================================================
if st.session_state.autenticado:
    with st.sidebar:
        if os.path.exists(logo_path):
            st.image(logo_path, use_column_width=True)
        else:
            st.title("🐔 Engord-IA Pollo")
            
        st.divider()
        st.success(f"Sesión activa: **{st.session_state.usuario_nombre}**")
        st.info(f"Plan Activo: {st.session_state.selected_plan}")
        if st.button("🔴 Cerrar Sesión", use_column_width=True):
            st.session_state.autenticado = False
            st.session_state.usuario_nombre = ""
            st.session_state.auth_stage = "planes"
            st.session_state.selected_plan = None
            st.rerun()
            
        st.divider()

        # CALIBRACIÓN AVANZADA DE PRODUCCIÓN Y RENDIMIENTO
        st.subheader("⚙️ Calibración de Granja")
        st.markdown("Parámetros clave para rendimiento y control de costos:")
        
        with st.expander("🧬 Grupo 1: Genética y Lote"):
            linea_genetica = st.selectbox("Línea Genética", ["Cobb 500", "Ross 308", "Hubbard Classic", "Arbor Acres"])
            num_aves = st.number_input("Número de Aves Iniciales", value=10000, step=500)
            peso_inicial = st.number_input("Peso Inicial Promedio (g)", value=42.0, step=1.0)
            dias_ciclo = st.slider("Duración del Ciclo (Días)", 35, 56, 42)

        with st.expander("🎯 Grupo 2: Metas Productivas"):
            peso_meta = st.number_input("Peso Meta Comercial (kg)", value=2.80, step=0.05)
            ica_objetivo = st.number_input("ICA Objetivo (Conversión)", value=1.60, step=0.01)
            mortalidad_max = st.slider("Mortalidad Máxima Permisible (%)", 1.0, 10.0, 3.0)

        with st.expander("🌡️ Grupo 3: Ambiente y Galpón"):
            temp_galpon = st.slider("Temperatura Promedio (°C)", 18.0, 33.0, 24.0)
            humedad_galpon = st.slider("Humedad Relativa (%)", 50.0, 80.0, 65.0)
            densidad_aves = st.number_input("Densidad (Aves/m²)", value=12.0, step=1.0)
            fotoperiodo = st.slider("Fotoperiodo (Horas luz/día)", 16, 24, 20)

        with st.expander("💰 Grupo 4: Costos y Mercado"):
            costo_pollo_bb = st.number_input("Costo Pollo BB ($/unidad)", value=14.50, step=0.50)
            precio_venta = st.number_input("Precio Venta en Pie ($/kg)", value=34.00, step=0.50)

        st.divider()
        st.markdown('<p class="credits-text">DESARROLLADA Y CREADA POR: DR. ALEJANDRO CASTAÑEDA CORREA</p>', unsafe_allow_html=True)
else:
    # Ocultar la barra lateral en la pantalla de inicio
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)


# ==============================================================================
# PÁGINA DE INICIO (LANDING PAGE - FLUJO GUIADO DE SUSCRIPCIÓN -> AUTH -> 2FA)
# ==============================================================================
if not st.session_state.autenticado:
    # Cabecera Principal
    col_img_main, col_txt_main = st.columns([1, 3])
    with col_img_main:
        if os.path.exists(logo_path):
            st.image(logo_path, use_column_width=True)
    with col_txt_main:
        st.markdown('<p class="main-header">Engord-IA Pollo: Plataforma Avícola de Precisión</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-slogan">«Inteligencia artificial que potencia la nutrición, optimiza la ganancia de peso y blinda la rentabilidad de tus pollos con precisión matemática.»</p>', unsafe_allow_html=True)

    st.divider()

    # ETAPA 1: PLANES DE SUSCRIPCIÓN (PRIMERO)
    if st.session_state.auth_stage == "planes":
        st.markdown("### 📋 Paso 1: Selecciona tu Plan de Suscripción")
        st.markdown("Asegura el máximo rendimiento zootécnico y protege tus márgenes frente a la volatilidad de las materias primas:")
        
        col_p1, col_p2, col_p3 = st.columns(3)
        
        with col_p1:
            st.markdown("#### 🥉 Plan Trimestral")
            st.markdown("**Duración:** 3 Meses")
            st.markdown("### **$2,499 MXN**")
            st.markdown("""
* Ideal para evaluar un ciclo completo de engorda.
* Formulación lineal básica de dietas por mínimo costo.
* Registro y seguimiento de calendario sanitario.
""")
            if st.button("Elegir Plan Trimestral", use_column_width=True):
                st.session_state.selected_plan = "Plan Trimestral (3 Meses)"
                st.session_state.auth_stage = "login"
                st.rerun()

        with col_p2:
            st.markdown("#### 🥈 Plan Semestral")
            st.markdown("**Duración:** 6 Meses")
            st.markdown("### **$4,599 MXN**")
            st.markdown("""
* **Ahorro del 8%** frente al plan trimestral.
* Optimización avanzada para 2 ciclos consecutivos.
* Recomendaciones predictivas de IA y control de ICA.
""")
            if st.button("Elegir Plan Semestral", use_column_width=True):
                st.session_state.selected_plan = "Plan Semestral (6 Meses)"
                st.session_state.auth_stage = "login"
                st.rerun()

        with col_p3:
            st.markdown("#### 🥇 Plan Anual (PRO - Recomendado)")
            st.markdown("**Duración:** 12 Meses")
            st.markdown("### **$7,999 MXN**")
            st.markdown("""
* **¡Ahorro masivo del 20%!** (Equivalente a $666 MXN al mes).
* **Blindaje Anual de Costos:** Protege tu granja contra las fluctuaciones estacionales en el precio del maíz y la soya mediante formulación matemática continua.
* **Máxima Rentabilidad Garantizada:** Control total en múltiples ciclos de producción, minimizando el costo por kilo producido y maximizando tu conversión alimenticia (ICA).
* **Soporte Prioritario y Actualizaciones VIP:** Acceso anticipado a todos los módulos de analítica predictiva del Dr. Alejandro Castañeda Correa.
""")
            if st.button("🚀 Asegurar Licencia Anual", use_column_width=True):
                st.session_state.selected_plan = "Plan Anual (12 Meses)"
                st.session_state.auth_stage = "login"
                st.rerun()

    # ETAPA 2: AUTENTICACIÓN DE USUARIO (REDESIRECCIÓN AUTOMÁTICA TRAS ELEGIR PLAN)
    elif st.session_state.auth_stage == "login":
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.success(f"✅ Plan seleccionado: **{st.session_state.selected_plan}**")
            if st.button("🔄 Cambiar de Plan"):
                st.session_state.auth_stage = "planes"
                st.rerun()

            st.markdown("<h3 style='text-align: center;'>🔑 Paso 2: Autenticación de Usuario</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Ingresa tus credenciales para continuar con el doble factor de autenticación (2FA):</p>", unsafe_allow_html=True)
            
            with st.form("form_login_pestana"):
                correo_input = st.text_input("Correo electrónico / Usuario")
                password_input = st.text_input("Contraseña", type="password")
                btn_next = st.form_submit_button("Continuar a Verificación 2FA ➔", use_container_width=True)
                
                if btn_next:
                    if correo_input and password_input:
                        st.session_state.temp_user = correo_input.split('@')[0].capitalize()
                        # Generar código aleatorio de 4 dígitos para 2FA
                        st.session_state.mock_code = str(np.random.randint(1000, 9999))
                        st.session_state.auth_stage = "2fa_verify"
                        st.rerun()
                    else:
                        st.error("⚠️ Por favor ingresa tu correo y contraseña.")

    # ETAPA 3: DOBLE FACTOR DE AUTENTICACIÓN (2FA)
    elif st.session_state.auth_stage == "2fa_verify":
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.markdown("<h3 style='text-align: center;'>🔒 Paso 3: Doble Factor de Autenticación (2FA)</h3>", unsafe_allow_html=True)
            st.info(f"✉️ Hemos enviado un código de verificación de 4 dígitos a tu correo y mensaje de texto registrados.\n\n*(Código de simulación para pruebas: **{st.session_state.mock_code}**)*")
            
            with st.form("form_2fa"):
                codigo_ingresado = st.text_input("Ingresa el código de 4 dígitos", max_chars=4)
                btn_verify = st.form_submit_button("Verificar Código e Ingresar 🚀", use_container_width=True)
                
                if btn_verify:
                    if codigo_ingresado == st.session_state.mock_code:
                        st.session_state.autenticado = True
                        st.session_state.usuario_nombre = st.session_state.temp_user if "temp_user" in st.session_state else "Usuario"
                        st.success("¡Autenticación 2FA completada con éxito!")
                        st.rerun()
                    else:
                        st.error("❌ Código incorrecto. Por favor intenta de nuevo.")

            if st.button("⬅️ Regresar a Credenciales"):
                st.session_state.auth_stage = "login"
                st.rerun()

    st.divider()
    st.markdown('<p class="credits-text">DESARROLLADA Y CREADA POR: DR. ALEJANDRO CASTAÑEDA CORREA</p>', unsafe_allow_html=True)


# ==============================================================================
# PANTALLA DE LA APLICACIÓN OPERATIVA (CUANDO EL USUARIO YA INICIÓ SESIÓN)
# ==============================================================================
else:
    # Cabecera dentro de la app
    col_img_app, col_txt_app = st.columns([1, 4])
    with col_img_app:
        if os.path.exists(logo_path):
            st.image(logo_path, use_column_width=True)
    with col_txt_app:
        st.markdown('<p class="main-header">🐔 Engord-IA Pollo: Panel de Control Inteligente</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-slogan">«Inteligencia artificial que potencia la nutrición, optimiza la ganancia de peso y blinda la rentabilidad de tus pollos con precisión matemática.»</p>', unsafe_allow_html=True)

    st.divider()

    # Pestañas de navegación operativas
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
            st.metric("Aves Activas", f"{int(num_aves * (1 - mortalidad_max/100)):,}", f"Línea: {linea_genetica}")
        with col2:
            st.metric("Peso Promedio Actual", f"{peso_inicial/1000 + 2.11:.2f} kg", f"Meta: {peso_meta} kg")
        with col3:
            st.metric("Conversión Alimenticia (ICA)", f"{ica_objetivo}", "Óptimo")
        with col4:
            st.metric("Viabilidad Proyectada", f"{100 - mortalidad_max}%", "Excelente")
            
        st.info(f"💡 **Recomendación de IA ({linea_genetica}):** Con una temperatura de {temp_galpon}°C y humedad del {humedad_galpon}%, el confort térmico es adecuado. Se sugiere ajustar la densidad energética para cumplir con la meta de {peso_meta} kg en {dias_ciclo} días.")

    # --- TAB 2: DISEÑO Y OPTIMIZACIÓN DE DIETAS (LEAST-COST) ---
    with tab2:
        st.subheader("Módulo de Formulación de Dietas al Mínimo Costo (Programación Lineal)")
        st.markdown("El motor de optimización calcula las proporciones exactas de cada ingrediente disponible para satisfacer los requerimientos nutricionales al menor costo por kilo de alimento.")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            fase_etapa = st.selectbox("Fase de Engorda", ["Iniciador (1-10 días)", "Crecimiento (11-24 días)", "Finalizador / Retiro (25-42 días)"])
        
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
            st.metric("Costo Configurado Pollo BB", f"${costo_pollo_bb:.2f}")
            costo_alimento_kg = st.number_input("Costo Promedio Alimento ($/kg)", value=9.20)
        with col_c2:
            st.metric("Precio Venta Configurado", f"${precio_venta:.2f} /kg")
            mortalidad_estimada = st.slider("Mortalidad Configurada (%)", 1.0, 10.0, mortalidad_max)
        with col_c3:
            st.markdown("#### 📈 Estimación de Retorno")
            costo_total_estimado = costo_pollo_bb + (ica_objetivo * peso_meta * costo_alimento_kg) + 4.0
            margen_estimado = precio_venta - costo_total_estimado
            st.metric("Costo Estimado por Kilo", f"${costo_total_estimado:.2f}")
            st.metric("Margen Neto Proyectado", f"${margen_estimado:.2f} por kg", "Rentabilidad Alta")
            
        if st.button("Exportar Reporte Financiero para Comercialización"):
            st.balloons()
            st.success("¡Reporte generado y listo para enviar a compradores y socios comerciales!")
