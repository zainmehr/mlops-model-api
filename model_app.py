import streamlit as st
import joblib

# Charger le modèle entraîné
model = joblib.load("regression.joblib")

st.title("Prédiction du prix d'une maison")

# Trois champs de formulaire
size = st.number_input("Taille (m²)", min_value=0.0, value=100.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=3, step=1)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0, step=1)

# Prédiction
if st.button("Prédire"):
    prediction = model.predict([[size, nb_rooms, garden]])
    st.write(f"Prix estimé : {prediction[0]:,.2f}")