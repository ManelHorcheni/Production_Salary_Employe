import os
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR


# Configuration de la page
st.set_page_config(page_title="Prédiction Salaire Employé", page_icon="💼", layout="centered")

# Créer un lien pour revenir à l'accueil
st.markdown('<a href="http://localhost:8501" target="_self">🏠 Retour à l\'accueil</a>', unsafe_allow_html=True)
    
st.title("💼 Prédiction du Salaire Mensuel")
st.markdown("Remplis les informations dans la barre latérale et clique sur **Prédire** pour estimer le salaire mensuel.")

# Barre latérale : Entrée utilisateur
st.sidebar.header("🎛️ Paramètres d'entrée")

# Entrées numériques
years = st.sidebar.slider("Années d'expérience", 0, 40, 5)
job_rate = st.sidebar.slider("Note de poste (Job Rate)", 1.0, 5.0, 3.0)
sick_leaves = st.sidebar.number_input("Congés maladie", 0, 100, 5)
unpaid_leaves = st.sidebar.number_input("Congés non payés", 0, 100, 2)
overtime_hours = st.sidebar.number_input("Heures supplémentaires", 0.0, 100.0, 5.0)

# Entrées catégorielles
gender = st.sidebar.selectbox("Genre", ["Male", "Female"])
department = st.sidebar.selectbox("Département", ["IT", "HR", "Sales", "Finance"])
country = st.sidebar.selectbox("Pays", ["France", "USA", "Germany", "UK"])

# Choix du modèle
model_choice = st.sidebar.selectbox("Choix du modèle", ["Régression Linéaire", "Random Forest", "Gradient Boosting", "SVR"])

# Bouton de prédiction
predict_btn = st.sidebar.button("🔮 Prédire le Salaire")

# Préparation des données (features d'entrée encodées à la main)
def encode_inputs():
    # Encodage simple à la main
    gender_encoded = 1 if gender == "Male" else 0
    dept_map = {"IT": 0, "HR": 1, "Sales": 2, "Finance": 3}
    country_map = {"France": 0, "USA": 1, "Germany": 2, "UK": 3}
    dept_encoded = dept_map[department]
    country_encoded = country_map[country]

    return np.array([[years, job_rate, sick_leaves, unpaid_leaves, overtime_hours, gender_encoded, dept_encoded, country_encoded]])

# Entraînement rapide d’un modèle sur des données fictives (pour test uniquement)
def train_dummy_model(model_name):
    # Générer un faux dataset (1000 lignes)
    np.random.seed(42)
    X_dummy = np.random.randint(0, 10, size=(1000, 8))
    y_dummy = 3000 + X_dummy[:, 0]*150 + X_dummy[:, 4]*50 + np.random.normal(0, 200, 1000)

    # Choix du modèle
    if model_name == "Régression Linéaire":
        model = LinearRegression()
    elif model_name == "Random Forest":
        model = RandomForestRegressor()
    elif model_name == "Gradient Boosting":
        model = GradientBoostingRegressor()
    else:
        model = SVR()

    model.fit(X_dummy, y_dummy)
    return model

# Prédiction et affichage
if predict_btn:
    input_data = encode_inputs()
    model = train_dummy_model(model_choice)
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Salaire mensuel prédit : **{prediction:.2f} €**")

# Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Réalisé par <strong>Manel Horchani</strong> 💻</div>", unsafe_allow_html=True)