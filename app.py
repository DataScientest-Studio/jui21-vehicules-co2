import streamlit as st
import pandas as pd

import intro
import visu
import modeles
import demo
import conclusion

# Variables globales
PAGES = {
    "Présentation du sujet": intro,
    "Visualisation des données": visu,
    "Modèles et résultats": modeles,
    "Démonstration": demo,
    "Conclusion et perspectives": conclusion
}
DATA_PATH = ('../Data/master_data_2014.csv')


# Fonction pour charger les données
@st.cache
def load_data():
    df = pd.read_csv(DATA_PATH, index_col = 0)
    return df

# Chargement des données
df = load_data()


# Affichage du menu sur le côté
st.sidebar.title('Emissions de CO2 des véhicules homologués')
selection = st.sidebar.radio("Menu", list(PAGES.keys()))
page = PAGES[selection]
page.app(df)
st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Auteurs :")
st.sidebar.markdown("Jian Hu  \nBruno Huart  \nEmilie Pottiez")
st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Projet DS  \nPromotion Continue Juillet 2021")





