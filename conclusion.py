import streamlit as st

# Page de conclusion
def app(df, data_path):
    st.title("Conclusion")

    st.subheader('Résultats obtenus')
    st.markdown("""
    Au cours de ce projet, nous nous sommes aperçus très rapidement qu’il est 
    relativement simple de prédire l’émission de CO2 d’un véhicule à partir de quelques caractéristiques 
    générales (marque, gamme) et techniques (puissance, poids en ordre de marche), et ce de façon assez précise.
    """)

    st.subheader('Limitations')
    st.markdown("""
    Si la prédiction de l’émission de CO2 fonctionne bien pour une période et une génération de véhicules données, 
    la pérennité dans le temps d’un modèle de ce genre est largement remise en question par l’avancée technologique.
    \nNous avons en effet découvert en essayant de réaliser des prédictions sur des données de 2018 (pour rappel, 
    les données d'entraînement datent de 2014) que les résultats étaient déjà de nettement moins bonne qualité.
    """)

    st.subheader('Applications du modèle')
    st.markdown("""
    Une application possible de ce modèle pourrait être de prédire et mesurer la pollution actuelle en France due 
    à la circulation des véhicules. La difficulté serait d’identifier lesdits véhicules : cela revient à mesurer, 
    quantifier et identifier l’ensemble des véhicules du parc automobile Français.
    """)