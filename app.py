import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

import intro
import visu
import modeles
import demo
import conclusion

# Variables globales
PAGES = {
    "Présentation du sujet": intro,
    "Visualisation des données": visu,
    "Modèles utilisés": modeles,
    "Démonstration": demo,
    "Conclusion et perspectives": conclusion
}


# Gestion des chemins

# Récupération du dossier courant
current_folder = os.path.dirname(__file__) 
# Récupération du dossier der données (dataset, images, ...)
data_path = os.path.join(current_folder, "data")


# Fonction pour charger les données
@st.cache
def load_data():
    df = pd.read_csv(os.path.join(data_path , "master_data_2014.csv"), index_col = 0)
    return df


# Chargement des données
df = load_data()


# Affichage du menu sur le côté
st.sidebar.title('Emissions de CO2 des véhicules homologués')

# Choix de la page
selection = st.sidebar.radio("Menu", list(PAGES.keys()))
page = PAGES[selection]
page.app(df, current_folder)
st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Auteurs :")
st.sidebar.markdown("Jian Hu  \nBruno Huart  \nEmilie Pottiez")
st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Projet DS  \nPromotion Continue Juillet 2021")





