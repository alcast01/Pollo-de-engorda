import os

# --- BARRA LATERAL (BRANDING Y SUSCRIPCIONES) ---
with st.sidebar:
    # Carga segura de la imagen del logotipo
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
