import streamlit as st
import os

# Configuration
st.set_page_config(page_title="Accueil | Prédiction Salaire", page_icon="👋", layout="centered")

# Titre et image
st.markdown("<h1 style='text-align: center;'>Bienvenue 👋</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://img.freepik.com/vecteurs-premium/paiement-du-salaire-travailleur-masculin-regarde-son-salaire-son-telephone-portable-alors-qu-il-est-debout-calendrier-informatique_566886-11508.jpg?semt=ais_hybrid&w=740" width="250"/>
    </div>
    """,
    unsafe_allow_html=True
)


# Message
st.markdown(
    "<p style='text-align: center;'>Cette application permet de prédire le salaire mensuel d’un employé "
    "selon différents paramètres.</p>", unsafe_allow_html=True
)

# Bouton de redirection
if st.button("🔮 Aller à la prédiction"):
    # Redirige vers prediction.py en relançant Streamlit
    os.system("streamlit run prediction.py")

# Signature
st.markdown("---")
st.markdown("<p style='text-align: center; color: #ff6600;'>Projet réalisé par <strong>Manel Horchani</strong> 👩‍💻</p>", unsafe_allow_html=True)
