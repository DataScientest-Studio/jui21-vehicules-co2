import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page de visualisation des données
def app(df):
    st.title("Visualisation des données")
    
    st.warning("Warning à enlever plus tard")

    st.subheader('Le jeu de données')

    st.write("Les données proviennent de l’ADEME (Agence De l'Environnement et de la Maîtrise de l'Énergie) et sont disponibles [ici](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_).")
    st.write("Le jeu de données contient 55 001 lignes et 14 colonnes après nettoyage. Chaque ligne représente un modèle de véhicule homologué.")   
    st.write("Aperçu des premières lignes de données :")
    st.dataframe(df.head())


    st.subheader('Corrélations entre les variables')

    st.write("Heatmap des corrélations :")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax, annot=True, cmap = 'magma')
    st.pyplot(fig)

    st.write("Relation entre la puissance maximale et l'émission de CO2 :")
    fig, ax = plt.subplots()
    sns.scatterplot(x='puiss_max', y='co2', data = df)
    st.pyplot(fig)
    
    st.title('Nouveau graphe à supprimer')
    st.write("Relation entre la puissance maximale et l'émission de CO2 :")
    fig, ax = plt.subplots()
    sns.scatterplot(x='puiss_max', y='co2', data = df)
    st.pyplot(fig)
